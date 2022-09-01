import boto3
import os

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = ''
secret_key = ''

def batch(ID, OS, ServerID):

    Centos7 = '#!/bin/bash \nrpm -Uvh http://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm \nyum -y install zabbix-agent zabbix-sender \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.201.149\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.201.149:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Centos6 = '#!/bin/bash \nrpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/6/x86_64/zabbix-release-5.0-1.el6.noarch.rpm \nyum -y install zabbix-agent zabbix-sender \nsed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"######Zabbix Server IP#######\" \necho \"#############################\" \necho \"Server=175.45.201.149\" >> /etc/zabbix/zabbix_agentd.conf \necho \"ServerActive=175.45.201.149:10051\" >> /etc/zabbix/zabbix_agentd.conf \necho \"#############################\" \necho \"####### HOSTMetadata #######\" \necho \"#############################\" \necho \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \ncat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsystemctl start zabbix-agent \nsystemctl enable zabbix-agent \nsystemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu2004 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+focal_all.deb \nsudo dpkg -i zabbix-release_5.0-1+focal_all.deb \nsudo apt update \nsudo apt install zabbix-agent -y \nsudo sed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo chmod 666 /etc/zabbix/zabbix_agentd.conf  \nsudo sed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"######Zabbix Server IP#######\" \nsudo echo \"#############################\" \nsudo echo \"Server=175.45.201.149\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"ServerActive=175.45.201.149:10051\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"####### HOSTMetadata #######\" \nsudo echo \"#############################\" \nsudo echo \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsudo sed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsudo chmod 644 /etc/zabbix/zabbix_agentd.conf \nsudo systemctl start zabbix-agent \nsudo systemctl restart zabbix-agent \nsudo systemctl enable zabbix-agent \nsudo systemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu1804 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+bionic_all.deb \nsudo dpkg -i zabbix-release_5.0-1+bionic_all.deb \nsudo apt update \nsudo apt install zabbix-agent -y \nsudo sed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo chmod 666 /etc/zabbix/zabbix_agentd.conf  \nsudo sed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"######Zabbix Server IP#######\" \nsudo echo \"#############################\" \nsudo echo \"Server=175.45.201.149\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"ServerActive=175.45.201.149:10051\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"####### HOSTMetadata #######\" \nsudo echo \"#############################\" \nsudo echo \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsudo sed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsudo chmod 644 /etc/zabbix/zabbix_agentd.conf \nsudo systemctl start zabbix-agent \nsudo systemctl restart zabbix-agent \nsudo systemctl enable zabbix-agent \nsudo systemctl status zabbix-agent'%(ID,ServerID)
    Ubuntu1604 = '#!/bin/bash \nwget https://repo.zabbix.com/zabbix/5.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_5.0-1+xenial_all.deb \nsudo dpkg -i zabbix-release_5.0-1+xenial_all.deb \nsudo apt update \nsudo apt install zabbix-agent -y \nsudo sed -i \'s/Server=127.0.0.1/#Server=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo chmod 666 /etc/zabbix/zabbix_agentd.conf  \nsudo sed -i \'s/ServerActive=127.0.0.1/#ServerActive=127.0.0.1/g\' /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"######Zabbix Server IP#######\" \nsudo echo \"#############################\" \nsudo echo \"Server=175.45.201.149\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"ServerActive=175.45.201.149:10051\" >> /etc/zabbix/zabbix_agentd.conf \nsudo echo \"#############################\" \nsudo echo \"####### HOSTMetadata #######\" \nsudo echo \"#############################\" \nsudo echo \"HostMetadata=%s\" >> /etc/zabbix/zabbix_agentd.conf \nsudo sed -i \'s/Hostname=Zabbix server/Hostname=\'\"%s\"\'/g\' /etc/zabbix/zabbix_agentd.conf \ncat /etc/zabbix/zabbix_agentd.conf | grep \'Server\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'Hostname=\' \nsudo cat /etc/zabbix/zabbix_agentd.conf | grep \'HostMetadata=\' \nsudo chmod 644 /etc/zabbix/zabbix_agentd.conf \nsudo systemctl start zabbix-agent \nsudo systemctl restart zabbix-agent \nsudo systemctl enable zabbix-agent \nsudo systemctl status zabbix-agent'%(ID,ServerID)
    
    if OS == 'Centos7':
        OS = Centos7
    elif OS == 'Centos6':
        OS = Centos6
    elif OS == 'Ubuntu20.04':
        OS = Ubuntu2004   
    elif OS == 'Ubuntu18.04':
        OS = Ubuntu1804  
    elif OS == 'Ubuntu16.04':
        OS = Ubuntu1604                

    f = open('%s.bat'%ServerID, 'w')
    f.write(OS)
    f.close()                                                           #local에 batch 파일 저장
                                              #NBP S3 Upload Code
    s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key)
    bucket_name = 'oidc'
    object_name = '%s.bat'%ServerID                                       #파일 이름(파일명 : ID)
    #local_file_path = 'C:/Users/user/Desktop/NBP_back/cloud/%s.bat'%ServerID      #local 위치 
    local_file_path = '/root/cloud/%s.bat'%ServerID                             #서버상 위치
    
    s3.upload_file(local_file_path, bucket_name, object_name, ExtraArgs={'ACL':'public-read'})
    
    if os.path.exists(local_file_path):                              #local에 저장한 file 삭제
        os.remove(local_file_path)

    #서버에서 agent 설치하는 법(metadata는 id로 설정되있음)
    #1. 서버에서 curl -O(centos), wget(ubuntu) 's3 url' 을 입력하여 bat 파일 다운로드
    #2. chmod 755 'bat file명' -->bat file 권한을 access 할 수 있게 변경
    #3. ./'file명'으로 실행(agent 설치&설정)
