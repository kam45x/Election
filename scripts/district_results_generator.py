#
# This script generates a csv file with results of the 2020 Polish presidential elections
# for Sejm districts. It uses data from the 2020 Polish presidential election results for powiats,
# because Sejm districts results for presidential election are not availaible on the PKW site.
#
import csv


class DistrictResultsGenerator:
    def __init__(self, powiat_results_path, districts_path, output_path):
        with open(powiat_results_path, "r") as powiat_results_file, open(
            districts_path, "r"
        ) as districts_file, open(output_path, "w") as output_file:
            self.generate_results(powiat_results_file, districts_file, output_file)

    def generate_results(self, powiat_results_file, districts_file, output_file):
        districts_reader = csv.DictReader(districts_file, delimiter=";")

        # csv.DictReader does not allow to iterate over the same instance twice,
        # so we need to write it into a list
        powiat_reader = csv.DictReader(powiat_results_file, delimiter=";")
        powiat_data = [row for row in powiat_reader]

        districts = []
        # We need to remove non-numeric keys from powiat_row
        non_numeric_keys = ["Nr OKW", "Województwo", "Powiat", "Kod TERYT"]

        for district_row in districts_reader:
            district_data = {
                "Numer okręgu": district_row["Numer okręgu"],
                "Nazwa": f'Okręg Wyborczy Nr {district_row["Numer okręgu"]}',
            }
            boundaries = district_row["Opis granic"]

            if "województwo" in boundaries:
                voivodeship = boundaries.removeprefix("województwo ")
                for powiat_row in powiat_data:
                    if powiat_row["Województwo"] == voivodeship:
                        for key in powiat_row.keys():
                            key = self.clear_key(key)
                            if key not in non_numeric_keys:
                                if key in district_data:
                                    district_data[key] += int(powiat_row[key])
                                else:
                                    district_data[key] = int(powiat_row[key])
            else:
                powiats_in_district = boundaries.split(", ")
                for powiat_row in powiat_data:
                    if powiat_row["Powiat"] in powiats_in_district:
                        for key in powiat_row.keys():
                            key = self.clear_key(key)
                            if key not in non_numeric_keys:
                                if key in district_data:
                                    district_data[key] += int(powiat_row[key])
                                else:
                                    district_data[key] = int(powiat_row[key])
            districts.append(district_data)

        self.write_results(districts, output_file)

    def write_results(self, districts, output_file):
        fieldnames = districts[0].keys()
        writer = csv.DictWriter(output_file, fieldnames, delimiter=";")
        writer.writeheader()
        for district_data in districts:
            writer.writerow(district_data)

    def clear_key(self, key):
        if "\ufeff" in key:
            key = key.removeprefix('\ufeff"')
            key = key.removesuffix('"')
        return key


if __name__ == "__main__":
    DistrictResultsGenerator(
        "wyniki_gl_na_kand_po_powiatach_utf8.csv",
        "okregi_sejm.csv",
        "districts_results_2020_AUTO.csv",
    )
