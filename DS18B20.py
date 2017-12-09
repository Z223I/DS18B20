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
	
        self.device_names = []




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
            return temp_f




    def finish_dict(self):	
        #while True:
            NumberFiles = len( self.device_files )
            NumberNames = len( self.device_names )
            if NumberFiles == NumberNames :
                #print "match"
                for sensor in range( NumberFiles ):
                    name = self.device_names[sensor]
                    file = self.device_files[sensor]
                    self.sensor_dict[ name ] = file
                    #print name, self.read_temp( file )
                # end for
            else:
            	for temperatureFile in self.device_files:
                	print( self.read_temp( temperatureFile ) )
	
            	print
	    time.sleep(1)
	
    def NameDevice(self, name):
        # This must be done in the same order that the devices are listed.

        # TODO: Sanity check need to see if there are too many names.


        self.device_names.append( name )

    def create_dict(self):
        self.sensor_dict = dict.fromkeys( self.device_names, self.device_files )
        self.finish_dict()
        print "sensor_dict: ", str( self.sensor_dict )

    def get_current_temp(self, name):
        file = self.sensor_dict[ "Water" ]


        print "...", file



        return self.read_temp( file )

#
# End class DS18B20
#


therms = DS18B20()

therms.NameDevice( "Air" )
therms.NameDevice( "Water" )
therms.create_dict()

while True:
    temp = therms.get_current_temp( "Water" )
    print "Water temp: ", temp


#therms.execute()
