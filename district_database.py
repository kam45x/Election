class DistrictDatabase:
    def __init__(self, districts_path: None, previous_election_path: None):
        self._districts = {}
        self._was_loaded = False

        if districts_path is not None and previous_election_path is not None:
            self.load_database(districts_path, previous_election_path)
            self._was_loaded = True

    def load_database(self, districts_path, previous_election_path):
        pass

    def _read_database_from_file(self, districts_file, previous_election_file):
        pass

    def _read_disctricts(self, districts_file):
        pass

    def _read_previous_election(self, previous_election_file):
        pass