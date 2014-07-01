#!/usr/bin/python

# Errol Casey
# 
# Lookup timestamp of file and compare to timestamp in suffix
# and determine difference in times
#

import os.path, time
from datetime import datetime

# source directory 
sdir = "."
# file pattern
fp = "*"

import fnmatch
import os

def get_files_in_dir(dir,pattern):
    filelist = []
    for file in os.listdir(dir):
        if fnmatch.fnmatch(file,pattern ):
            filelist.append(file)
    return filelist

fl = get_files_in_dir(sdir,fp)
fl = sorted(fl)
for file in fl:
    tfile = file.strip()
    suffix = tfile[-3:]
    if suffix == ".gz":
        continue
    # DESTIME201406191106.txt.20140619182340
    backup_ts = tfile[-6:]
    #print file,backup_ts
    backup_ts = backup_ts[0:2] + ":" + backup_ts[2:4] + ":" + backup_ts[4:6]
    #print "last modified: %s" % time.ctime(os.path.getmtime(file))
    file_mt = time.ctime(os.path.getmtime(sdir + file))
    #print "last modified: %s " % file_mt
    # Tue Jun 24 10:20:20 2014
    mt_list = file_mt.split()
    if len(mt_list) > 3:
        mtime = mt_list[3]
        #mtime = mtime[:5]
    else:
        mtime = None
    #print file,backup_ts,file_mt,mtime
    FMT = '%H:%M:%S'
    try:
        tdelta = datetime.strptime(backup_ts, FMT) - datetime.strptime(mtime, FMT)
    except:
        continue
    #print file,backup_ts,mtime,tdelta
    print file,tdelta

