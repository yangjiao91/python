#!/bin/bash
#发送邮件报告
python zeusSmokeTestReport.py
#host恢复
sleep 1
sed -i "s/#192.168.16.212 jsonfe.funshion.com/192.168.16.212 jsonfe.funshion.com/g" /etc/hosts
echo "execute finished..."
