L = [[0]]
L *= 3
	#обход 
	L0 = [[0], [0], [0]]
	L1 = []
	[L.extend(deepcopy(L)) for i in range(3)]

__mul__
#слева от операнда
	class _int(int):
		def __mul__(self, other):
			print('hi')
			return super().__mul__(other)


# # # #
def f(x, l=[])
	for i in range(x):
		l.append(i * i)
	return l

f(2)
f(3, [0, 1, 2])
f(3)


# # # #
def f():
    l = [1]
    def inner(x):
        l.append(x)
        return l
    return inner

def g():
    y = 1
    def inner(x):
        y += x
        return y
    return inner

f_inner, g_inner = f(), g()

f_inner(2), g_inner(2)