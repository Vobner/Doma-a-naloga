target_total = int(input())
infected_day1 = int(input())
total_people = int(input())

current_infected = infected_day1
total_infected = infected_day1
day_count = 0

while total_infected <= target_total:
    current_infected *= total_people  
    total_infected += current_infected
    day_count += 1

print(day_count)