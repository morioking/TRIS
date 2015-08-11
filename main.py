#! /usr/bin/python
# coding: UTF-8

import sys
import subprocess
import re
import commands

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
table = [["" for i in range(ROW_MAX)] for j in range(COLOUMN_MAX)]
i = 0
j = 0

# htmlからTableに
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

i = 0
Max_num = 0
while i < COLOUMN_MAX:
	if table[i][NUM] != "":
		Max_num = table[i][NUM]
	i += 1


# ffmpegを用いて画像を抽出する
print "extract image................"
imagefilepath = "./image/"+re.sub("\..*","",argvs[1])+"/"
subprocess.Popen(["mkdir",imagefilepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # UNIX only, Don't work on MS-DOS

i = 1
while i < COLOUMN_MAX:
	input_f = table[i][FILE]

	# mp3ファイルがない場合はwhileを抜ける
	if input_f == "":
		break

	input_f = input_f.replace('Macintosh HD','')
	input_f = input_f.replace('&amp;','&')
	input_f = input_f.replace(':','/')
	output_f = imagefilepath+table[i][NUM]+".jpg"

	# mp3のtag情報からfront coverのStreamを検索する
	p = subprocess.Popen(["ffmpeg","-i",input_f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout_data = p.stdout.read()
	stderr_data = p.stderr.read()
	stderr_data_list = stderr_data.split('\n')
	if i == 1: print stderr_data
	stream = -1
	map = ""
	tmp = 0
	for tmp in range(len(stderr_data_list)):
		if re.match(".*Stream", stderr_data_list[tmp]):
			stream += 1
			if re.match(".*front", stderr_data_list[tmp+2]):
				map = "0:"+str(stream)
				break

	# 画像を抽出する
	if map == "":
		p = subprocess.Popen(["ffmpeg","-i",input_f,output_f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	else:
		p = subprocess.Popen(["ffmpeg","-i",input_f,"-map",map,output_f], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	print "    "+table[i][TITLE] +" -> Stream #"+map

	i += 1


# export HTML file
print "export html................"
filename = re.sub("\..*","",argvs[1])+'_out.html'
f = open(filename, "w")
i = 0
j = 0

if int(Max_num) > 11:
	Image_width = 32 * 11 / int(Max_num)
	Image_height = 32 * 11 / int(Max_num)
else:
	Image_width = 32
	Image_height = 32


print "Image size is.........." + str(Image_width) + str(Image_height)



f.write('<link href="./example.css" rel="stylesheet" type="text/css">\n')
f.write('<table class="example">\n')
f.write('<caption>'+filename.replace('_out.html','')+'</caption>\n')


f.write('<thead>\n')
f.write('<tr>\n')
#f.write('<th>'+table[i][NUM]+'</th>\n')
f.write('<th>#</th>\n') # Num. is changed to # 
f.write('<th>.</th>\n') # Image row  is .
f.write('<th>'+table[i][TITLE]+'</th>\n')
f.write('<th>'+table[i][BPM]+'</th>\n')
f.write('<th>'+table[i][KEY]+'</th>\n')
f.write('<th>'+table[i][ARTIST]+'</th>\n')
f.write('<th>'+table[i][LABEL]+'</th>\n')
#f.write('<th>'+table[i][RELEASE_DATE]+'</th>\n')
f.write('<th>YEAR</th>\n') # Relase date is changed to Year
f.write('</tr>\n')
f.write('</thead>\n')

f.write('<tbody>\n')

i = 1
while i < COLOUMN_MAX:
	if table[i][NUM] != "":
		f.write('<tr>\n')
		f.write('<td>'+table[i][NUM]+'</td>\n')
		f.write('<td><img src="' + imagefilepath + str(i) + '.JPG " width="' + str(Image_width) + '" height="' + str(Image_height) + '"></td>\n')
		f.write('<td>'+table[i][TITLE]+'</td>\n')
		f.write('<td>'+re.sub("\..*","",table[i][BPM])+'</td>\n') #Omit the figures blow the decimal place
		f.write('<td>'+table[i][KEY]+'</td>\n')
		f.write('<td>'+table[i][ARTIST]+'</td>\n')
		f.write('<td>'+table[i][LABEL]+'</td>\n')
		f.write('<td>'+re.sub("/../..", "", table[i][RELEASE_DATE])+'</td>\n') # Omit date
		f.write('</tr>\n')
	i += 1

f.write('</tbody>\n</table>\n')
f.close()

print "convert html to pdf........"

p = subprocess.Popen(["wkhtmltopdf",filename,filename.replace('html', 'pdf')], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print "finish!"