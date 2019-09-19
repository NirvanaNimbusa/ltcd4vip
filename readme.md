# Ltcd4vip

[website](http://leetcode.liangjiateng.cn/leetcode/algorithm)

## Deploy

Make sure your server has installed docker.

### 1. Build a Image

In **bin** directory:

`./docker_build.sh [option]` (test, prod)

**Usage:**

`./docker_build.sh test`

### 2. Start the web server

```
docker attach ltcd4vip:lastest
./bin/run.sh test (test, prod)
```
