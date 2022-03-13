#!/usr/bin/env python3

# Create a data structure that is like a dictionary,
# but allows you to go in either direction.

# It can be a pair of functions that maps from X to Y and back again

# X <-> Y

# So if you give it a key, it will return a value, and if you give
# it a value, it will return a key. Assume values held in each side are of
# different types

class Mapping:
	def __init__(self, x_type, y_type):
		# maps keys of type x_type to values of type y_type
		self.X = {}
		# maps values to keys of type y_type to values of type x_type
		self.Y = {}
		self.x_type = x_type
		self.y_type = y_type

	def add(self, key, value):
		if(type(key) == self.x_type):
			self.X[key] = value
			self.Y[value] = key
		elif(type(key) == self.y_type):
			self.Y[key] = value
			self.X[value] = key
		else:
			print("Wrong types {}, {}".format(type(key), type(value)))
			print("Expected {} and {}".format(self.x_type, self.y_type))

	def get(self, key):
		if(type(key) == self.x_type):
			value = self.X.get(key)
			if(value):
				return value
			else:
				print("That key/value is not in the mapping")
				return None

		elif(type(key) == self.y_type):
			print(self.Y)
			value = self.Y.get(key)
			if(value):
				return value
			else:
				print("That key/value is not in the mapping")
				return None

		else:
			print("Wrong type {}".format(key))
			return None

TUPLE = (1,1,1)
INT = 1

def main():
	mapping = Mapping(type(TUPLE), type(INT))
	mapping.add(1, ('a', 'b', 'c'))
	mapping.add(('x', 'y', 'z'), 2)

	test(mapping)

def test(mapping):
	print("Mapping get 2")
	print("Should return ('x', 'y', 'z')")
	x = mapping.get(2)
	print(x)
	assert(x == ('x', 'y', 'z'))
	print('\n')

	print("Mapping get ('x','y','z')")
	print("Should return 2")
	y = mapping.get(('x', 'y', 'z'))
	print(y)
	assert(y == 2)
	print('\n')

	print("Mapping get 10")
	print("Should return 'not in the mapping'")
	k = mapping.get(10)
	print(k)
	assert(k is None)
	print('\n')

if __name__ == "__main__":
	main()
