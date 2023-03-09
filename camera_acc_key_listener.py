import time
import threading
import subprocess
import os
from pynput import keyboard

from AccelerometerRecorder import AccRecorder
from VideoRecorder import VideoRecorder

def record_ten_seconds():
	file_name = time.ctime(time.time())
	
	start_ACCVideoRecording(file_name)
	time.sleep(10)
	stop_ACCVideoRecording(file_name)

def start_ACCVideoRecording(file_name):
    print("Starting threads...")
    video_thread.start(file_name, file_dir)
    acc_thread.start(file_name, file_dir)
    

def stop_ACCVideoRecording(file_name):
    print("Stopping threads...")
    acc_thread.stop()
    video_thread.stop()
    print("done")

def key_press(key):
    try:
        a=key.char
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=key_press)
listener.start()

def main():
    global video_thread
    global acc_thread
    global file_dir, file_name
    global a
    
    
    # Creates final media directory if does not exist
    file_dir = "/home/ktm/Dev/media"
    #if(os.path.isdir(final_dir) == False):
    #    print("Can't find media directory, creating...")
    #    os.mkdir(final_dir)

    # Initializes threads
    video_thread = VideoRecorder()
    acc_thread = AccRecorder()

    # Allows time for camera to boot up
    time.sleep(2)

    #button = Button(14)
    #button.when_pressed = record_ten_seconds
    print("ready for action!")
    
    while True:
        try:
            record_ten_seconds()
        except KeyboardInterrupt:  #ctrl C or Ctrl z is the keyboard interrupt
            break
    
    print("stop")
    stop_ACCVideoRecording(file_name)
    listener.stop()
    

if __name__ == "__main__":
    main()
