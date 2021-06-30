#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f=cgi.FieldStorage()
inp=f.getvalue("inp")
if  ("launch" in inp) and ("pod" in inp):
	np=f.getvalue("np")
	im=f.getvalue("im")
	o=subprocess.getoutput("kubectl run "+np+" --image "+im+" --kubeconfig admin.conf")
	print(o)
elif ("create" in inp) and ("deployment" in inp):
	nd=f.getvalue("nd")
	im=f.getvalue("im")
	o=subprocess.getoutput("kubectl create deployment "+nd+" --image "+im+" --kubeconfig admin.conf")
	print(o)
elif ("view" in inp) and ("deployment" in inp):
	
	o=subprocess.getoutput("kubectl get deployment --kubeconfig admin.conf")
	print(o)
elif ("scale" in inp) and ("deployment" in inp):
	nd=f.getvalue("nd")
	r=f.getvalue("r")
	o=subprocess.getoutput("kubectl scale deployment "+nd+" --replicas="+r+" --kubeconfig admin.conf")
	print(o)
elif ("expose" in inp) and ("deployment" in inp):
	nd=f.getvalue("nd")
	p=f.getvalue("p")
	o=subprocess.getoutput("kubectl expose deployment "+nd+" --port="+p+" --type=NodePort --kubeconfig admin.conf")
	print(o)
elif ("delete" in inp) and ("deployment" in inp):
	nd=f.getvalue("nd")
	o=subprocess.getoutput("kubectl delete deployment "+nd+" --kubeconfig admin.conf")
	print(o)
else:
	print("not recognized")
