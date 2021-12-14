polymer, insertion_input = open('input.txt').read().split('\n\n')

first = polymer[0]
last = polymer[-1]

insertions = {}
for insertion in insertion_input.split('\n'):
    l, r = insertion.split(' -> ')
    insertions[l] = r

pair_count = {}
for i in range(len(polymer) - 1):
    pair = polymer[i:i+2]
    pair_count[pair] = pair_count.get(pair, 0) + 1

for _ in range(40):
    new_pair_count = {}
    for pair, count in pair_count.items():
        if pair in insertions:
            left_pair = pair[0] + insertions[pair]
            right_pair = insertions[pair] + pair[1]
            new_pair_count[left_pair] = new_pair_count.get(left_pair, 0) + count
            new_pair_count[right_pair] = new_pair_count.get(right_pair, 0) + count
    pair_count = new_pair_count

freqs = {first : 1, last : 1}
for pair, count in pair_count.items():
    freqs[pair[0]] = freqs.get(pair[0], 0) + count
    freqs[pair[1]] = freqs.get(pair[1], 0) + count
print((max(freqs.values()) - min(freqs.values())) // 2)
