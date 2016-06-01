"""COUNTING SUNDAYS Problem-19
Days are represented by the numbers of days since the January 1st 1900.
Lists of relevant days are drawn and the intersection is then taken.
In the end the cardinal of the intersection set is returned."""

max_year = 2001
start_year = 1900
start_counting_years = 1901
pos_days_to_compare = 6 #Monday starts at 0

non_leap_years = [31,28,31,30,31,30,31,31,30,31,30,31]
leap_years = [31,29,31,30,31,30,31,31,30,31,30,31]

days = [pos_days_to_compare]
first_of_month = [0]


#Filling months
for year in range(start_year,max_year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        for nb_days in leap_years:
            first_of_month.append(first_of_month[-1]+nb_days)
    else:
        for nb_days in non_leap_years:
            first_of_month.append(first_of_month[-1]+nb_days)

#Number of days to remove
to_remove = 0
for year in range(start_year,start_counting_years):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        to_remove += sum(leap_years)
    else:
        to_remove += sum(non_leap_years)

#Filling days
days = [d for d in xrange(first_of_month[-1]+1) if d % 7 == pos_days_to_compare and d >= to_remove]

#The wanted days are the one that are in both lists
print len(set(first_of_month).intersection(set(days)))