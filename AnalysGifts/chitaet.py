with open('dbgifts.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

number_counts = {}
for number in numbers:
    if number not in number_counts:
        number_counts[number] = 0
    number_counts[number] += 1

sorted_numbers = sorted(number_counts.items(), key=lambda x: x[1], reverse=True)

with open('top.txt', 'a') as f:
    for number, count in sorted_numbers:
        f.write(f'{number}: {count}\n')
