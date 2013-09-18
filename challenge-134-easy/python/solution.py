
inp = input("enter input: ")
params = [int(i) for i in inp.split(' ')]
n, m = params[0], params[1]
num = int('9' * n)
res = num - (num % m)
print(res)