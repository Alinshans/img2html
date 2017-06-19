# img2html: Convert a image to HTML   ![WTFPL License][license-badge]


`img2html` 用于将图片转化为 HTML 页面，并没有什么实际作用，只是为了好玩。

```
                                 ___      __          __                    ___
 __                            /'___`\   /\ \        /\ \__                /\_ \
/\_\     ___ ___       __     /\_\ /\ \  \ \ \___    \ \ ,_\    ___ ___    \//\ \
\/\ \  /' __` __`\   /'_ `\   \/_/// /__  \ \  _ `\   \ \ \/  /' __` __`\    \ \ \
 \ \ \ /\ \/\ \/\ \ /\ \L\ \     // /_\ \  \ \ \ \ \   \ \ \_ /\ \/\ \/\ \    \_\ \_
  \ \_\\ \_\ \_\ \_\\ \____ \   /\______/   \ \_\ \_\   \ \__\\ \_\ \_\ \_\   /\____\
   \/_/ \/_/\/_/\/_/ \/___L\ \  \/_____/     \/_/\/_/    \/__/ \/_/\/_/\/_/   \/____/
                       /\____/
                       \_/__/
```


### 示例

|原始图片 |  转换后|
|:-----------:|:----------:|
|![Python logo](http://i2.muimg.com/594413/4498516ba1014e6fs.jpg) |![Python logo html](http://i2.muimg.com/594413/a4ac532b374791f7s.jpg)|

### 需要

* Python 2.7

### 注意

我 `fork` 了 xlzd 的 [https://github.com/xlzd/img2html](https://github.com/xlzd/img2html)，并对原作者的代码做了一些修改，主要修改如下：

* 若使用命令行时没有输入文件，则会显示帮助
* 若使用命令行时没有输出文件，会自动创建一个跟输入文件同级、同名的，扩展名为 `.html` 的文件

如果你要使用我这个版本，那么你可以按照下面的方法进行。

### 使用

首先你可以通过 `git clone` 或 [`Download Zip`](https://github.com/Alinshans/img2html/archive/master.zip) 获取文件。

```
$ git clone git@github.com:Alinshans/img2html.git
```

然后你可以安装这个脚本，就能直接在任意位置使用命令行运行了，若不想安装这个脚本，也可以跳过这个步骤。
```
$ cd img2html
$ python setup.py install
```

#### 安装脚本后命令行调用
```
usage: img2html [-h] [-b #RRGGBB] [-s 1~32] [-c CHAR] [-t TITLE] [-f FONT]
                [-i SRC_FILE] [-o OUT_FILE]

img2html : Converts the image to HTML

optional arguments:
  -h, --help            show this help message and exit
  -b #RRGGBB, --background #RRGGBB
                        background color (#RRGGBB format)
  -s (1~32), --size (1~32)
                        text font size (int)
  -c CHAR, --char CHAR  characters for HTML text
  -t TITLE, --title TITLE
                        html title
  -f FONT, --font FONT  html font
  -i SRC_FILE, --in SRC_FILE
                        the image to convert
  -o OUT_FILE, --out OUT_FILE
                        output file
```
例：
```
img2html -i D:\mm.jpg -o D:\gg.html
```
#### 未安装脚本使用命令行运行
先按 **使用 IDE 运行** 中的方法修改文件，然后在 `__init__.py` 的目录下打开命令行，调用：
```
python __init__.py -i D:\a.html
```

#### 使用 IDE 运行

打开 `__init__.py`，在如下位置做修改：
```Python
###########################################################################
    # Modifies here to run code.

    # Directly sets to input path, e.g.:
    #src_file = 'D:\\a.jpg'
    src_file = getattr(args, 'in')

    # Directly sets to output path, e.g.:
    #out_file = 'D:\\a.html'
    out_file = args.out

    if src_file:
        # Sets the conversion configuration information.
        converter_config = Img2HTMLConverter(
            font_size=args.size,
            char=args.char,
            background=args.background,
            title=args.title,
            font_family=args.font,
        )
        html = converter_config.convert(src_file)
    ###########################################################################
```
然后 `Run '__init__'`。


[license-badge]:   https://img.shields.io/badge/license-WTFPL-007EC7.svg
