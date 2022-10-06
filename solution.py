'''
kamran ahmad khan
difficulty: 5%
run time:   0:00
answer:     2.223561019313554106173177
	***
751 Concatenation Coincidence
Find the only value of theta for which the concatenated sequence equals theta. Give your answer rounded to 24 places after the decimal point.
'''


from math import floor
from decimal import getcontext, Decimal as D

P = 24 # precision

getcontext().prec = P+1

def concat(theta):
	a = [floor(theta)]
	b = [theta]
	for _ in range(P+1):
		b.append(floor(b[-1])*(b[-1]-floor(b[-1])+1))
		a.append(floor(b[-1]))
	tau = D(str(a[0]) + "." + "".join(str(i) for i in a[1:]))
	return tau

assert str(concat(D('2.956938891377988'))).startswith('2.3581321345589')

theta = D(2)
tau = concat(theta)

while theta != tau:
	theta = tau
	tau = concat(theta)

print(str(round(tau, P)))
