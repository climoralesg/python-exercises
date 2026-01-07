#11	Calcula cuántos meses y días ha vivido una persona.
from datetime import date

day =int( input("Ingresa el numero del dia que naciste: "))
month = int(input("Ingresa el mes en numero: "))
year = int(input("ingresa el año: "))

birthdayDate = date(year,month,day)
'''
print(type(birthdayDate))
print(type(birthdayDate.strftime("%d/%m/%Y")))
print(f"{birthdayDate}")
'''
today = date.today()
yearCalculate = (today.year - birthdayDate.year)-1
monthCalculate = today.month
dayCalculate = today.day
mCalculate = yearCalculate * 12 + monthCalculate

'''
print(f"{yearCalculate} {monthCalculate} {dayCalculate}")
print(f"{yearCalculate}")
print(f"{today}")
'''

print(f"Months: {mCalculate}\nDays: {dayCalculate} ")