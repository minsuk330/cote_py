import sys

def input():
    return sys.stdin.readline().rstrip()

N = input()
mapping = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'
}
result = []

for i, num in enumerate(N):
    bi = mapping[num]

    if i == 0:
        result.append(bi.lstrip('0') or '0')
    else:
        result.append(bi)

print(''.join(result))
    