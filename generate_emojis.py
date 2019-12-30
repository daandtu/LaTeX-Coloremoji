# -*- coding: utf-8 -*-
import urllib.request as ur
import os
#import traceback

head = r"""\ProvidesPackage{coloremoji}[2019/12/30]
\RequirePackage{graphicx}
\RequirePackage{ifxetex,ifluatex}
\RequirePackage[export]{adjustbox}

\DeclareOption{apple}{
  \def \emojidir {appl}
}
\DeclareOption{google}{
  \def \emojidir {goog}
}
\DeclareOption{fb}{
  \def \emojidir {fb}
}
\DeclareOption{joy}{
  \def \emojidir {joy}
}
\DeclareOption{win}{
  \def \emojidir {wind}
}
\DeclareOption{sams}{
  \def \emojidir {sams}
}
\DeclareOption{twtr}{
  \def \emojidir {twtr}
}

\ExecuteOptions{apple}
\ProcessOptions\relax

\newif\ifunicode
\ifxetex\unicodetrue\fi
\ifluatex\unicodetrue\fi

\ifunicode
  \RequirePackage{fontspec}
  \RequirePackage{newunicodechar}
  \newcommand{\DeclareUnicodeCharacter}[2]{%
    \begingroup\lccode`|=\string"#1\relax
    \lowercase{\endgroup\newunicodechar{|}}{#2}%
  }
\else
  \usepackage[utf8]{inputenc}
\fi

\newcommand{\coloremoji}[1]{\textrm{\includegraphics[width=0.95em,raise=-0.1em]{coloremoji/\emojidir/#1.jpg}\allowbreak}}

"""

vendor_list = ['appl', 'goog', 'fb', 'wind', 'twtr', 'joy', 'sams']
for v in vendor_list:
	if not os.path.exists(os.path.join('coloremoji', v)):
		os.makedirs(os.path.join('coloremoji', v))
		
page = ur.urlopen("https://unicode.org/emoji/charts-13.0/full-emoji-list.html").read()
print('Downloaded webpage. Start processing...')
contents = page.decode().split('<tr>')

count = 0
errorcount = 0
out = open('coloremoji.sty', 'w')
out.write(head)
for line in contents:
	try:
		
		name = line.split("name='", 1)[1].split("'>", 1)[0]
		image = line.split("src='")
		for i in range(7):
			try:
				image_name = os.path.join('coloremoji',vendor_list[i],'{}.jpg'.format(name.replace('_','')))
				ur.urlretrieve(image[i+1].split("'>", 1)[0], image_name)
			except:
				pass
				#print(traceback.format_exc())
		for i in name.split('_'):
			if int(i, 16) > 127: # Ignore ASCII character
				out.write('\DeclareUnicodeCharacter{%s}{{\coloremoji{%s}}}\n' % (i.upper(), name.replace('_','')))
		count += 1
	except:
		errorcount += 1
		#print(traceback.format_exc())

out.write(r'\endinput')
out.close()
print('Successfully downloaded {} emoji images.'.format(count))