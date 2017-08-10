# Record how to build a basic image for nginx + php-fpm


## 0x01 php-fpm
pull images from hub
```
docker pull php:7.1-fpm
```
change the tag to get different version


## 0x02 nginx
pull nginx from 163hub
```
docker pull hub.c.163.com/library/nginx:latest
```

## 0x03 mysql(Not use this times)
pull mysql from 163hub
```
docker pull hub.c.163.com/library/mysql:5.6.36
```

## 0x04 Start a container for php-fpm
```
docker run --name php-fpm-7.1 -d -v ~/study/dockerfiledir:/var/www/html:ro php:7.1-fpm
```
1. --name 指定容器的名字
2. -d 后台运行
3. -v 把主机的~/study/dockerfiledir目录映射到容器的/var/www/html目录下 ro表示只读 
4. php:7.1-fpm表示来源镜像

## 0x05 Start a container for nginx
```
docker run --name nginx_server -d -p 80:80 -v ~/study/dockerfiledir:/usr/share/nginx/html:ro -v ~/study/containerconfig/nginx/conf.d:/etc/nginx/conf.d:ro --link php-fpm-7.1:php hub.c.163.com/library/nginx
```
1. -p 80:80 端口映射，把所创建的容器的80端口绑定到宿主机80端口
2. -d 后台运行
3. -v 目录映射
4. --link 建立容器间连接关系，把php-fpm-7.1容器的信息绑定到所创建容器的环境变量php中，则通过php这个别名即可访问到容器php-fpm-7.1

至此完成了nginx + php-fpm容器的创建，在docker官方文档中建议一个容器只运行一个应用，但是docker并没有限制对于一个容器运行多个应用的情况

为了方便对于多个容器互连的管理，可以使用开源docker项目管理工具docker-compose
