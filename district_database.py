import csv
from district import District

from constants import *


class DistrictDatabase:
    def __init__(
        self,
        districts_path=None,
        parlamentary2019_election_path=None,
        presidential2020_election_path=None,
    ):
        self._districts = {}

        if (
            districts_path is not None
            and parlamentary2019_election_path is not None
            and presidential2020_election_path is not None
        ):
            self.load_database(
                districts_path,
                parlamentary2019_election_path,
                presidential2020_election_path,
            )

    def load_database(
        self,
        districts_path,
        parlamentary2019_election_path,
        presidential2020_election_path,
    ):
        with open(districts_path, "r") as districts_file, open(
            parlamentary2019_election_path, "r"
        ) as parlamentary2019_election_file, open(
            presidential2020_election_path, "r"
        ) as presidential2020_election_file:
            self._read_database_from_file(
                districts_file,
                parlamentary2019_election_file,
                presidential2020_election_file,
            )

    def _read_database_from_file(
        self,
        districts_file,
        parlamentary2019_election_file,
        presidential2020_election_file,
    ):
        self._read_disctricts(districts_file)
        self._read_parlamentary_election(parlamentary2019_election_file)
        self._load_holownia(presidential2020_election_file)
        self.save_all_districts_state()

    def _read_disctricts(self, districts_file):
        reader = csv.DictReader(districts_file, delimiter=";")
        for row in reader:
            self._districts[row["Numer okręgu"]] = District(
                row["Siedziba OKW"], row["Numer okręgu"], row["Liczba mandatów"]
            )

    def _read_parlamentary_election(self, parlamentary2019_election_file):
        reader = csv.DictReader(parlamentary2019_election_file, delimiter=";")
        for row in reader:
            district_id = row["Numer okręgu"]

            # Set sum of votes
            self._districts[district_id].set_sum_of_votes(
                int(row["Liczba głosów ważnych"])
            )

            # Add votes for each party
            for party in LIST_OF_PARTIES:
                if party == "Inne":
                    other_votes = 0
                    for other_party in OTHER_PARTIES:
                        if row[other_party] != "":
                            other_votes += int(row[other_party])
                    self._districts[district_id].add_party("Inne", other_votes)
                else:
                    if row[party] != "":
                        self._districts[district_id].add_party(party, int(row[party]))
                    else:
                        self._districts[district_id].add_party(party, 0)

            # Scale votes to 100% if they do not sum up to sum of votes
            self._districts[district_id].rescale_votes_to_100_percent()

    def _load_holownia(self, presidential2020_election_file):
        reader = csv.DictReader(presidential2020_election_file, delimiter=";")
        holownia_votes_districts = {
            row["Numer okręgu"]: int(row["Szymon Franciszek HOŁOWNIA"])
            for row in reader
        }
        sum_of_votes_holownia = sum(holownia_votes_districts.values())
        sum_of_votes_psl = self.get_current_overall_results()["PSL"]

        # Rescale PSL votes to make space for PL2050 votes (approx by Holownia votes in presidetial
        # election) to create an electoral profile of Trzecia Droga
        scale_dict = {}
        scale_dict["PSL"] = POLL_PSL_APRIL2023_PERCENT / (
            POLL_PSL_APRIL2023_PERCENT + POLL_PL2050_APRIL2023_PERCENT
        )
        self.scale_results_in_all_districts(scale_dict)

        # Add PL2050 votes (they must sum up with PSL votes to PSL result in 2019 election)
        for district_id in holownia_votes_districts.keys():
            self._districts[district_id].add_votes(
                "PSL",
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

    def scale_results_in_all_districts(self, scale_dict):
        for district in self._districts.values():
            district.scale_votes(scale_dict)
            district.rescale_votes_to_100_percent()

    def get_district(self, id):
        return self._districts[id]

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
                party == "PSL"
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
                and party != "PSL"
            ):
                parties_over_threshold.append(party)
        return parties_over_threshold

    def get_number_of_mandates(self):
        mandates = {party: 0 for party in LIST_OF_PARTIES}
        parties_over_threshold = self.get_parties_over_threshold()

        for district in self._districts.values():
            district_mandates = district.get_number_of_mandates_dhont(
                parties_over_threshold
            )
            for party in district_mandates.keys():
                mandates[party] += district_mandates[party]

        return mandates

    def get_mandates_of_parties(self, parties):
        mandates_parties = 0

        for party, mandates in self.get_number_of_mandates().items():
            if party in parties:
                mandates_parties += mandates

        return mandates_parties
