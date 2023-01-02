import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[born])
 
# Driver program

if __name__ == "__main__":
    date = input() #input format mm/dd/yyyy
    day = findDay(date)
    print(day.upper())


"""
Task

You are given a date. Your task is to find what the day is on that date.
"""