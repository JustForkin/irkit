import os

levelMin=2 
levelMax=10

os.system('v4l2-ctl --list-ctrls')

annotationStub='\'Focus=\''

index=0
for level in range(levelMin, levelMax):
    filename=str(index).zfill(5)+'_snap.jpeg'
    os.system('sudo fswebcam ./'+filename)
    #os.system('v4l2-ctl --list-ctrls')
    os.system('v4l2-ctl --set-ctrl sharpness='+str(level)) 
    os.system('convert '+filename+' -gravity North -background YellowGreen -splice 0x18 -annotate +0+2'+annotationStub+' '+filename)
    index=index+1
