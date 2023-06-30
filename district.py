class District:
    def __init__(self, name, id, n_seats, votes_previous: None):
        self._name = name
        self._id = id
        self._n_seats = n_seats

        if votes_previous is not None:
            self._votes_previous = votes_previous

    def add_votes(self, party, votes_percent):
        if self._votes_previous is None:
            self._votes_previous = {}
        self._votes_previous[party] = votes_percent
