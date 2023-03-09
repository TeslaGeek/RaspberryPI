import csv
import threading
from datetime import datetime
from time import sleep
import board
import busio
import adafruit_adxl34x


class AccRecorder():
	def __init__(self):
		
		self.open = True
		self.file_name = 'default name'
		self.i2c = board.I2C()
		self.acc = adafruit_adxl34x.ADXL345(self.i2c)
		self.acc_data = [0 for i in range(3)]
		self.data_dict = {}

	
	def callback(self,indata,status):
		if status:
			print(status, file =sys.stderr)
		
		self.q.put(indata.copy())
		
	def record(self):	
		'''collect data and assign to class variable'''
		i=0;
		for d in self.acc.acceleration:
			self.acc_data[i] = d
			i = i+1
		self.data_dict['accelerometer'] = (datetime.now(), self.acc_data[0], self.acc_data[1],self.acc_data[2])
		
		''' log the data into csv files'''
		for file, data in self.data_dict.items():
			with open(self.file_name, 'a+', newline ='') as f:
				writer = csv.writer(f)
				writer.writerow(data)
		
		
	# def log_data(self):
		# ''' log the data into csv files'''
		# for file, data in self.data_dict.items():
			# with open(self.file_name, 'a+', newline ='') as f:
				# writer = csv.writer(f)
				# writer.writerow(data)
				
	def stop(self):
		self.open = False
	
	def start(self,file_name,file_dir):
		self.open = True
		self.file_name ='{}/{}.csv'.format(file_dir,file_name)
		
		acc_thread = threading.Thread(target = self.record)
		acc_thread.start()
		acc_thread.join()
				
# def main():
	# while True:
		# logger = AccLogger()
		# logger.record()
		# logger.log_data()
		# #logger.print_data()
		# sleep(5)
		
		
# main()
