import copy


class District:
    def __init__(self, name, id, n_seats, previous_results=None, number_of_votes=None):
        self._name = name
        self._id = id
        self._n_seats = int(n_seats)
        self._sum_of_votes = 0
        self._results = {}

        if number_of_votes is not None:
            self._sum_of_votes = number_of_votes

        if previous_results is not None:
            self._results = previous_results

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def get_n_seats(self):
        return self._n_seats

    def get_sum_of_votes(self):
        return self._sum_of_votes

    def get_previous_results(self):
        return self._results

    def set_sum_of_votes(self, number_of_votes):
        self._sum_of_votes = number_of_votes

    def get_number_of_votes(self, party):
        if self._results is None:
            return 0
        return self._results[party]

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

    def get_number_of_mandates_dhont(self, parties_over_threshold):
        # Initialize mandates
        mandates = {party: 0 for party in parties_over_threshold}

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
        return mandates

    def save_state(self):
        self._saved_results = copy.deepcopy(self._results)

    def reset(self):
        self._results = copy.deepcopy(self._saved_results)