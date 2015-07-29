# coding: UTF-8

import sys
import re

ROW = 24
COLOUMN = 20

class MyClass:
	def __init__(self):
		self.name = "hoge"

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name


argvs = sys.argv
argc = len(argvs)


# a = MyClass()
# a.setName("start")
# print a.getName()


print argvs
print argc
print argvs[1]

print 'The content of %s ....' % argvs[1]
f = open(argvs[1])
line = f.readline()
pattern = r"<tr>"


table = [[0 for i in range(ROW)] for j in range(COLOUMN)]
i = 0
j = 0

while line:
	if re.match(".*<th>", line):
		if i < 10:
			table[i][j] = line
		print line
		print i
		j += 1
	if re.match("<tr>", line):
		i += 1
		#print line
	line = f.readline()
print table
f.close
