# -*- coding: utf-8 -*-
import urllib.request as ur
import os
#import traceback

head = r"""\usepackage{graphicx}
\usepackage{ifxetex,ifluatex}

\newif\ifunicode
\ifxetex\unicodetrue\fi
\ifluatex\unicodetrue\fi

\ifunicode
  \usepackage{fontspec}
  \usepackage{newunicodechar}
  \newcommand{\DeclareUnicodeCharacter}[2]{%
    \begingroup\lccode`|=\string"#1\relax
    \lowercase{\endgroup\newunicodechar{|}}{#2}%
  }
\else
  \usepackage[utf8]{inputenc}
\fi

\newcommand{\coloremoji}[1]{\textrm{\includegraphics[width=1em]{coloremoji/img/#1.jpg}}}

"""
		
if not os.path.exists(os.path.join('coloremoji','img')):
    os.makedirs(os.path.join('coloremoji','img'))
		
page = ur.urlopen("https://unicode.org/emoji/charts-13.0/full-emoji-list.html").read()
print('Downloaded webpage. Start processing...')
contents = page.decode().split('<tr>')

count = 0
errorcount = 0
out = open('coloremoji.tex', 'w')
out.write(head)
for line in contents:
	try:
		
		name = line.split("name='", 1)[1].split("'>", 1)[0]
		image = line.split("src='", 1)[1].split("'>", 1)[0]
		image_name = os.path.join('coloremoji','img','{}.jpg'.format(name.replace('_','')))
		ur.urlretrieve(image, image_name)
		for i in name.split('_'):
			if int(i, 16) > 127: # Ignore ASCII character
				out.write('\DeclareUnicodeCharacter{%s}{{\coloremoji{%s}}}\n' % (i.upper(), name.replace('_','')))
		count += 1
	except:
		errorcount += 1
		#print(traceback.format_exc())

out.close()
print('Successfully downloaded {} emoji images.'.format(count))