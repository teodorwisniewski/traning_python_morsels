from datetime import datetime,date
from datetime import timedelta

def meetup_date(rok, miesiac, nth=4, weekday=3):
    
    
    delta_dzien = timedelta(days=1)
    liczydlo = 1
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    if nth>=0:
        data_aktualna = date(rok, miesiac, 1)
        while liczydlo<=nth:
        
            dzien_daty = weekDays[data_aktualna.weekday()]
            if dzien_daty == weekDays[weekday]: # 0 -> monday, 1->tuesday
                liczydlo +=1

            data_aktualna +=delta_dzien
    
        return data_aktualna - delta_dzien
    else:
        





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