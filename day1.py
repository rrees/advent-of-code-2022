from day1data import calorie_list

calorie_totals = []
current_total = 0

for line in calorie_list.split("\n"):
    print(line)
    if len(line) == 0:
        calorie_totals.append(current_total)
        current_total = 0
        continue
    current_total += int(line)

print(max(calorie_totals))

sorted_calories = sorted(calorie_totals, reverse=True)

print(sum(sorted_calories[0:3]))