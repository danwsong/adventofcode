def most_common(lst):
    if lst.count('0') == lst.count('1'):
        return '1'
    return '0' if lst.count('0') > lst.count('1') else '1'

def least_common(lst):
    if lst.count('0') == lst.count('1'):
        return '0'
    return '0' if lst.count('0') < lst.count('1') else '1'

bits = open('input.txt').read().split('\n')

temp = bits
for i in range(len(temp[0])):
    column = [temp[j][i] for j in range(len(temp))]
    common = most_common(column)
    temp = list(filter(lambda x: x[i] == common, temp))
    if len(temp) == 1:
        oxygen = temp[0]
        break

temp = bits
for i in range(len(temp[0])):
    column = [temp[j][i] for j in range(len(temp))]
    common = least_common(column)
    temp = list(filter(lambda x: x[i] == common, temp))
    if len(temp) == 1:
        co2 = temp[0]
        break

print(int(oxygen, 2) * int(co2, 2))

