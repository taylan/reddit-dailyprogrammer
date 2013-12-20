inp = '7 = +'
basestr, trunk, leaf = inp.split(' ')
base = int(basestr)
print('\n'.join([' ' * (base // 2) + leaf] + [' '*((base - i) // 2) + leaf*i for i in range(3, base+1, 2)] + [' '*((base - 3) // 2) + trunk*3]))
