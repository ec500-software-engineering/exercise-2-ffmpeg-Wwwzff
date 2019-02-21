# python-CI-template
Python CI template for EC500 Software Engineering
## ffmpeg
* This script use os.system to call terminal and run ffmpeg by commands.
* queue QUEUE and QUEUE_HQ are used for storing file paths(string type). Each time finished processing on one file, that path will be popped
* Assign first job by passing path from argv[1], and after finishing that you may type other paths in the command line(split by space)
