import collections

polymer, insertion_input = open('input.txt').read().split('\n\n')

insertions = {}
for insertion in insertion_input.split('\n'):
    l, r = insertion.split(' -> ')
    insertions[l] = r

for _ in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        if polymer[i:i+2] in insertions:
            new_polymer += insertions[polymer[i:i+2]]
    new_polymer += polymer[-1]
    polymer = new_polymer

freqs = collections.Counter(polymer).values()
print(max(freqs) - min(freqs))
