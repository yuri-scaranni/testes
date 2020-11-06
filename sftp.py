import pysftp
import sys

myHostname = "ec2-18-229-162-55.sa-east-1.compute.amazonaws.com"
myUsername = "ec2-user"
myPassword = "/home/ec2-user/work_space/testes/scaranni_key.pem"

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

file_path = '/home/ec2-user/work_space/texto.txt'
remote_dir = '/home/ec2-user/downloads'

#python3 sftp.py '/home/ec2-user/work_space/texto.txt' '/home/ec2-user/downloads'

with pysftp.Connection(host=myHostname, username=myUsername, private_key=myPassword, cnopts=cnopts) as sftp:
    print("Connection succesfully stablished ... ")
    sftp.put(file_path, remote_dir)
    sftp.close()
