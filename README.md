# PDF转word
可实现批量pdf转word

## 直接安装

windows [下载地址](https://github.com/Shanyaliux/pdf2word/releases/download/1.0.0/pdf2word.exe)

## 源码编译

```shell
pip install -r requirements.txt
pyinstaller -F -w imageBrowser.py -p {your site-packages path}
#例如我的site-packages path是 D:\Software\Miniconda3\envs\pdf2word\Lib\site-packages
```

## 自定义

克隆仓库进行修改并编译即可

```shell
git clone https://github.com/Shanyaliux/pdf2word.git
```

> 若想要对UI界面进行修改，则自行安装`qtdesigner`修改`MainWindow.ui`并编译
