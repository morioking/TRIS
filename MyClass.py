class MyClass:
	def __init__(self):
		self.name = "hoge"

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

a = MyClass()
print a.getName()
