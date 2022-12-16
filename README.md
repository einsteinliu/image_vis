### 给一个牛逼艺术家写的图片展示代码

打开一个Terminal

- 安装Python，git：

```bash
sudo apt install python3
sudo apt install python3-pip
sudo apt install git
```

- 克隆本项目到本地文件夹然后进入文件夹

```bash
git clone https://github.com/einsteinliu/image_vis.git
cd image_vis
```

- 安装本项目的依赖包

```bash
pip3 install -r requirements.txt
```

- 查看本机的IP地址

```bash
ifconfig
```

- 假设本机的ip是192.168.0.101，打开server.py文件，将ip改为192.168.0.101
- 打开一个terminal，执行下面的命令，现在一个网页后端就开始跑了：

```bash
python3 server.py
```

- 新建一个terminal，执行下面的命令，图片全屏显示中：

```bash
python3 image_viewer.py
```

- 按Esc键，退出显示
- 在局域网的任何一个浏览器里（比如手机浏览器）里访问这个网址http://192.160.0.101:5005/change 会发现图片切换到了下一张
