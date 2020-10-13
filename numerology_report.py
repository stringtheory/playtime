import datetime

from numerology.life_path_calculator import life_path_calc as lpc
from numerology.reference_data import life_path_data


class MasterReport:
    """This Class Produces a Report for a given birthday."""

    def __init__(self, name, lpc_date):
        self.title = "Are You A Master {}?".format(name)
        self.name = name
        self.lpn_date = lpc_date

    def insert_newlines(self, string, every=80):
        """Return string with newline inserted every x letters
        TODO: split at words
        """
        lines = []
        for i in range(0, len(string), every):
            lines.append(string[i:i + every])
        return '\n'.join(lines)

    def get_life_path_data(self):
        """Print out funny copy"""
        life_path_number = lpc(self.lpn_date)
        data = next(item for item in life_path_data if item["number"] == life_path_number)
        birthday = self.lpn_date.strftime('%b %d, %Y')
        percent_string = str(round(data['percent'], 1))
        copy = self.insert_newlines(data['copy'])

        print(self.title)
        print("************************")
        print("Birthday: {}".format(birthday))
        print("Life Path Number: {}".format(data['display_name']))
        # Format Decimal into string and shorten

        print("The Chances of being a {}: {}%".format(life_path_number, percent_string))

        if data['master']:
            print("{} is a Master Number!!!!\n".format(data['display_name']))
        else:
            print("{} is not a Master Number but you are still special. \n".format(data['display_name']))
        print("--------------------------------------------------")
        print("Life Path Number{} \n".format(data['display_name']))
        print(copy)

jane = MasterReport("Jane", datetime.date(1990, 1, 1))
jane.get_life_path_data()
print("--------------------------------------------------")
print("--------------------------------------------------")
frank = MasterReport("Franklin", datetime.date(1979, 3, 11))
frank.get_life_path_data()
print("--------------------------------------------------")
print("--------------------------------------------------")
sara = MasterReport("Sara", datetime.date(1985, 3, 23))
sara.get_life_path_data()
