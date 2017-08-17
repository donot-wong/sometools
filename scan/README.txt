安装所需库：
pip install -r requirements.txt

运行（python版本为 2.7）：
python scanner.py 215.151.41.0/24
215.151.41.0/24为所需要扫描的网段

备注：时间紧，没有文件处理函数，建议将输出重定向至文件,命令为：
python scanner.py 215.151.41.0/24 > result.txt