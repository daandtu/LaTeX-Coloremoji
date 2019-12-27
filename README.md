# Coloremoji for LaTeX

A LaTeX package for outputting Emojis (🙂🐗🍈🕛) in your LaTeX files. The idea is taken from [this repository](https://github.com/alecjacobson/coloremoji.sty) which for me only worked for the pdflatex-compiler and does only contain 847 emoji images. This repository currently contains 1809 images.

### How it works
The library actually replaces the emoji characters with small images of the corresponding emoji. Therefore they can't be copied in the final PDF file. The emoji images are downloaded from [unicode.org](https://unicode.org/emoji/charts-13.0/full-emoji-list.html) via the script `generate_emojis.py`. Standard emoji images are from the Apple emoji font.  
Different skin tones are currently not supported.

### Setup
1. Clone the `coloremoji` directory and the `coloremoji.tex` file to the same directory as your main `.tex` file.
2. Copy `\input{coloremoji.tex}` into the preamble of your main `.tex` file.

### License
The code is licensed under the GPLv3: [http://www.gnu.org/licenses/gpl-3.0.html](http://www.gnu.org/licenses/gpl-3.0.html).
