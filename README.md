# Coloremoji for LaTeX

A LaTeX package for outputting Emojis (🙂🐗🍈🕛) in your LaTeX files. The package is inspired from [this repository](https://github.com/alecjacobson/coloremoji.sty). However, this repository supports 1809 emojis and not only PDFLaTeX but also other compilers such as XeLaTeX and LuaLaTeX. Furthermore, multiple emoji designs can be choosen.

### How it works
The library replaces the emoji characters with small images of the corresponding emoji. Therefore they can't be copied in the final PDF file. The emoji images are downloaded from [unicode.org](https://unicode.org/emoji/charts-13.0/full-emoji-list.html) via the script [generate_emojis.py](generate_emojis.py). Standard emoji images are from Apples emoji font.  
Different skin tones are currently not supported.

### Setup
1. Download the [latest release](https://github.com/daandtu/LaTeX-Coloremoji/releases/) and unzip the files.
2. If you place the `coloremoji` directory and the `coloremoji.sty` file in the same directory as your main `.tex` file you can just use `\usepackage[<vendor>]{coloremoji}` in the preamble to include the package.  
If you place the files in another directory you have to use `\usepackage[<vendor>, directory=/path/to/emoji-dir]{/path/to/coloremoji-sty}`.  
Depending on `<vendor>` different emoji images are used. Possible values are `apple`,`google`,`facebook`,`joypixels`,`windows`,`samsung` and `twitter`. The default value is `apple`.

### Example
The LaTeX code (in this case used for math) `$😂 = \frac{😜}{😋} \cdot 💦$` will generate something like <img src="https://github.com/daandtu/coloremoji-latex/raw/master/example/example.png" alt="LaTeX Emoji example" width="200"/>.  
You can find the complete example code [here](example/example.tex).
