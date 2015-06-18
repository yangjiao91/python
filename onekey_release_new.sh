#!/bin/bash

war_filepath=$1

tomcat_home=$2
context_filename=user-service.xml

#web_home=/home/users/wangjw/user-service/web_root_8080/
web_home=$3


if [[ ! -f "$war_filepath" ]]
then
	echo -e "\033[41m war_filepath:$war_filepath is not exist or not a war file \033[0m"
	exit 1
fi

version=$(cat ${tomcat_home}conf/Catalina/localhost/${context_filename}|awk -F "/" '{print $(NF-2)}')

echo -e "current version: \033[33m $version \033[0m"

version_1=$(echo $version|cut -d . -f1)
version_2=$(echo $version|cut -d . -f2)
version_3=$(echo $version|cut -d . -f3)

n_version_1=$version_1
n_version_2=$version_2
n_version_3=$((version_3+1))


if [ $n_version_3 -eq 50 ]
then
	n_version_3=0
	n_version_2=$((n_version_2+1))

	if [ $n_version_2 -eq 10 ]
	then
		n_version_2=0
		n_version_1=$((n_version_1+1))
	fi
fi

new_version=${n_version_1}.${n_version_2}.${n_version_3}
echo -e "new_version: \033[33m $new_version \033[0m"

version_home=${web_home}${new_version}/
web_root_home=${version_home}web/
mkdir $version_home
if [ $? -ne 0 ]
then
	echo -e "\033[41m [ERRO] mkdir $version_home failed! \033[0m"
	exit 1
fi

mkdir $web_root_home
if [ $? -ne 0 ]
then
	echo -e "\033[41m [ERRO] mkdir $web_root_home failed! \033[0m"
	exit 1
fi

echo -e "[INFO] \033[33m mkdir new version web directory: $web_root_home success \033[0m"

unzip -q $war_filepath -d $web_root_home
echo -e "[INFO] \033[33m unzip $war_filepath -d $web_root_home success \033[0m"

bash $4 $web_root_home
echo -e "[INFO] \033[33m replace_conf success \033[0m"

echo -e "\n\n=============================================================================\n\n"

bash ${tomcat_home}bin/shutdown.sh
sleep 3
pid=$(ps aux|grep "$tomcat_home"|grep java|grep -v grep|head -n 1|awk '{print $2}')
while test "$pid" != ""
do
	sleep 1
	pid=$(ps aux|grep "$tomcat_home"|grep java|grep -v grep|head -n 1|awk '{print $2}')
done

echo -e "\n\n=============================================================================\n\n"

echo -e "[INFO] \033[33m tomcat is stopped \033[0m"

replace_version_cmd="sed -i 's/$version_1\.$version_2\.$version_3/$new_version/g' ${tomcat_home}conf/Catalina/localhost/${context_filename}"

eval "$replace_version_cmd"

echo -e "\n\n=============================================================================\n\n"

bash ${tomcat_home}bin/startup.sh
sleep 3

tail -n 150 ${tomcat_home}logs/catalina.out

echo -e "\n\n=============================================================================\n\n"

pid=$(ps aux|grep "$tomcat_home"|grep java|grep -v grep|head -n 1|awk '{print $2}')

echo -e "$war_filepath is deployed,pid:\033[33m $pid \033[0m"


