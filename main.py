# coding: UTF-8

import sys
import re

ROW_MAX = 24
COLOUMN_MAX = 20

NUM = 0
TITLE = 1
ARTIST = 2
TIME = 3
BPM = 4
TRACK = 5
RELEASE = 6
LABEL = 7
GENRE = 8
KEY_TEXT = 9
KEY = 10
COMMENT = 11
LYRICS = 12
RATING = 13
FILE = 14
ANALYZED = 15
REMIXER = 16
PRODUCER = 17
RELEASE_DATE = 18
BITRATE = 19
COMMENT2 = 20
PLAY_COUNT = 21
LAST_PLAYED = 22
IMPORT_DATE = 23


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

f = open(argvs[1])
line = f.readline()
pattern = r"<tr>"


table = [["" for i in range(ROW_MAX)] for j in range(COLOUMN_MAX)]
i = 0
j = 0

# htmlのtableからListへ要素を格納
while line:
	if re.match(".*<th>", line):
		cell = re.sub(".*<th>","",line)
		cell = re.sub("</th>.*\n","",cell)
		table[i][j] = cell
		j += 1
	elif re.match(".*<td>", line):
		cell = re.sub(".*<td>","",line)
		cell = re.sub("</td>.*\n","",cell)
		table[i][j] = cell
		j += 1
	elif re.match(".*<tr>", line):
		j = 0
	elif re.match(".*</tr>", line):
		i += 1
	
	line = f.readline()

f.close


# Release DateをYearに更新
i = 0
for i in range(COLOUMN_MAX):
	table[i][RELEASE_DATE] = re.sub("Release Date", "Year", table[i][RELEASE_DATE])
	table[i][RELEASE_DATE] = re.sub("/../..", "", table[i][RELEASE_DATE])

# HTMLファイルに書き出す
f = open("hoge.txt", "w")
j = 0
f.write(table[NUM][j]+'\n')
f.write(table[TITLE][j]+'\n')
f.close()
print "finish!"
