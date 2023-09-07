import copy
from constants import *


class District:
    def __init__(
        self,
        name,
        id,
        n_seats,
        previous_results=None,
        number_of_votes=None,
        boundaries_description=None,
    ):
        self._name = name
        self._id = id
        self._n_seats = int(n_seats)

        self._boundaries_description = ""
        self._sum_of_votes = 0
        self._attendance_percent = 0
        self._votes_per_seat = 0
        self._results = {}
        self._mandates = {}
        self._list_leaders = {}
        self._population = 0
        self._area = 0

        if number_of_votes is not None:
            self._sum_of_votes = number_of_votes

        if previous_results is not None:
            self._results = previous_results

        if boundaries_description is not None:
            self._boundaries_description = boundaries_description

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_n_seats(self):
        return self._n_seats

    def get_sum_of_votes(self):
        return self._sum_of_votes

    def get_results(self):
        return self._results

    def get_list_leader(self, party):
        return self._list_leaders[party]

    def get_results_percent(self):
        results_percent = {}
        for party in self._results.keys():
            results_percent[party] = self._results[party] / self._sum_of_votes * 100
        return results_percent

    def get_attendance_percent(self):
        return self._attendance_percent

    def get_votes_per_seat(self):
        return self._votes_per_seat

    def get_number_of_votes(self, party):
        if self._results is None:
            return 0
        return self._results[party]

    def get_population(self):
        return self._population

    def get_area(self):
        return self._area

    def get_boundaries_description(self):
        return self._boundaries_description

    def set_sum_of_votes(self, number_of_votes):
        self._sum_of_votes = number_of_votes

    def set_list_leader(self, party, list_leader):
        self._list_leaders[party] = list_leader

    def set_attendance_percent(self, attendance_percent):
        self._attendance_percent = attendance_percent

    def set_votes_per_seat(self, votes_per_seat):
        self._votes_per_seat = votes_per_seat

    def set_population(self, population):
        self._population = population

    def set_area(self, area):
        self._area = area

    def add_party(self, party, votes):
        self._results[party] = votes

    def add_votes(self, party, votes):
        self._results[party] += votes

    # Scale votes by given scale, scale is a dict {party: scale}
    def scale_votes(self, scale_dict):
        for party in self._results:
            if party in scale_dict:
                self._results[party] *= scale_dict[party]

    # If votes for all parties do not sum up to sum of votes,
    # which was set, scale them
    def rescale_votes_to_100_percent(self):
        if self._sum_of_votes > 0:
            scale = self._sum_of_votes / sum(self._results.values())
            self.scale_votes({party: scale for party in self._results})

    def calculate_number_of_mandates_dhont(self, parties_over_threshold):
        # Initialize mandates
        mandates = {party: 0 for party in LIST_OF_PARTIES}

        # Initialize last divisors
        last_divisors = {party: 1 for party in parties_over_threshold}

        # Extract results for parties over threshold
        results_dhont = {
            party: self._results[party] for party in parties_over_threshold
        }

        # Calculate number of mandates
        for i in range(self._n_seats):
            party_max_value = max(results_dhont, key=results_dhont.get)
            mandates[party_max_value] += 1
            last_divisors[party_max_value] += 1
            results_dhont[party_max_value] = (
                self._results[party_max_value] / last_divisors[party_max_value]
            )

        self._mandates = mandates

    def get_number_of_mandates(self):
        return self._mandates

    def save_state(self):
        self._saved_results = copy.deepcopy(self._results)

    def reset(self):
        self._results = copy.deepcopy(self._saved_results)
        self._mandates = {}

    def __str__(self) -> str:
        return f"Okręg nr {self._id} ({self._name})"
