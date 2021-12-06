nums = list(map(lambda x: int(x) + 1, open('input.txt').read().split(',')))

freq = {num : nums.count(num) for num in range(7)}
next_freq = {num : 0 for num in range(7)}

days_to_sim = 256

for day in range(0, days_to_sim + 1):
    n = freq[day % 7]
    freq[day % 7] += next_freq[day % 7]
    next_freq[day % 7] = 0
    next_freq[(day + 2) % 7] += n
    print(day, sum(freq.values()) + sum(next_freq.values()))

print(sum(freq.values()) + sum(next_freq.values()))
