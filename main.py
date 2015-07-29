# coding: UTF-8

import sys
import re
import xml.dom.minidom

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
a.setName("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print a.getName()


print argvs
print argc
print argvs[1]

print 'The content of %s ....' % argvs[1]
f = open(argvs[1])
line = f.readline()
pattern = r"<tr>"
dom = xml.dom.minidom.parse(argvs[1])

print dom.documentElement.tagName
for node in dom.documentElement.childNodes:
	if node.nodeType == node.ELEMENT_NODE:
		print "    " + node.tagName

		for node2 in node.childNodes:
			if node2.nodeType == node2.ELEMENT_NODE:
				print "        " + node2.tagName


# while line:
# 	if re.match(pattern, line) != "None":
# 		print line 
# 	line = f.readline()
f.close
