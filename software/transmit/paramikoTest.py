import paramiko
import scp
import os
#import snap


#ssh=paramiko.SSHClient()
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('habeo.net',username='asine',password='habeocat999')



#def createSSHClient(server, port, user, password):
def createSSHClient(server,user,password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #client.connect(server, port, user, password)
    client.connect(server,username=user,password=password)
    return client

def getRecentfile(baseDir,file_paths):
    
    result = []
    for f in file_paths:
        g=baseDir+"/"+f
        stats = os.stat(g)
        modified_time = stats[8]
        file_time_tuple = modified_time,g
        result.append(file_time_tuple)
    return sorted(result)[-1][1]

def sendMostRecentFile(baseDir, remotepath,server,user,password):
    files=os.listdir(baseDir)
    latestFile=getRecentfile(baseDir,files)
    ssh = createSSHClient(server, user, password)
    scp = scp.SCPClient(ssh.get_transport())
    scp.put(latestFile,'pvos.org/ircam/latest.png')

remotepath='pvos.org/ircam/latest.png'
baseDir="./imgs"
server='habeo.net'
user='asine'
password='habeocat999'

sendMostRecentFile(baseDir, remotepath,server,user,password)

