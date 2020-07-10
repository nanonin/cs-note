# docker-note

## docker images

```Shell
# list docker images
docker images

# download docker image
docker pull ubuntu:13.10

# remove docker image
docker rmi ubuntu

# commit docker container as image
docker ps
docker commit -m="ubuntu nginx" -a="vvyun" 0b2ab724e6e5 custom/ubuntu:v1

# tag docker image
docker tag 0b2ab724e6e5 custom/ubuntu:v2
```

## docker container

```Shell

docker ps -a

docker run -it ubuntu /bin/bash

docker start 0b2ab724e6e5

docker stop 0b2ab724e6e5

docker restart 0b2ab724e6e5

# run background
docker run -itd --name ubuntu-test ubuntu /bin/bash
# attach a shell
docker attach 0b2ab724e6e5
docker exec -it 0b2ab724e6e5 /bin/bash

# export import
docker export 0b2ab724e6e5 > ubuntu.tar
docker import http://example.com/exampleimage.tgz example/imagerepo
cat docker/ubuntu.tar | docker import - test/ubuntu:v1

# remove
docker rm -f 0b2ab724e6e5
```

ps docker 镜像加速配置(docker toolbox)

```Shell
#通过docker-machine进入docker环境
docker-machine ssh default

#修改boot2docker配置文件
sudo vi /var/lib/boot2docker/profile
#在--label provider=virtualbox的下一行添加
--registry-mirror https://docker.mirrors.ustc.edu.cn

#重启docker服务
sudo /etc/init.d/docker restart
#或者重启VM：
exit
docker-machine restart
```
