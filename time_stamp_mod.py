# Script to update the modified date of a MOD file based on the MOI file information

import struct
import os
import time
import datetime
import glob

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Get list of files
for file in glob.glob("*.MOD"):
        print("Processing: {}...".format(file))
        fileName, _ = os.path.splitext(file)

	# Check if the corresponding moi file exists
        if os.path.exists("{}.MOI".format(fileName)):
		print("{}Found MOI file{}".format(bcolors.OKGREEN, bcolors.ENDC))

	        f = open("{}.MOI".format(fileName), "rb")
		b = f.read()
        	f.close()
		(year,) = struct.unpack(">H", b[6:8])
		(month,) = struct.unpack("B", b[8])
		(day,) = struct.unpack("B", b[9])
		(hour,) = struct.unpack("B", b[10])
		(minute,) = struct.unpack("B", b[11])
		(second,) = struct.unpack(">H", b[12:14])
        	print("{}/{}/{}: {}:{},{}".format(year, month, day, hour, minute, second))
		date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second/1000)
		modTime = time.mktime(date.timetuple())
		os.utime("{}.MOD".format(fileName), (modTime, modTime))
		print("{}Done{}".format(bcolors.OKGREEN, bcolors.ENDC))
	else:
		print("{}{}: MOI file not found!{}".format(bcolors.FAIL, fileName, bcolors.ENDC))
        
	print("")  # print blank line
