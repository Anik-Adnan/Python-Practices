n = int(input())
even = (n) // 2
odd = (n+1)//2
sum_even = even * (even + 1)
sum_odd = odd * odd
print(sum_even-sum_odd)
