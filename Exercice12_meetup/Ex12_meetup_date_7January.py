
from datetime import datetime,date
from datetime import timedelta
from dataclasses import dataclass


@dataclass
class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

def meetup_date(rok, miesiac, nth=4, weekday=3):

    data_wyznaczona = date(rok,miesiac,1)
    delta_dzien = timedelta(days=1)
    licznik = 1

    if nth >= 0:
        while licznik <= nth:
            dzien = data_wyznaczona.weekday()
            if dzien == weekday:
                licznik += 1 
            data_wyznaczona += delta_dzien 
    else:
        licznik = 0
        data_wyznaczona = date(rok,miesiac+1,1) - delta_dzien
        while licznik != nth:
            dzien = data_wyznaczona.weekday()
            if dzien == weekday:
                licznik -= 1 
            data_wyznaczona -= delta_dzien 
        data_wyznaczona += 2*delta_dzien 
         




    return data_wyznaczona - delta_dzien

    






if __name__ == "__main__":
    a = meetup_date(2020, 1)
    print(a)
    print(meetup_date(2012, 3))
    # datetime.date(2012, 3, 22)
    print(meetup_date(2015, 2))
    # datetime.date(2015, 2, 26)
    print(meetup_date(2018, 6))
    # datetime.date(2018, 6, 28)
    print(meetup_date(2020, 1))
    # datetime.date(2020, 1, 23)

    print("SD Python:", meetup_date(2015, 8, nth=4, weekday=3))
    print("PyLadies on 4th Wed:", meetup_date(2018, 7, nth=4, weekday=2))
    print("SDJS on 1st Tues:", meetup_date(2012, 2, nth=1, weekday=1))

    print("SDHN on last Friday:", meetup_date(2010, 6, nth=-1, weekday=4))
    # SDHN on last Friday: 2010-06-25
    print("-1 != 4 (sometimes):", meetup_date(2020, 1, nth=-1, weekday=4))
    # -1 != 4 (sometimes): 2020-01-31
    print("Second to last Monday:",meetup_date(2018, 1, nth=-2, weekday=0))
    # datetime.date(2018, 1, 22)

    print("SDJS", meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY))
    # SDJS 2012-02-07
    print("PyLadies", meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY))
    # PyLadies 2018-07-11
    print("SDHN", meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY))
    # SDHN 2010-06-25