# class Generic:
# 	def __init__(self):
# 		self._x = 10

# 	def getter(self):
# 		return self._x

# 	def setter(self,value):
# 		print('set x')
# 		self._x = value

# 	def deleter(self):
# 		print('delete x')
# 		del self._x

# 	x = property(getter,setter,deleter)

class Generic:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        # add any other code
        return self._x

    @x.setter
    def x(self, value):
        # add any other code
        print('set x')
        self._x = value

    @x.deleter
    def x(self):
        # add any other code
        print('delete x')
        del self._x


# This is used to run any code when getting, changing, or deleting an instance
generic = Generic()
generic.x = 4
print(generic.x)
del generic.x


def decorator(func):
    def wrapper(*args, **kwargs):
        print('decoration begins')
        func(*args, **kwargs)
        print('decoration ends')

    return wrapper


@decorator  # same thing as func = decorator(func)
def function(func_parameter):
    print(func_parameter)


function('something')
