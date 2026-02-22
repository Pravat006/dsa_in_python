# 12. Check Leap Year

# So every year we are short by: 0.2422 day
#After 4 years: 0.2422 × 4 ≈ 0.97 ≈ 1 day 
# So we add 1 extra day every 4 years.
# thats why a leap year divisible by 4
# remove extra → every 100 years
#  restore balance → every 400 years

# leap year= year%4=0 and year%100 != 0    or year%400=0

def isLeap(year):
    if( (year%4==0 and year%100!=0) or year%400==0  ):
        return True
    else:
        return False

print(isLeap(2028))

