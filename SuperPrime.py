n = int(input("Enter a number: "))

count_n = 0
for i in range(1, n + 1):
  if n % i == 0:
    count_n += 1

temp = n
rev = 0
while temp > 0:
  rev = rev * 10 + (temp % 10)
  temp //= 10

count_rev = 0
for i in range(1, rev + 1):
  if rev % i == 0:
    count_rev += 1

temp = n
digit_sum = 0
while temp > 0:
  digit_sum += temp % 10
  temp //= 10

count_sum = 0
for i in range(1, digit_sum + 1):
  if digit_sum % i == 0:
    count_sum += 1

if count_n == 2 and count_rev == 2 and count_sum == 2:
  print("SUPER PRIME")
else:
  print("NOT A SUPER PRIME")