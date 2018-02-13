## This program will monitor the state of the namenode always.

#!/usr/bin/python
# Author: Shourabh Singh
# Date: 30.09.2017
# Purpose: Monitoring of NameNode

import os
import subprocess
import sys

srv_state=os.popen('hdfs haadmin -ns gbispindev-lnn -getServiceState nn1 2>/dev/null')
state_file="/home/hdfs/state"

#srv_state="standby"
#state_file="/root/gt"

if (not os.path.exists(state_file)):
   if srv_state.read() == "standby":
      print "NameNode current state is ",srv_state
      with open("/home/hdfs/state","w") as stdout:
        subprocess.Popen('hdfs haadmin -ns gbispindev-lnn -getServiceState nn1 2>/dev/null', cwd = '/home/hdfs', shell=True, stdout=stdout, stderr=stdout)
   else:
       with open("/home/hdfs/state","w") as stdout:
         subprocess.Popen('hdfs haadmin -ns gbispindev-lnn -getServiceState nn1 2>/dev/null', cwd = '/home/hdfs', shell=True, stdout=stdout, stderr=stdout)

else:
   var2=os.popen('cat /home/hdfs/state')
   if srv_state.read() != var2.read():
      print "Namenode state is changed to ", srv_state, "from", open('/home/hdfs/state','r').read()
      with open("/home/hdfs/state","w") as stdout:
         subprocess.Popen('hdfs haadmin -ns gbispindev-lnn -getServiceState nn1 2>/dev/null', cwd = '/home/hdfs', shell=True, stdout=stdout, stderr=stdout)
   else:
      print "Namenode state is still %s" % (srv_state)

#END
