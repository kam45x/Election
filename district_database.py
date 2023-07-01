import csv
from district import District

LIST_OF_PARTIES = ["PiS", "KO", "Lewica", "PSL", "Konfederacja", "Inne"]


class DistrictDatabase:
    def __init__(self, districts_path: None, previous_election_path: None):
        self._districts = {}
        self._was_loaded = False

        if districts_path is not None and previous_election_path is not None:
            self.load_database(districts_path, previous_election_path)
            self._was_loaded = True

    def load_database(self, districts_path, previous_election_path):
        with open(districts_path, 'r') as districts_file, \
                open(previous_election_path, 'r') as previous_election_file:
            self._read_database_from_file(
                districts_file, previous_election_file)

    def _read_database_from_file(self, districts_file, previous_election_file):
        self._read_disctricts(districts_file)
        self._read_previous_election(previous_election_file)

    def _read_disctricts(self, districts_file):
        reader = csv.DictReader(districts_file)
        for row in reader:
            self._districts[row["Numer okręgu"]] = District(
                row["Siedziba OKW"],
                row["Numer okręgu"],
                row["Liczba mandatów"]
            )

    def _read_previous_election(self, previous_election_file):
        reader = csv.DictReader(previous_election_file)
        for row in reader:
            district_id = row["Numer okręgu"]
            # Set sum of votes
            self._districts[district_id].set_sum_of_votes(
                int(row["Liczba głosów ważnych"]))
            # Add votes for each party
            for party in LIST_OF_PARTIES:
                self._districts[district_id].add_votes(
                    party, int(row[party]))
            # Scale votes to 100% if they do not sum up to sum of votes
            self._districts[district_id].rescale_votes_to_100_percent()
