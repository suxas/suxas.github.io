## 使用方法：

main.py为主窗口文件，运行即可。

------

## 开发日志：

2020/11/26 知道了我们要做的东西是个叫DTMF的玩意，百度百科提供了很多资料

2020/11/26 找到了可用的DTMF分析源码，只进行了调试，没有修改

2020/12/10 找到了可用的DTMF识别源码，只进行了调试，没有修改

2020/12/20 修改了分析和识别源码，并设计了初版的GUI，将其命名为1.0能用版本

2021/1/1     继续修改分析和识别源码，由于遇到严重BUG重做GUI，将其命名为1.1还行版本（为什么我元旦还在写代码）

2021/1/5     最终完善了分析代码，分为单一音频信号分析和所有音频信号分析（加了个循环），并为分析源码和识别源码增加少许注释，重新制作了新版的GUI（因为突然加了所有音频分析的功能），将其命名为1.2一般版本，发布了第一个release

----------------------------------------------

项目内文件含义：

README.md：就是你现在看的这玩意，是开发日记desu.

single_analyzer.py：单个DTMF信号分析源码，可进行音频文件的频谱分析，并绘图输出

all_analyzer.py：所有DTMF信号分析源码，可进行音频文件的频谱分析，并绘图输出，用于找到DTMF信号分布规律

detector.py：DTMF信号识别源码，是最终识别出音频内容的输出工具

extensions.pylintrc：强行导入pyqt5的库，不让vs报错

main.py：编译后可运行的窗口main文件，最终的主文件，运行GUI和进行分析和识别操作.

window.ui：未经转换的pyqt-designer编译的GUI源文件.

--------------------------------------------------------

以下是文件夹：

samples：放入了从0到#所有的音频文件，用来统一分析并生成散点图（一般不用动）

test：默认放入一个拨号音为0的音频文件，可替换为任意拨号音（记得改为test），只有在这个文件夹中的文件才能进行转码和降噪处理，并进行分析识别。

------

## [源码](https://github.com/suxas/suxas.github.io/tree/main/python/exp_4)

## [发布包](https://github.com/suxas/suxas.github.io/releases)