nums = list(map(int, open('input.txt').read().split(',')))

freq = {num : nums.count(num) for num in nums}

def cost(a, b):
    return abs(a - b)

print(min(sum(cost(base, crab) * freq[crab] for crab in freq) for base in range(min(nums), max(nums) + 1)))
