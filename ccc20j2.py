# Read input values
target_total = int(input())
infected_day1 = int(input())
total_people = int(input())


# Initialize variables
current_infected = infected_day1
total_infected = infected_day1
day_count = 0

# Simulate the spread of the disease
while total_infected <= target_total:
    current_infected *= total_people  # Each infected person infects exactly 'total_people' others
    total_infected += current_infected
    day_count += 1

# Output the result
print(day_count)