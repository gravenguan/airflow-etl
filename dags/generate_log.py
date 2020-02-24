import os
import subprocess

# def execute_local(args):
#     print('running command : %s' % (' '.join(args)))
#     process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     output = process.communicate()
#     print('STDOUT:{}'.format(output))
from common.s3_utils import copy_to_s3
from common.system_utils import execute_local, del_local_file

###############################################################
#  constants and configs
###############################################################
location = 's3://heran-bucket/access-log/'


def generate_data():
    path="C:/Users/grave/Dropbox/study/airflow-etl/Fake-Apache-Log-Generator-master/"
    os.chdir(path)

    print(os.getcwd())

    cmd=["python","apache-fake-log-gen.py","-n", "1000", "-o", "GZ"]
    execute_local(cmd)

    #list file in current dir
    files=os.listdir(os.curdir)

    list=[path + i for i in files if 'access_log' in i]
    print(list)

    return list

def run(**kwargs):
    date=str(kwargs['ds'])
    log_files=generate_data()
    copy_to_s3(location+date+'/',log_files)
    del_local_file(log_files)

run(ds=2018)

