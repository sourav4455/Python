## This programs scans the SAN LUNS coming from storage and then creates PV/VG/LV and then filesystem. 
## This also make the entries in multipath.conf.


#!/usr/bin/python
#Purpose: Working with file argument
# LUNID   ALIAS   Mount_Point
import sys,getopt,string,subprocess

def mount_vol(data):
    for i in data:
        file2 = string.split(i)
        mount_cmd = "mount "+file2[2]
        cmd1 = mount_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]

def dir_create(data):
    for i in data:
        file2 = string.split(i)
        mk_cmd = "mkdir "+file2[2]+" -p"
        cmd1 = mk_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]
    mount_vol(data)

def fstab_entry(data):
    fs_file = "/etc/fstab"
    f3 = open(fs_file,"a")
    for i in data:
        file2 = string.split(i)
        fs_ent = "/dev/"+"vg_"+file2[1]+"/lv_"+file2[1] , file2[2] , "ext4  defaults 0 0 \n"
        fs_ent1 = string.join(fs_ent)
        f3.writelines(fs_ent1)
    f3.close()       
    dir_create(data)

def filesystem_create(data):
    for i in data:
        file2 = string.split(i)
        mkfs_cmd = "mkfs.ext4 " + "/dev/"+"vg_"+file2[1]+"/lv_"+file2[1]
        cmd1 = mkfs_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]
    fstab_entry(data)

def lv_create(data):
    for i in data:
        file2 = string.split(i)
        lv_cmd = "lvcreate -l 100%vg -n" + " lv_"+file2[1] + " vg_"+file2[1]
        cmd1 = lv_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]
    filesystem_create(data)

def vg_create(data):
    for i in data:
        file2 = string.split(i)
        vg_cmd = "vgcreate " + "vg_"+file2[1] + " /dev/mapper/"+file2[1]
        cmd1 = vg_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]
    lv_create(data)

def pv_create(data):
    for i in data:
        file2 = string.split(i)
        pv_cmd = "/sbin/pvcreate " + "/dev/mapper/"+file2[1]
        cmd1 = pv_cmd.split()
        p = subprocess.Popen(cmd1, shell=False, stderr=subprocess.PIPE)
        print p.communicate()[1]
    vg_create(data)

def multipath(inputfile):
    var_multipath = "/etc/multipath.conf"
    f1 = open(inputfile,"r")
    f2 = open(var_multipath,"a")
    data = f1.readlines()


    for i in data:

        file2 = string.split(i)
        print   "multipath { \n\t\t", "wwid\t" , file2[0]  , "\n\t\t alias\t" , file2[1] ,"\n } \n"
    user_input = raw_input ("Would you like to append the multipath with above alias (yes/no)")

    if user_input == "yes":
        for i in data:
            file2 = string.split(i)
            file3 = "multipath { \n\t\t", "wwid\t" , file2[0]  , "\n\t\t alias\t" , file2[1] ,"\n } \n"
            f2.writelines(file3)
    else:
        print "Please check your input file syntext and try again"
        sys.exit()
    f1.close()
    f2.close()
    print "Restarting multipath"
    service_cmd = "service multipathd reload"
    p = subprocess.Popen(service_cmd, shell=True, stderr=subprocess.PIPE)
    print p.communicate()[1]
    pv_create(data)
       
def main(argv):

    inputfile = ''
        
    try:    
        opts, args = getopt.getopt(argv,"hf:",["ifile="])

    except getopt.GetoptError:

        print "you need to provide the -f with filename/path"
         sys.exit()

    for opt,arg in opts:
           
        if opt == "-h":
             print "you need to provide the -f with filename/path that you want to print"
            sys.exit()
        elif opt in ("-f" , "--ifile"):
             inputfile = arg
    multipath(inputfile)
   
   
if len(sys.argv) == 3:
    main(sys.argv[1:])
else:
    print "You must provide the argumnet - multipath.py -f $file_name"

