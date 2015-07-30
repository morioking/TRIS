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

argvs = sys.argv
argc = len(argvs)

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


# ffmpegにて画像を抽出する処理を書く



# HTMLファイルに書き出す
filename = re.sub("\..*","",argvs[1])
f = open(filename+'_out.html', "w")
i = 0
j = 0

f.write('<link href="./example.css" rel="stylesheet" type="text/css">\n')
f.write('<table class="example">\n')
f.write('<caption>'+filename+'</caption>\n')


f.write('<thead>\n')
f.write('<tr>\n')
#f.write('<th>'+table[i][NUM]+'</th>\n')
f.write('<th>#</th>\n') # Numは#に変更
f.write('<th>image</th>\n')
f.write('<th>'+table[i][TITLE]+'</th>\n')
f.write('<th>'+table[i][BPM]+'</th>\n')
f.write('<th>'+table[i][KEY]+'</th>\n')
f.write('<th>'+table[i][ARTIST]+'</th>\n')
f.write('<th>'+table[i][LABEL]+'</th>\n')
#f.write('<th>'+table[i][RELEASE_DATE]+'</th>\n')
f.write('<th>YEAR</th>\n') # Relase dateはYearに変更
f.write('</tr>\n')
f.write('</thead>\n')

f.write('<tbody>\n')

i = 1
while i < COLOUMN_MAX:
	if table[i][NUM] != "":
		f.write('<tr>\n')
		f.write('<td>'+table[i][NUM]+'</td>\n')
		f.write('<td><img src="./image/1.JPG " width="32" height="32"></td>\n')
		f.write('<td>'+table[i][TITLE]+'</td>\n')
		f.write('<td>'+re.sub("\..*","",table[i][BPM])+'</td>\n') #小数点以下は削除
		f.write('<td>'+table[i][KEY]+'</td>\n')
		f.write('<td>'+table[i][ARTIST]+'</td>\n')
		f.write('<td>'+table[i][LABEL]+'</td>\n')
		f.write('<td>'+re.sub("/../..", "", table[i][RELEASE_DATE])+'</td>\n')# 日付は削除
		f.write('</tr>\n')
	i += 1

f.write('</tbody>\n</table>\n')
f.close()
print "finish!"
