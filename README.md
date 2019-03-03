# python-CI-template
Python CI template for EC500 Software Engineering
## ffmpeg
* This script use subprocess.check_out to call terminal and run ffmpeg by commands.
* queue QUEUE and QUEUE_HQ are used for storing file paths(string type). Each time finished processing on one file, that path will be popped
* Assign first job by passing path from variable filepath.

## Parallel Details
* Convert input video into 720p and 480p in parallel. Each time convert one video in different resolution.
* When works are done the input module will wake up and you may wanna add other jobs.

## How to Run?
Be sure to install ffmpeg first and insert your file path in the ffmpeg.py
```
python ffmpeg.py
```
