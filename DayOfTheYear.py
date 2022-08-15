def isYearLeap(year):
    #Rok przestępny: f-cja zwraca 1. W pzeciwnym wypadku 0
    if year%100==0:
        if year%400==0:
            return True
        return False
    elif year%4==0:
        return True
    else: return False 

def daysInMonth(year, month):
    #Funkcja pokazuje ile jest dni w danym miesiącu roku
    monthLeap=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthNLeap=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year)== True:
        return monthLeap[int(month)-1]
    else:
        return monthNLeap[int(month)-1]

def dayOfYear(year, month, day):
#F-cja zwraca, który to dzień w roku
    if not day <= daysInMonth(year, month):
        return None
    monthLeap=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthNLeap=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if isYearLeap(year)== True:
        corDay=sum(monthLeap[:month-1]) + day
        return corDay
    else:
        corDay=sum(monthNLeap[:month-1]) + day
        return corDay
        

print(dayOfYear(2000, 12, 31))
