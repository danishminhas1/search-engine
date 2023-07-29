numbers = [19.8, 15.4, 11.4, 19.5, 10.1, 18.5, 14.1, 8.8, 14.9, 7.9, 17.6, 13.6, 7.5, 12.7, 16.7, 11.9, 15.4, 11.9, 15.8, 11.4, 15.4, 11.4]
sum = 0
for i in numbers:
    sum+=i

print(sum)

avg = sum/(len(numbers))
print(avg)
difference = []

for i in numbers:
    difference.append(i-avg)

print(difference)

difference_sqr = []

for i in difference:
    difference_sqr.append(i**2)

print(difference_sqr)

sum_diff_sqr = 0

for i in difference_sqr:
    sum_diff_sqr+=i

print(sum_diff_sqr)

print(sum_diff_sqr/21)