from pprint import pprint
N = 16
pprint([{'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)} for num in range(N)])
