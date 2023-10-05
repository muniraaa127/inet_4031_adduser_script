#!/usr/bin/python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^#', line)
        fields=  line.strip().split(":")
        if match or len(fields) != 5:  #this condition is checking if the line starts with a # or if the number of fields after the split isnt 5 and if either condiotn is true then the code will continue to the next iteration
            continue
        username = fields[0]
        password = fields[1]

        gecos    = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',') #this line splits the fifth field by a comma and returns a list of spserated values and its splliting up the groups that are assigned to the user
        print("==> Creating account for %s..." % username,end='')
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)
    
        os.system(cmd) #this line executes the command stored in the cmd variable in which in this code is out creating a user command
        print("==> Setting the password for %s..." % username,end='')
    
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)
        os.system(cmd)
        for group in groups: #this for loop is looping around each group in the group list and then assigned the user to a group 
            if group != "-":    
                print("==> Assigning %s to the %s group..." % (username, group),end='')   
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                os.system(cmd)
if __name__ == '__main__':
    main()
