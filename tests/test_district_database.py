from ..scripts.district_database import DistrictDatabase

database = DistrictDatabase(
    districts_path="./data/okregi_sejm.csv",
    parlamentary2019_election_path="./data/wyniki_gl_na_listy_po_okregach_sejm.csv",
    presidential2020_election_path="./data/districts_results_2020_AUTO.csv",
    list_leaders_path="./data/jedynki.csv",
    population_path="./data/ludnosc_2022.csv",
    area_path="./data/powierzchnia.csv",
    load_holownia=False,
)


def test_distrcits_loaded():
    assert len(database.get_districts()) == 41


def test_sum_of_votes():
    assert database.get_sum_of_votes() == 18470710


def test_current_overral_results():
    results = database.get_current_overall_results()
    assert len(results) == 7


def test_get_results_percent():
    results = database.get_results_percent()
    assert results["PiS"] < 43.6 and results["PiS"] > 43.58
    assert results["KO"] < 27.41 and results["KO"] > 27.39
    assert results["Lewica"] < 12.57 and results["Lewica"] > 12.55
    assert results["TD"] < 8.56 and results["TD"] > 8.54
    assert results["Konfederacja"] < 6.82 and results["Konfederacja"] > 6.8
    assert results["MN"] < 0.18 and results["MN"] > 0.16


def test_get_parties_over_threshold():
    parties = database.get_parties_over_threshold()
    assert len(parties) == 6


def test_get_number_of_mandates():
    mandates = database.get_number_of_mandates()
    assert mandates["PiS"] == 235
    assert mandates["KO"] == 134
    assert mandates["Lewica"] == 49
    assert mandates["TD"] == 30
    assert mandates["Konfederacja"] == 11
    assert mandates["MN"] == 1


def test_simulate_poll_results():
    poll_results_percent = {
        "PiS": 20,
        "KO": 20,
        "Lewica": 20,
        "TD": 20,
        "Konfederacja": 20,
        "MN": 0,
        "Inne": 0,
    }
    database.simulate_poll_results(poll_results_percent, 0.1)
    results = database.get_results_percent()

    assert results["PiS"] < 20.1 and results["PiS"] > 19.9
    assert results["KO"] < 20.1 and results["KO"] > 19.9
    assert results["Lewica"] < 20.1 and results["Lewica"] > 19.9
    assert results["TD"] < 20.1 and results["TD"] > 19.9
    assert results["Konfederacja"] < 20.1 and results["Konfederacja"] > 19.9
    assert results["MN"] < 0.1
    assert results["Inne"] < 0.1


def test_get_mandates_flis():
    poll_results_percent = {
        "PiS": 20,
        "KO": 20,
        "Lewica": 20,
        "TD": 20,
        "Konfederacja": 20,
        "MN": 0,
        "Inne": 0,
    }
    mandates = database.get_number_of_mandates_flis(poll_results_percent)
    assert mandates["PiS"] == 92
    assert mandates["KO"] == 92
    assert mandates["Lewica"] == 92
    assert mandates["TD"] == 92
    assert mandates["Konfederacja"] == 92
