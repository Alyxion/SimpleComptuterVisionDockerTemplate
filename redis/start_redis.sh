#!/bin/sh
echo "Starting Redis"
rm -r ./data/* || true
exec redis-server /usr/local/etc/redis/redis.conf