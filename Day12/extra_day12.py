from datetime import datetime as d


def age_in_minutes():
    while True:
        year = input("Enter your birth year : ")
        try:
            if len(year) != 4:
                print("Enter a four digits year")
            elif int(year) < 1900 or int(year) > 2023:
                print("Enter a valid year")
            else:
                now1 = int(d.now().strftime("%Y"))
                time = (now1 - int(year)) * 525600
                return print(f"you are {time:,} minutes old")
        except ValueError:
            print("Age entered must be an integer")


age_in_minutes()