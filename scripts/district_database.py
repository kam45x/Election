import csv
from district import District

from constants import *


# Exception raised when max iterations in simulate_poll_results() is reached
class MaxIterationsError(Exception):
    def __init__(self, max_iterations):
        self.max_iterations = max_iterations
        super().__init__(f"Maximum iterations ({max_iterations}) reached at iteration")


class DistrictDatabase:
    def __init__(
        self,
        districts_path=None,
        parlamentary2019_election_path=None,
        presidential2020_election_path=None,
        list_leaders_path=None,
        population_path=None,
        area_path=None,
        load_holownia=True
    ):
        self._districts = {}

        if (
            districts_path is not None
            and parlamentary2019_election_path is not None
            and presidential2020_election_path is not None
            and list_leaders_path is not None
            and population_path is not None
            and area_path is not None
        ):
            self.load_database(
                districts_path,
                parlamentary2019_election_path,
                presidential2020_election_path,
                list_leaders_path,
                population_path,
                area_path,
                load_holownia
            )

    def load_database(
        self,
        districts_path,
        parlamentary2019_election_path,
        presidential2020_election_path,
        list_leaders_path,
        population_path,
        area_path,
        load_holownia
    ):
        with open(districts_path, "r") as districts_file, open(
            parlamentary2019_election_path, "r"
        ) as parlamentary2019_election_file, open(
            presidential2020_election_path, "r"
        ) as presidential2020_election_file, open(
            list_leaders_path, "r"
        ) as list_leaders_file, open(
            population_path, "r"
        ) as population_file, open(
            area_path, "r"
        ) as area_file:
            self._read_database_from_file(
                districts_file,
                parlamentary2019_election_file,
                presidential2020_election_file,
                list_leaders_file,
                population_file,
                area_file,
                load_holownia
            )

    def _read_database_from_file(
        self,
        districts_file,
        parlamentary2019_election_file,
        presidential2020_election_file,
        list_leaders_file,
        population_file,
        area_file,
        load_holownia
    ):
        self._load_disctricts(districts_file)
        self._load_parlamentary_election(parlamentary2019_election_file)
        if load_holownia:
            self._load_holownia(presidential2020_election_file)
        self._load_list_leaders(list_leaders_file)
        self._load_districts_population_and_area(population_file, area_file)
        self.save_all_districts_state()

    def _load_disctricts(self, districts_file):
        reader = csv.DictReader(districts_file, delimiter=";")
        for row in reader:
            self._districts[row["Numer okręgu"]] = District(
                name=row["Siedziba OKW"],
                id=row["Numer okręgu"],
                n_seats=int(row["Liczba mandatów"]),
                boundaries_description=row["Opis granic"],
            )

    def _load_parlamentary_election(self, parlamentary2019_election_file):
        reader = csv.DictReader(parlamentary2019_election_file, delimiter=";")
        for row in reader:
            district_id = row["Numer okręgu"]

            # Set sum of votes
            self._districts[district_id].set_sum_of_votes(
                int(row["Liczba głosów ważnych"])
            )

            # Set attendance
            self._districts[district_id].set_attendance_percent(
                int(row["Liczba wyborców, którym wydano karty do głosowania"])
                / int(row["Liczba wyborców uprawnionych do głosowania"])
                * 100
            )

            # Set votes per seat
            self._districts[district_id].set_votes_per_seat(
                int(row["Liczba głosów ważnych"])
                / self._districts[district_id].get_n_seats()
            )

            # Add votes for each party
            for party in LIST_OF_PARTIES:
                if party == "Inne":
                    other_votes = 0
                    for other_party in OTHER_PARTIES:
                        if row[other_party] != "":
                            other_votes += int(row[other_party])
                    self._districts[district_id].add_party("Inne", other_votes)
                elif party == "TD":
                    self._districts[district_id].add_party("TD", int(row["PSL"]))
                else:
                    if row[party] != "":
                        self._districts[district_id].add_party(party, int(row[party]))
                    else:
                        self._districts[district_id].add_party(party, 0)

            # Scale votes to 100% if they do not sum up to sum of votes
            self._districts[district_id].rescale_votes_to_100_percent()

        self.calculate_number_of_mandates_in_all_districts()

    def _load_holownia(self, presidential2020_election_file):
        reader = csv.DictReader(presidential2020_election_file, delimiter=";")
        holownia_votes_districts = {
            row["Numer okręgu"]: int(row["Szymon Franciszek HOŁOWNIA"])
            for row in reader
        }
        sum_of_votes_holownia = sum(holownia_votes_districts.values())
        sum_of_votes_psl = self.get_current_overall_results()["TD"]

        # Rescale PSL votes to make space for PL2050 votes (approx by Holownia votes in presidetial
        # election) to create an electoral profile of TD
        scale_dict = {}
        scale_dict["TD"] = POLL_PSL_APRIL2023_PERCENT / (
            POLL_PSL_APRIL2023_PERCENT + POLL_PL2050_APRIL2023_PERCENT
        )
        self.scale_results_in_all_districts(scale_dict)

        # Add PL2050 votes (they must sum up with PSL votes to PSL result in 2019 election)
        for district_id in holownia_votes_districts.keys():
            self._districts[district_id].add_votes(
                "TD",
                holownia_votes_districts[district_id]
                * (sum_of_votes_psl / sum_of_votes_holownia)
                * (
                    POLL_PL2050_APRIL2023_PERCENT
                    / (POLL_PL2050_APRIL2023_PERCENT + POLL_PSL_APRIL2023_PERCENT)
                ),
            )

        # Rescale votes to 100% in all districts
        for district in self._districts.values():
            district.rescale_votes_to_100_percent()

    def _load_list_leaders(self, list_leaders_file):
        reader = csv.DictReader(list_leaders_file, delimiter=",")
        for row in reader:
            district_id = row["Numer okręgu"]
            for party in LIST_OF_PARTIES:
                if party != "Inne":
                    list_leader = row[party]
                    if list_leader == "":
                        self._districts[district_id].set_list_leader(party, "-")
                    else:
                        self._districts[district_id].set_list_leader(party, list_leader)

    def _load_districts_population_and_area(self, population_file, area_file):
        # csv.DictReader does not allow to iterate over the same instance twice,
        # so we need to write it into a list
        population_reader = csv.DictReader(population_file, delimiter=";")
        area_reader = csv.DictReader(area_file, delimiter=";")
        population_data = [row for row in population_reader]
        area_data = [row for row in area_reader]

        for district in self._districts.values():
            boundaries = district.get_boundaries_description()

            if "województwo" in boundaries:
                voivodeship = boundaries.removeprefix("województwo ")
                for row in population_data:
                    if voivodeship.upper() in row["Nazwa"]:
                        district.set_population(int(row["ludność"]))
                        break
                for row in area_data:
                    if voivodeship.upper() in row["Nazwa"]:
                        district.set_area(int(row["powierzchnia"]))
                        break
            else:
                district_population = 0
                district_area = 0
                powiats_in_district = boundaries.split(", ")
                for powiat in powiats_in_district:
                    for row in population_data:
                        if powiat in row["Nazwa"]:
                            district_population += int(row["ludność"])
                            break
                    for row in area_data:
                        if powiat in row["Nazwa"]:
                            district_area += int(row["powierzchnia"])
                            break
                district.set_population(district_population)
                district.set_area(district_area)

    def get_district(self, id):
        return self._districts[id]

    def get_districts(self):
        return self._districts.values()

    def save_all_districts_state(self):
        for district in self._districts.values():
            district.save_state()

    def reset_all_districts_state(self):
        for district in self._districts.values():
            district.reset()

    def get_sum_of_votes(self):
        sum = 0
        for district in self._districts.values():
            sum += district.get_sum_of_votes()
        return sum

    def get_current_overall_results(self):
        results = {}
        for party in LIST_OF_PARTIES:
            results[party] = 0

        for district in self._districts.values():
            for party in LIST_OF_PARTIES:
                results[party] += district.get_number_of_votes(party)
        return results

    def get_results_percent(self):
        results_percent = {}
        sum_of_votes = self.get_sum_of_votes()
        for party, votes in self.get_current_overall_results().items():
            results_percent[party] = votes / sum_of_votes * 100
        return results_percent

    def scale_results_in_all_districts(self, scale_dict):
        for district in self._districts.values():
            district.scale_votes(scale_dict)
            district.rescale_votes_to_100_percent()

    def simulate_poll_results(self, poll_results_percent: dict, epsilon_percent: float):
        # Poll results in absolute numbers
        poll_results = {}
        for party in poll_results_percent.keys():
            poll_results[party] = (
                poll_results_percent[party] * self.get_sum_of_votes() / 100
            )

        # Max iterations in while loop
        MAX_ITERATIONS = 1000

        # Scale results in all districts until current results are almost equal to poll results
        it = 0
        while (
            not self.are_results_approx_equal(
                self.get_current_overall_results(), poll_results, epsilon_percent
            )
            and it < MAX_ITERATIONS
        ):
            scale_dict = {}
            current_results = self.get_current_overall_results()

            for party in poll_results_percent.keys():
                if current_results[party] != 0:
                    scale_dict[party] = poll_results[party] / current_results[party]
                else:
                    scale_dict[party] = 1

            self.scale_results_in_all_districts(scale_dict)
            it += 1

        if it == MAX_ITERATIONS:
            raise MaxIterationsError(MAX_ITERATIONS)

        self.calculate_number_of_mandates_in_all_districts()

    def calculate_number_of_mandates_in_all_districts(self):
        parties_over_threshold = self.get_parties_over_threshold()
        for district in self._districts.values():
            district.calculate_number_of_mandates_dhont(parties_over_threshold)

    def are_results_approx_equal(self, results1, results2, epsilon_percent):
        epsilon = epsilon_percent * self.get_sum_of_votes() / 100
        for party in LIST_OF_PARTIES:
            if abs(results1[party] - results2[party]) > epsilon:
                return False
        return True

    def get_parties_over_threshold(self):
        parties_over_threshold = []
        for party in LIST_OF_PARTIES:
            if (
                party == "TD"
                and self.get_current_overall_results()[party]
                > COALITION_TRESHOLD * self.get_sum_of_votes()
            ):
                parties_over_threshold.append(party)
            elif party == "MN":
                parties_over_threshold.append(party)
            elif party == "Inne":
                continue
            elif (
                self.get_current_overall_results()[party]
                > PARTY_TRESHOLD * self.get_sum_of_votes()
                and party != "TD"
            ):
                parties_over_threshold.append(party)
        return parties_over_threshold

    def get_number_of_mandates(self):
        mandates = {party: 0 for party in LIST_OF_PARTIES}

        for district in self._districts.values():
            district_mandates = district.get_number_of_mandates()
            for party in district_mandates.keys():
                if party in mandates.keys():
                    mandates[party] += district_mandates[party]
                else:
                    mandates[party] = district_mandates[party]

        return mandates

    # Implement Flis formula
    def get_number_of_mandates_flis(self, poll_results_percent):
        mandates = {party: 0 for party in LIST_OF_PARTIES}
        parties_over_threshold = []
        wasted_votes_percent = 0.0

        for party, percent in poll_results_percent.items():
            if (
                (party == "TD" and percent <= COALITION_TRESHOLD)
                or party == "Inne"
                or percent <= PARTY_TRESHOLD
            ):
                wasted_votes_percent += percent
            else:
                # MN should not be counted in Flis formula
                if party != "MN":
                    parties_over_threshold.append(party)

        for party in parties_over_threshold:
            n_parties_over_threshold = len(parties_over_threshold)
            mandates[party] = int(
                round(
                    (
                        (460 + 41 * n_parties_over_threshold / 2)
                        * poll_results_percent[party]
                        / (100 - wasted_votes_percent)
                        - 41 / 2
                    ),
                    0,
                )
            )

        return mandates
