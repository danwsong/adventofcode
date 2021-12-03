def most_common(lst):
    return max(set(lst), key=lst.count)

def least_common(lst):
    return min(set(lst), key=lst.count)

bits = open('input.txt').read().split('\n')

gamma = ''
epsilon = ''
for i in range(len(bits[0])):
    column = [bits[j][i] for j in range(len(bits))]
    gamma += most_common(column)
    epsilon += least_common(column)

print(int(gamma, 2) * int(epsilon, 2))

