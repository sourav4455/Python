# This function copies the overwrite directory if does not exists and if exists then remove the old one copy it again.

#!/bin/python

import os
import shutil

file_path = "/home/shourabh/Desktop/Current_Work/puppet_new/hieradata/overwrite"
dest_path = "/home/shourabh/Desktop/Current_Work/puppet/hieradata/overwrite"

def copy_overwrite(file_path,dest_path):
    if os.path.exists(file_path):
            if os.path.exists(dest_path):
                    shutil.rmtree(dest_path)
         	    shutil.copytree(file_path,dest_path)
      	    else:
         	    shutil.copytree(file_path,dest_path)

copy_overwrite(file_path,dest_path)

