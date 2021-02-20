
一，每日记录机器的磁盘容量变化情况方案

二，每日获取磁盘容量信息
    到机器目录取结果文件：/tmp/result/result_(日期)。

    如/tmp/result/result_20210209，效果如下
#cat result/result_20210209
20210209
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        99G  8.4G   86G   9% /
devtmpfs        7.7G     0  7.7G   0% /dev
tmpfs           7.8G   24K  7.8G   1% /dev/shm
tmpfs           7.8G  250M  7.5G   4% /run
tmpfs           7.8G     0  7.8G   0% /sys/fs/cgroup
tmpfs           1.6G     0  1.6G   0% /run/user/0
/dev/vdb        197G  124G   64G  66% /data
capacity(MB)  dist_20210209                         capacity(MB)  dist_20210209
51041         /data/kafka-logs                      51052         /data/kafka-logs
38510         /data/apps                            38511         /data/apps
20288         /data/kafka-logs/cftlog71-0           20291         /data/kafka-logs/cftlog71-0
17233         /data/kafka-logs/cftlog101-0          17239         /data/kafka-logs/cftlog101-0
15948         /data/zookeeper-uat1                  15949         /data/zookeeper-uat1
12876         /data/apps/vb_base_eureka_server1     12877         /data/apps/vb_base_eureka_server1
12782         /data/zookeeper-uat1/data             12782         /data/zookeeper-uat1/data
10769         /data/apps/vb_base_eureka_server2     10769         /data/apps/vb_base_eureka_server2
10755         /data/apps/vb_base_eureka_server3     10755         /data/apps/vb_base_eureka_server3
7552          /data/kafka-logs/cftlog91-0           7554          /data/kafka-logs/cftlog91-0
4111          /data/apps/vb_base_eureka_server      4111          /data/apps/vb_base_eureka_server
3104          /data/zookeeper-uat1/log              3104          /data/zookeeper-uat1/log
2084          /data/icafe                           2085          /data/icafe
2010          /data/cftlogagent                     2010          /data/cftlogagent
1985          /data/cftlogagent/log                 1985          /data/cftlogagent/log
1025          /data/kafka-logs/stat_data-0          1025          /data/kafka-logs/stat_data-0
867           /data/kafka-logs/vb_um_application-0  867           /data/kafka-logs/vb_um_application-0
759           /data/zookeeper-uat2                  759           /data/zookeeper-uat2
646           /data/zookeeper-uat3                  646           /data/zookeeper-uat3
536           /data/icafe/fit_op_tool               536           /data/icafe/fit_op_tool



三， 实施
    将采集脚本countDisk.sh上传至服务器/data目录，在机器上加入crontab每日处理脚本：
    #count Disk capacty 每天凌晨1点执行一次。
    * 1 * * * cd /data/; sh  countDisk.sh > /dev/null 2>&1