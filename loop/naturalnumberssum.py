num_start = 1
num_end =int(input(f"Enter your upper range: "))
sum_n = 0
while(num_start <= num_end):
    sum_n = sum_n + num_start
    num_start = num_start + 1

print(f"Sum of first {num_end} natural numbers is = {sum_n}")