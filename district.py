class District:
    def __init__(self, name, id, n_seats, previous_results: None,
                 number_of_votes: None):
        self._name = name
        self._id = id
        self._n_seats = n_seats
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

    def add_votes(self, party, votes):
        self._results[party] = votes

    # Scale votes by given scale, scale is a dict {party: scale}
    def scale_votes(self, scale_dict):
        for party in self._results:
            self._results[party] *= scale_dict[party]

    # If votes for all parties do not sum up to sum of votes,
    # which was set, scale them
    def rescale_votes_to_100_percent(self):
        if self._sum_of_votes > 0:
            scale = self._sum_of_votes / sum(self._results.values())
            self.scale_votes({party: scale for party in self._results})
