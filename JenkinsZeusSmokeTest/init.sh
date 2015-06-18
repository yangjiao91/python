#!/bin/bash
echo "init begin..."
#修改host为公网环境
sed -i "s/192.168.16.212 jsonfe.funshion.com/#192.168.16.212 jsonfe.funshion.com/g" /etc/hosts

#启动fitnesse
nap_count=$(ps -ef|grep fitnesse_standalone | grep -v 'grep' | wc -l)

if [ $nap_count -gt 0 ]
then 
  echo "fitnesse_standalone is runing"  
else 
  cd /home/fitnesse/
  nohup java -jar fitnesse_standalone.jar -p 8887 &
  str=$"/n"
  sstr=$(echo -e $str)
  echo "$sstr"
  echo "fitnesse_standalone restart..."
fi
echo "finished..."
