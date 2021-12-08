nums = [num for line in open('input.txt').read().split('\n') for num in line.split(' | ')[1].split(' ')]
print(len(list(filter(lambda x: len(x) in [2, 3, 4, 7], nums))))
