import threading
from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
import datetime
from time import sleep

class VideoRecorder():
	def __init__(self):
		
		self.file_name = 'default name'
		self.picam2 = Picamera2()
		self.video_config = self.picam2.create_video_configuration(main={"size": (1920,1080)}, lores={"size": (640,480)}, display="lores")
		self.picam2.configure(self.video_config)
		self.encoder = JpegEncoder(q=70)
		
	def record(self):
		self.picam2.start_recording(self.encoder,self.file_name)
		
		annotate_thread = threading.Thread(target=self.update_annotation)
		annotate_thread.start()
		
	def stop(self):
		self.picam2.stop_recording()
		
	def update_annotation(self):
		sleep(0)
		#while True:
			#self.picam2.annotate_background = Color('blue')
			#self.picam2.annotate_foreground = Color('yellow')
			#self.picam2.annotate_text = datetime.datetime.now().strftime("%Y%m%d, %H:%M:%S")
			#self.picam2.annotate_text_size = 20
			#sleep(0.5)
			
	def start(self,file_name,file_dir):
		self.file_name = '{}/{}.mjpeg'.format(file_dir,file_name)
		
		video_thread = threading.Thread(target = self.record)
		video_thread.start()
		video_thread.join()
			
