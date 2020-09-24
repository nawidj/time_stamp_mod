# Script to update the modified date of a MOD file based on the MOI file information
import struct
import os
import time
import datetime
import glob

# Get list of files
for file in glob.glob("*.MOI"):
        print("Processing: {}".format(file))

	fileName, _ = os.path.splitext(file)        
	f = open(file, "rb")
	b = f.read()
	f.close()
	(year,) = struct.unpack(">H", b[6:8])
	(month,) = struct.unpack("B", b[8])
	(day,) = struct.unpack("B", b[9])
	(hour,) = struct.unpack("B", b[10])
	(minute,) = struct.unpack("B", b[11])
	(second,) = struct.unpack(">H", b[12:14])

	date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second/1000)
	modTime = time.mktime(date.timetuple())

	os.utime("{}.MOD".format(fileName), (modTime, modTime))
