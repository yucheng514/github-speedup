#!/usr/bin/env sh

# 当发生错误时中止脚本
set -e


python3 ./src/speedup.py

# /usr/bin/dscacheutil -flushcache
dscacheutil -flushcache
killall -HUP mDNSResponder

cd -