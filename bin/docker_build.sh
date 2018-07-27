#!/usr/bin/env bash

echo "==============开始构建docker镜像================="
docker rm -f ltcd4vip_test
docker rm -f ltcd4vip
docker rmi -f ltcd4vip:lastest

CURRENT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd ${CURRENT_DIR}/..

docker build -t ltcd4vip:lastest .

echo "==============镜像ltcd4vip:lastest构建完成!================="

ENV=$1
echo "==============开始启动docker容器================="
case ${ENV} in
    "test")
        docker run --name ltcd4vip_test -p 12580:12580 -dit ltcd4vip:lastest /bin/bash
        echo "==============test环境容器启动成功================="
        ;;
    "prod")
        mkdir /root/repos/log/ltcd4vip
        docker run --name ltcd4vip -p 12306:12306 -v /root/repos/log/ltcd4vip:/repos/log/ltcd4vip -dit ltcd4vip:lastest /bin/bash
        echo "==============prod环境容器启动成功================="
        ;;
    *)
        echo "参数错误：输入test或者prod"
        ;;
esac
