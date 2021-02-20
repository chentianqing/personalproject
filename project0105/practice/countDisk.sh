#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
BASEDIR=$( (
  cd "${BASEDIR}"
  pwd
))


function main(){
    mkdir -p /tmp/result/
    result_dir=/tmp/result/
    cd $result_dir;
    datetime=`date +%Y%m%d`
    echo $datetime > $result_dir/result_$datetime
    df -h >> $result_dir/result_$datetime

    #文件磁盘容量前20名
    du -hm /data/* --max-depth=1 |sort -rn|head -n 20 |sed "1i capacity(MB) dist_$datetime"> $result_dir/current

    #对比前一天的增长率
    if [ ! -f $result_dir/before ];then
        echo "capacity(MB) dist_$datetime"> $result_dir/before;
        paste before current |column -t > $result_dir/compare
    else
        paste before current |column -t > $result_dir/compare

     fi


    #将比较结果加入到报告文件中
    cat $result_dir/compare >> $result_dir/result_$datetime

    #重置before文件，用于下一次比较。
    cat $result_dir/current > $result_dir/before

}

main