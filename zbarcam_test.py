import os
p=os.popen('zbarcam --nodisplay','r')
print 'scanning'
while True:
        barcode = p.readline()
        print 'Got barcode:', barcode
        #The returned code is made up of 2 parts, the type : data
        type = barcode.split(':')[0]
        print type +' '
        code = barcode.split(':')[1]
        print code +' '+str(len(code))
        #You need to remove the return extra character from the string!
        code =code [0:-1]
        #os.system('chromium http://www.goodreads.com/search/search?q=%s'%isbn)
        #This might launch Quake3.
        if (code=='quake3'):
                os.system('/home/pi/quake3/./ioquake3.arm')
        elif (code=='minecraft'):
                os.system('startx /home/pi/mcpi/./minecraft-pi')
        else:
                print ('What is: ' + code + '?')
                os.system('espeak "Sorry I dont recognise that!"')
