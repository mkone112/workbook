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