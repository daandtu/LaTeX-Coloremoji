# -*- coding: utf-8 -*-
import urllib.request as urlrequest
import os
import traceback

EMOJI_URL = 'https://unicode.org/emoji/charts-13.0/full-emoji-list.html'

vendor_list = ['apple', 'google', 'facebook', 'windows', 'twitter', 'joypixels', 'samsung']
for v in vendor_list:
	if not os.path.exists(os.path.join('coloremoji', v)):
		os.makedirs(os.path.join('coloremoji', v))

print('Fetch webpage...', end = '\r')
page = urlrequest.urlopen(EMOJI_URL).read()
print('Downloaded webpage. Start processing...')
page_content = page.decode().split('<tr>')

file = open('coloremoji.sty', 'r+')
output = ""
line = file.readline()
while '% Start declaring emojis' not in line and len(line) > 0:
	output += line
	line = file.readline()
output += '% Start declaring emojis\n'

count = 0
emojilist = []
for index, row in enumerate(page_content):
	if "class='code'" in row:
		print('Processing emoji {} ({:.2f}%)'.format(count, index / len(page_content) * 100), end = '\r')
		unicode_name = row.split("name='", 1)[1].split("'>", 1)[0]
		images = row.split("src='")
		for i in range(7):
			try:
				image_name = os.path.join('coloremoji', vendor_list[i],'{}.png'.format(unicode_name.replace('_','')))
				urlrequest.urlretrieve(images[i+1].split("'>", 1)[0], image_name)
			except:
				pass
		for i in unicode_name.split('_'):
			if int(i, 16) > 127 and i not in emojilist: # Ignore ASCII character and prevent double declaration
				output += r'\DeclareUnicodeCharacter{{{}}}{{{{\coloremoji{{{}}}}}}}'.format(i.upper(), unicode_name.replace('_','')) + '\n'
				emojilist.append(i)
		count += 1

line = file.readline()
while len(line) > 0:
	if 'DeclareUnicodeCharacter' not in line:
		output += line
	line = file.readline()

file.seek(0)
file.write(output)
file.truncate()
file.close()

print('Successfully downloaded {} emoji images.'.format(count))