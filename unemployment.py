import os
import unittest


def read_file(filename):
    """Returns the lines from the file named filename"""

    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    unemployment_file = open(full_path, "r", encoding="utf-8")
    lines = unemployment_file.readlines()
    unemployment_file.close()
    return lines


def create_dictionary(lines):
    """Returns a nested dictionary from the passed lines.
    The outer dictionary has a key of the country and the inner dictionary has the
    year as the key and the data as the value"""

    outerd = {}
    for line in lines[1:]:
        data_list = line.split(",")
        country = data_list[0]
        year = int(data_list[2])
        data = float(data_list[3])
        if country not in outerd:
            outerd[country] = {}
        outerd[country][year] = data
    return outerd


def year_with_highest_population(country, un_p):
    """returns the year that has the highest population for the given country"""
    innerd = un_p[country]
    max = -1
    max_year = -1
    for year in innerd:
        curr = innerd[year]
        if curr > max:
            max = curr
            max_year = year
    return max_year


def highest_ten_avg_unemp(
    start: int, end: int, un_d: dict[str, dict[str, float]]
) -> list[tuple[str, float]]:
    """returns a list of tuples for the 10 countries with the highest
    average unemployment rate in the year range from start to end inclusive"""
    dic_of_averages = {
        country: sum(rate for year, rate in rates.items() if start <= int(year) <= end)
        / len([rate for year, rate in rates.items() if start <= int(year) <= end])
        for country, rates in un_d.items()
    }
    return sorted(dic_of_averages.items(), key=lambda x: x[1], reverse=True)[:10]


def lowest_ten_avg_unemp(
    start: int, end: int, un_d: dict[str, dict[str, float]]
) -> list[tuple[str, float]]:
    """returns a list of tuples for the 10 countries with the highest
    average unemployment rate in the year range from start to end
    inclusive"""
    dic_of_averages = {
        country: sum(rate for year, rate in rates.items() if start <= int(year) <= end)
        / len([rate for year, rate in rates.items() if start <= int(year) <= end])
        for country, rates in un_d.items()
    }
    return sorted(dic_of_averages.items(), key=lambda x: x[1])[:10]


def highest_ten_total_unemp(
    year: int, un_d: dict[str, dict[str, float]], pop_d: dict[str, dict[str, float]]
) -> list[tuple[str, float]]:
    """returns a list of tuples for the 10 countries with the highest
    total unemployment in the year"""
    dic_of_total_unemployment = {
        country: ((pop_d[country][year]) * (un_d[country][year])) / 100
        for country in pop_d
        if year in pop_d[country] and country in un_d and year in un_d[country]
    }
    return sorted(dic_of_total_unemployment.items(), key=lambda x: x[1], reverse=True)[
        :10
    ]


class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.un_lines = read_file("unemployment-rate.csv")
        self.un_data = create_dictionary(self.un_lines)
        self.pop_lines = read_file("population.csv")
        self.pop_data = create_dictionary(self.pop_lines)

    def test_create_dictionary(self):
        self.assertIsInstance(self.un_data, dict, "Dictionary not created")
        self.assertEqual(len(self.un_data), 233)
        self.assertAlmostEqual(
            self.un_data["Afghanistan"][1993],
            12.368,
            2,
            "test of 1993 un data for Afghanistan",
        )
        self.assertAlmostEqual(
            self.un_data["Zimbabwe"][2017],
            5.011,
            2,
            "test of 2017 un data for Zimbabwe",
        )
        self.assertIsInstance(self.pop_data, dict, "Dictionary not created")
        self.assertEqual(
            self.pop_data["Afghanistan"][1993],
            15816601,
            "test of 1993 pop data for Afghanistan",
        )
        self.assertEqual(
            self.pop_data["Zimbabwe"][2017],
            14236599,
            "test of 2017 pop data for Zimbabwe",
        )
        self.assertEqual(len(self.pop_data), 244)

    def test_year_with_highest_pop(self):
        self.assertEqual(
            year_with_highest_population("Algeria", self.pop_data),
            2021,
            "testing year with highest pop for Algeria",
        )
        self.assertEqual(
            year_with_highest_population("Albania", self.pop_data),
            1990,
            "testing year with highest pop for Albania",
        )

    def test_lowest_10_avg_un(self):
        values = [
            ("Qatar", 0.14066666613022466),
            ("Cambodia", 0.19766666988531734),
            ("Niger", 0.344666669766108),
            ("Belarus", 0.48733333746592206),
            ("Laos", 0.6606666644414264),
            ("Myanmar", 0.7823333342870077),
            ("Thailand", 0.8733333150545758),
            ("Tonga", 1.10800000031789),
            ("Bahrain", 1.2083333333333333),
            ("Rwanda", 1.2313333352406832),
        ]
        out = lowest_ten_avg_unemp(2015, 2017, self.un_data)
        self.assertEqual(values, out, "test of lowest_ten_avg_unemp")

    def test_highest_10_avg_un(self):
        values = [
            ("Lesotho", 27.33400026957193),
            ("Palestine", 26.703332901000966),
            ("Eswatini", 26.35866673787437),
            ("South Africa", 26.346666336059567),
            ("Bosnia and Herzegovina", 26.105333328247067),
            ("Mozambique", 25.164999643961565),
            ("North Macedonia", 24.0566660563151),
            ("Greece", 23.31000010172527),
            ("Saint Lucia", 22.11100006103513),
            ("Namibia", 22.092332839965835),
        ]
        out = highest_ten_avg_unemp(2015, 2017, self.un_data)
        self.assertEqual(values, out, "test of highest_ten_avg_unemp")

    def test_highest_10_un_total(self):
        values = [
            ("World", 414027203.62649673),
            ("China", 66432771.579883926),
            ("India", 47161582.949703254),
            ("Brazil", 27683464.855741456),
            ("North America", 26480483.130568996),
            ("South Africa", 15580764.904805038),
            ("United States", 14173695.882834964),
            ("Nigeria", 13443203.208521716),
            ("Egypt", 11649300.90229515),
            ("Indonesia", 11062410.008096498),
        ]
        out = highest_ten_total_unemp(2017, self.un_data, self.pop_data)
        self.assertEqual(values, out, "highest_ten_total_unemp")


if __name__ == "__main__":
    unittest.main(verbosity=2)
