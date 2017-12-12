import os

def openyumfile():
    os.system("sed -i s/python/python2.6/g /usr/bin/yum")
    print "replace yumfile sucess"

def yum():
    instpack = raw_input("strings like:  nfs-utils|rpcbind|rsyncnc|mysql|lrzsz  \n\n\n")
    rawpack = instpack.split("|")
    os.system("yum update")
    #print rawpack
    for i in rawpack:
        print "Now install" + i
        packname = "yum install %s -y" % (i)
        os.system(packname)

def menu():
    os.system("hostname -I")
    userpress = raw_input("Press 1 to yum install software:\nPress 2 to replace yumfile:\nPress exit to close\n")
    if userpress == "1":
        yum()
        menu()
    elif userpress == "2":
        openyumfile()
        menu()
    else:
        pass

menu()
