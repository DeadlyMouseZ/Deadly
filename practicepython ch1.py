name = input("Write your name please")
age = input("Write your age please")
age_ = int(age)
from datetime import date
year_ = date.today().year
endyear = (year_-age_)+100
endyear_ = str(endyear)
print(name + " will be 100 in the year "+ endyear_)