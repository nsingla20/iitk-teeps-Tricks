#checks online pcs in CSE and CC
import platform
import subprocess
import threading

def ping(server,x,host,ans):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    loc=server+str(x)+host
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param,'1', loc]

    if subprocess.call(command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL) == 0:
        ans.append(x)

def Th100(server,x,host):
    ans=[]
    l=[]
    for i in range(x*100,(x+1)*100):
        l.append(threading.Thread(target=ping,args=(server,i,host,ans)))

    for t in l:
        t.start()
    for t in l:
        t.join()
    ans.sort()
    return ans

def go(server,host,i,j):  #x=0,cse ; x=1,cc ; from i to j;
    print("\nOnline "+server+" pcs are:")
    ans=[]
    for e in range(i,j+1):
        ans=ans+Th100(server,e,host)
    
    for e in ans:
        print(server+str(e)+", ",end="")
    print("")

go('csews','.cse.iitk.ac.in',0,3)
go('ccpc','.cc.iitk.ac.in',0,3)
go('escpc','.cc.iitk.ac.in',0,3)
