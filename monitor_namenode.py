## This program will monitor the namenodes and check the state of the current namenode.

#!/usr/bin/python
# Author: Shourabh Singh
# Date: 30.09.2017
# Purpose: Monitoring of NameNode

import os
import sys

srv_state=os.popen('hdfs haadmin -ns gbispindev-lnn -getServiceState nn1 2>/dev/null').read()
state_file="/home/hdfs/state"

if (not os.path.exists(state_file)):
   if srv_state == "standby":
      print "NameNode current state is ",srv_state
      f = open(state_file,"w")
      f.write(srv_state)
      f.close()
   else:
      f = open(state_file,"w")
      f.write(srv_state)
      f.close()
else:
   var2=os.popen('cat /home/hdfs/state').read()
   if srv_state != var2:
      print "Namenode state is changed from %s to %s" % (var2,srv_state)
#      print "Namenode state is changed to ", srv_state, "from", open('/home/hdfs/state','r').read()
      f = open(state_file,"w")
      f.write(srv_state)
      f.close()
   else:
      print "Namenode state is still %s" % (srv_state)


#END
