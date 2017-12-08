import os
import glob
import time

#*******************************************************************************
#
# Class Name:  DS18B20
#
#*******************************************************************************

class DS18B20:

    def __init__(self):
    	os.system('modprobe w1-gpio')
    	os.system('modprobe w1-therm')
	
    	base_dir = '/sys/bus/w1/devices/'
    	device_folders = glob.glob(base_dir + '28*')
	
    	self.device_files = []
    	for xfolder in device_folders:
            self.device_files.append( xfolder + '/w1_slave' )
	
	
    	for therm in self.device_files:
            print therm
	
    	print "Number of thermometers: ", len(self.device_files)
	

    def read_temp_raw(self, _device_file):
        f = open(_device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp(self, _device_file):
        lines = self.read_temp_raw(_device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f

    def Exec(self):	
        while True:
            for temperatureFile in self.device_files:
                print( self.read_temp( temperatureFile ) )

            print
	    time.sleep(1)
#
# End class DS18B20
#


therms = DS18B20()
therms.Exec()
