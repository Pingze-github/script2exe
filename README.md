# script2exe
A python tool to convert .bat/.vbs or other script whitch can "click to run" to .exe automatically. Need GCC's support.

一个python工具，自动将.bat/.vps等可直接执行的脚本文件编译成.exe可执行文件。需要GCC的支持。

## Installation
1. Make sure you have Python2.7+.
2. Install [GCC](http://gcc.gnu.org/). Make sure you can run command "gcc" and "windres" in your terminal.
3. Download "script2exe.py"

## 安装
1. 确保你有Python2.7以上版本。
2. 安装[GCC](http://gcc.gnu.org/)。确保你能在终端中运行"gcc"和"windres"命令。
3. 下载"script2exe.py"。

## Usage
+ Run this command in your terminal:
```python script2exe.py test.bat```
+ You can also specify output .exe's position:
```python script2exe.py -i test.bat -o ./exe/test.exe```
+ You can add a icon for the .exe:
```python script2exe.py -i test.bat -c ./icons/test.ico -o ./exe/test.exe```

## 使用
+ 在终端中运行下面这行命令：
```python script2exe.py test.bat```
+ 你也可以指定输出.exe的位置：
```python script2exe.py -i test.bat -o ./exe/test.exe```
+ 你还可以为.exe添加一个图标：
```python script2exe.py -i test.bat -c ./icons/test.ico -o ./exe/test.exe```

## Others
The tool will create dir "bat/" and "temp/" in the tool's dir. You should not remove "bat/" for it's linked with the .exe. But you can remove the files in "temp/" as your wish.

## 其他
这个工具会在其所在目录内创建"bat/"和"temp/"两个目录。你不可以删除"bat/"，因为它储存了.exe调用的.bat文件。你可以自由地删除"temp/"内的文件，它们只是生成过程的中间文件。
