#!/usr/bin/env bash


build_img(){
   CURRENT_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
   env=$1
   cd $CURRENT_DIR/.. && \
   if test ${env} = "dev"
   then
      python bootstrap.py
   elif test ${env} = "test"
   then
      nohup python bootstrap.py ${env}&
   elif test ${env} = "prod"
   then
      nohup python bootstrap.py ${env}&
   else
      echo '参数错误!'
   fi
}

ENV=$1
case ${ENV} in
    "dev")
        build_img dev
        ;;
    "test")
        build_img test
        ;;
    "prod")
        build_img prod
        ;;
    *)
        build_img dev
        ;;
esac

