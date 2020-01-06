#!/bin/bash

#保留文件数

ReservedNum=20

#当前脚本所在目录
cd a/video
RootDir=$(cd `dirname $0`; pwd)

#显示文件数， *.*可以改为指定文件类型

FileNum=$(ls -l *.* | grep ^- | wc -l)

while(( $FileNum > $ReservedNum ))

do

    #取最旧的文件，*.*可以改为指定文件类型

    OldFile=$(ls -rt *.* | head -1)

    echo "Delete File:"$RootDir'/'$OldFile

    rm -f $RootDir'/'$OldFile

    let "FileNum--"

done