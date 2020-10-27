# 实验三

------

1、安装pyqt5和pyqt5-tools

用以下命令安装

```
$ pip install -i https://mirrors.aliyun.com/pypi/simple/ pyqt5
$ pip install -i https://mirrors.aliyun.com/pypi/simple/ pyqt5-tools
```

2、使用QT designer绘制窗体

在X:\Python385\Lib\site-packages\pyqt5_tools\Qt\bin打开designer

绘制如下窗体

![05](https://suxas.github.io/images/exp03/05.png)

在右边的属性编辑器中分别修改windowTitle，QAbstractButton，如图

![01](https://suxas.github.io/images/exp03/01.png)

保存为ui文件，在文件目录下进行py文件编译

```
$pyuic5 -o [FileName].py [FileName].ui
```

新建项目，将写好的离散信号源代码与窗体源代码放入同一目录

在main中，定义编译函数绑定至按钮点击事件

```
import sys
import os
.
.
.
self.pushButton.clicked.connect(self.button1) 
.
.
.
def button1(self):
		str1=('python button1.py')
		os.system(str1)
```

加入PyQt主函数运行窗体

```
if __name__ == "__main__":
	app = QApplication(sys.argv)
	test_demo = Function()
	test_demo.show()
	sys.exit(app.exec_())
```

------

## [附源代码](https://github.com/suxas/suxas.github.io/tree/main/python/exp_3)

![02](https://suxas.github.io/images/exp03/02.png) 

![03](https://suxas.github.io/images/exp03/03.png) 

![04](https://suxas.github.io/images/exp03/04.png) 


