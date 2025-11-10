from datetime import date
year=int(input('Digite um ano. digite zero para analisar o ano atual:'))
if year == 0:
    year = date.today().year
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f'The year {year} is leap!')
else:
    print('This year is not leap :(')