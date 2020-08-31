#!/bin/bash
# ==================INSTALL ON UBUNTU=======================
# https://phoenixnap.com/kb/how-to-install-docker-on-ubuntu-18-04
# https://docs.docker.com/engine/install/linux-postinstall/

sudo apt-get update

sudo apt-get remove docker docker-engine docker.io

sudo apt install docker.io

sudo systemctl start docker

sudo systemctl enable docker

sudo usermod -aG docker $USER

#restart machine

# docker-compose 
# https://docs.docker.com/compose/install/
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# ================= INSTALL ON CENTOS/RHEL
# install docker
yum install -y http://mirror.centos.org/centos/7/extras/x86_64/Packages/container-selinux-2.68-1.el7.noarch.rpm

yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

yum install -y docker-ce

usermod -a -G docker ec2-user

systemctl enable docker

systemctl start docker

docker -v 

docker run -d --name nginx --rm -p 80:80 nginx

curl localhost

docker stop nginx && docker rmi nginx

# install compose
curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-Linux-x86_64" -o /usr/bin/docker-compose

chmod +x /usr/bin/docker-compose

docker-compose -v
