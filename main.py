# coding: UTF-8

import sys
import re

argvs = sys.argv
argc = len(argvs)

class MyClass:
	def __init__(self):
		self.name = "hoge"

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name




a = MyClass()
a.setName("start")
print a.getName()


print argvs
print argc
print argvs[1]

print 'The content of %s ....' % argvs[1]
f = open(argvs[1])
line = f.readline()
pattern = r"<tr>"

i = 0
j = 0
table[[]]
print table

while line:
	if re.match("<tr>", line):
		print line
	line = f.readline()
f.close
