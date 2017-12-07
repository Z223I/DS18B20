import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


device_folders = glob.glob(base_dir + '28*')
#device_files   = [ os.path.split(x)[1][3:] for x in device_folders ]

device_files = []
for xfolder in device_folders:
    print "--> " + xfolder + '/w1_slave'
    device_files.append( xfolder + '/w1_slave' )

print 
print "--------"
print


for therm in device_files:
    print therm


#device_files = []
#device_files.append("28-0417a0dfffff")
#device_files.append("28-0417a1107aff")
print "Number of thermometers: ", len(device_files)

device_file = base_dir + device_files[0] + "/w1_slave"
device_file = device_files[0]

print
print "lksdf"
print
print device_file



def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f
	
while True:
	print(read_temp())	
	time.sleep(1)
