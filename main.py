# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from datetime import date

from dateutil.relativedelta import relativedelta


if __name__ == '__main__':
    current_date = date.today()
    max_pr_open_date = current_date - relativedelta(months=6)
    a=0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
