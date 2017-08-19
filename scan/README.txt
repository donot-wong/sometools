## Instroduction
今天领导安排任务，要一个扫描器
可以扫整个网段。并且爬取网页title
用的IPy处理网段
libnmap做扫描引擎
bs4解析网页获取title

## Install Dependes
pip install -r requirements.txt

## Usage
python scanner.py 215.151.41.0/24
215.151.41.0/24

python scanner.py 215.151.41.0/24>result.txt
