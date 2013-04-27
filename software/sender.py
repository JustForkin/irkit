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
    sortedList=sorted(result)
    imFileA=sortedList[len(sortedList)-1][1]
    imFileB=sortedList[len(sortedList)-2][1]
    print imFileA, imFileB
    return [imFileA,imFileB]

def sendMostRecentFile(baseDir, remotepath,server,user,password):
    files=os.listdir(baseDir)
    #print files
    latestFiles=getRecentfile(baseDir,files)
    #print latestFile
    ssh = createSSHClient(server=server, user=user, password=password)
    #print ssh
    scp1 = scp.SCPClient(ssh.get_transport())
    print "copying images remotely ..."
    #remoteFilePath0='pvos.org/ircam/imgs/'+latestFiles[0].split('/')[2]
    #remoteFilePath1='pvos.org/ircam/imgs/'+latestFiles[1].split('/')[2]
    remoteFilePath0='pvos.org/co2cam/imgs/'+latestFiles[0].split('/')[2]
    remoteFilePath1='pvos.org/co2cam/imgs/'+latestFiles[1].split('/')[2]
    scp1.put(latestFiles[0],remoteFilePath0)
    scp1.put(latestFiles[1],remoteFilePath1)
    #places images in "latest" in order for web page to display them side-by-side:    
    print "updating remote webpage ..."
    scp1.put(latestFiles[0],'pvos.org/ircam/latestA.png')
    scp1.put(latestFiles[1],'pvos.org/ircam/latestB.png')
    scp1.put(latestFiles[0],'pvos.org/co2cam/latestA.png')
    scp1.put(latestFiles[1],'pvos.org/co2cam/latestB.png')


"""
remotepath='pvos.org/ircam/latest.png'
baseDir="./imgs"
server='habeo.net'
user='asine'
password='habeocat999'

sendMostRecentFile(baseDir,remotepath,server,user,password)
"""

"""
remotepath='pvos.org/ircam/latest.png'
baseDir="./imgs"
server='habeo.net'
user='asine'
password='habeocat999'
files=os.listdir(baseDir)
print files
latestFile=getRecentfile(baseDir,files)
print latestFile
ssh = createSSHClient(server=server, user=user, password=password)
print ssh
scp = scp.SCPClient(ssh.get_transport())
scp.put(latestFile,'pvos.org/ircam/latest.png')
"""

#sendMostRecentFile(baseDir, remotepath,server,user,password)

