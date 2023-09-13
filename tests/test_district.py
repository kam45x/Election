from ..scripts.district import District


def test_contructor():
    district = District("test", 1, 3)
    assert district.get_name() == "test"
    assert district.get_id() == 1
    assert district.get_n_seats() == 3


def test_sum_of_votes():
    district = District("test", 1, 3)
    district.set_sum_of_votes(100)
    assert district.get_sum_of_votes() == 100


def test_list_leader():
    district = District("Chełm", 1, 3)
    district.set_list_leader("PPU", "Paweł Kozioł")
    assert district.get_list_leader("PPU") == "Paweł Kozioł"


def test_attendance_percent():
    district = District("test", 1, 3)
    district.set_attendance_percent(50)
    assert district.get_attendance_percent() == 50


def test_votes_per_seat():
    district = District("test", 1, 3)
    district.set_votes_per_seat(100)
    assert district.get_votes_per_seat() == 100


def test_add_party():
    district = District("test", 1, 3)
    district.add_party("PPU", 1000)
    district.add_party("PO", 3000)
    district.set_sum_of_votes(4000)
    assert district.get_number_of_votes("PPU") == 1000
    assert district.get_results_percent()["PPU"] == 25


def test_dhont():
    results = {"A": 100, "B": 200, "C": 300}
    district = District("test", 1, 5, results, 600)
    district.calculate_number_of_mandates_dhont(["A", "B", "C"])
    mandates = district.get_number_of_mandates()
    assert mandates["A"] == 0
    assert mandates["B"] == 2
    assert mandates["C"] == 3
