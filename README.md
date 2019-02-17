# python-CI-template
Python CI template for EC500 Software Engineering
## ffmpeg
* This script use os.system to call terminal and run ffmpeg by commands.
* queue QUEUE and QUEUE_HQ are used for storing file paths(string type). Each time finished processing on one file, that path will be popped
* When finished all the jobs, you can assign more files from command line.
