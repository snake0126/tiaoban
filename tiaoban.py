import xlrd
import os
import pexpect


data = xlrd.open_workbook('/tmp/qsonline1117.xlsx')
table = data.sheets()[0]
Name = table.col_values(2)
Cpuip = table.col_values(4)
utfList = []
utfip = []
Namenum = range(1,len(Name))

for Namelist in range(1,len(Name)):
    UtfName = Name[Namelist].encode('UTF-8')
    utfList.append(UtfName)

for CpuList in range(1,len(Cpuip)):
    if Cpuip[CpuList].encode('UTF-8') == '':
        utfip.insert(CpuList,'None')
    else:
        Utfip = Cpuip[CpuList].encode('UTF-8')
        utfip.append(Utfip)

for num in range(0,len(Name)-1):
    print "%d   %s/%s" % (num+1,utfList[num],utfip[num])


Userinput = input("\n\n\nPress Num of your Chosen:\n\n\n")
if Userinput == '':
    print("Input Error is empty")
    pass
elif Userinput in Namenum:
    print"\n\n\n%s  %d   %s/%s" % ("Now connect to", Userinput, utfList[Userinput-1],utfip[Userinput-1])
    #os.system('sshpass -pSGH71746j51234 ssh -p56000 root@'+utfip[Userinput-1]+' cd/home')
    #SSH = os.system('ssh -p56000 root@'+utfip[Userinput-1])
    SSH = "ssh -p56000 root@%s" % (utfip[Userinput-1])
    print SSH
    child = pexpect.spawn(SSH)
    index = child.expect(['password:', 'continue connecting (yes/no)?', pexpect.EOF, pexpect.TIMEOUT])
    print index
    if index == 0:
        child.sendline("SGH71746j51234")
        child.interact()
    elif index == 1:
        child.sendline('yes')
        child.expect(['password:'])
        child.sendline("SGH71746j51234")
        child.interact()
    elif index == 2:
        print "error"
        child.close()
    elif index == 3:
        print "time out"
else:
    print("Press Error Number")
