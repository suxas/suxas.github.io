

## 1、申请Github账号

①进入Github官网	https://github.com/

![1602324102314](C:\Users\Suxas\AppData\Local\Temp\1602324102314.png)

②输入用户名，邮箱，密码，验证码

![1602324176878](C:\Users\Suxas\AppData\Local\Temp\1602324176878.png)

③建立完毕

## 2、安装VCCODE

①进入官网 https://code.visualstudio.com/

![1602324406243](C:\Users\Suxas\AppData\Local\Temp\1602324406243.png)

②点击下载安装

![1602324474081](C:\Users\Suxas\AppData\Local\Temp\1602324474081.png)

③安装汉化：按下快捷键ctrl+shift+p，输入搜索configuration display language，选择Install additional languages，安装简体中文汉化包

![1602324562608](C:\Users\Suxas\AppData\Local\Temp\1602324562608.png)

![1602324619018](C:\Users\Suxas\AppData\Local\Temp\1602324619018.png)

④重启软件

![1602324658440](C:\Users\Suxas\AppData\Local\Temp\1602324658440.png)

⑤汉化完成

![1602324759245](C:\Users\Suxas\AppData\Local\Temp\1602324759245.png)

## 3、实现Github在本地端和云端的数据同步

①云端建立Github库

在个人主页下点击NEW，按照下图配置

![1602325358277](C:\Users\Suxas\AppData\Local\Temp\1602325358277.png)

![1602325455535](C:\Users\Suxas\AppData\Local\Temp\1602325455535.png)

②打开Git官网 https://git-scm.com/，下载并安装

![1602324867944](C:\Users\Suxas\AppData\Local\Temp\1602324867944.png)

②在Git命令行模式下 输入如下命令，配置username和useremail

```
git config --global user.name "username"
git config --global user.email "example@example.com"
```

输入git config --list，显示user.name和user.email即为成功

![1602325087395](C:\Users\Suxas\AppData\Local\Temp\1602325087395.png)

③建立SSH并连接至Github

创建密钥文件

```
ssh-keygen -t rsa -C example@example.com（改为自己的邮箱）
```

大部分情况下，密钥生成在C:\Users\电脑用户名\\.ssh路径下

![1602325245167](C:\Users\Suxas\AppData\Local\Temp\1602325245167.png)

第一个文件是私钥，第二个文件是公钥。将公钥文件以记事本类型打开，复制里面的内容。进入Github自己建立的库中，选择Settings→Deploy keys→Add deploy key

![1602325675637](C:\Users\Suxas\AppData\Local\Temp\1602325675637.png)

在Git命令行中 输入

```
ssh -T git@github.com
```

显示You‘ve successfully authenticated即成功。

![1602325726702](C:\Users\Suxas\AppData\Local\Temp\1602325726702.png)

④本地建立Github库

```
1、新建目录（名字必须英文）
2、在Git命令行下输入git init
3、在Git命令行下输入git clone git@github.com:用户名/库名称.github.io.git
4、在Git命令行下输入git status，如图所示即为成功
```

![1602325920936](C:\Users\Suxas\AppData\Local\Temp\1602325920936.png)

⑤拉取云端文件

```
在Git命令行下输入 git pull
```

⑥修改本地文件并上传

在本地库文件夹新建一个文件1.txt

```
1、在Git命令行下输入git status，确认文件变动
2、在Git命令行下输入git add 1.txt(第一次新建文件需输入)
3、在Git命令行下输入git commit -m 1.txt（-m参数取消对文件的描述）
4、在Git命令行下输入git push，即上传至云端
```

