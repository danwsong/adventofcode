nums = list(map(int, open('input.txt').read().split(',')))

freq = {num : nums.count(num) for num in nums}

def cost(a, b):
    dist = abs(a - b)
    return dist * (dist + 1) // 2

print(min(sum(cost(base, crab) * freq[crab] for crab in freq) for base in range(min(nums), max(nums) + 1)))
