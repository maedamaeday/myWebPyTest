#!/usr/bin/env python3

#reference : Qiita article by @goodboy_max
# https://qiita.com/goodboy_max/items/833d482827bf0efab45a
#4th Jul. 2019

import cgi
import os
import subprocess

print('Content-Type: text/html charset=utf-8\n')

print('<!DOCTYPE html><html lang="ja"><head><title>run python script on browser</title></head><body>')

print ("<html><body>")

form = cgi.FieldStorage()
form_check = 0


print("<h1>output of python script with given arguments</h1>")
print("<hr>")
print("requests from "+os.environ["REMOTE_ADDR"]+"<br>")
print("request method : " + os.environ['REQUEST_METHOD']+"<br>")

if "arg1" not in form:
    print("<h2>ERROR !</h2>")
    print("arg1 is mandatory.")
else :
    print("<b>arg1 : </b>" + form["arg1"].value + "<br>")
    print("<b>arg2 : </b>" + (form["arg2"].value if "arg2" in form else "(not given)") + "<br>")
    print("<b>arg3 : </b>" + (form["arg3"].value if "arg3" in form else "(not given)") + "<br>")
    print("<b>arg4 : </b>" + form["arg4"].value + "<br>")

    print("<hr>")
    cmd = "python cgi-bin/my_script.py " + form["arg1"].value + " "\
        + (form["arg2"].value if "arg2" in form else "") + " "\
        + (form["arg3"].value if "arg3" in form else "") + " "\
        + form["arg4"].value
    print( "<i>" + cmd + "</i><br>" )
    print("output of the python script:<br>")
    proc = subprocess.run( cmd, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )    

    print( proc.stdout.decode('utf-8').replace("\n","<br>").replace(" ","&ensp;") )
#    while True:
#        for line in proc.stdout.readlines():
#            print( line.decode('utf-8').replace("\n","<br>").replace(" ","&emp;") )
#
#        if not line:
#            break

print ("</body></html>")
