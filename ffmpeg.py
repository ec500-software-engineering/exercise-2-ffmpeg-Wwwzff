'''
This script is used for processing on a batch of videos and
using FFMPEG to do series of jobs

Copyright 2018 chesterw@bu.edu by Zifan Wang
'''

import subprocess
from threading import Thread
import time
from queue import Queue

QUEUE = Queue()
QUEUE_HQ = Queue()

COUNT_HQ = 0
COUNT = 0
TOTAL = 0
TMP = []
done = False
done_HQ = False



def ffmpeg_hq():
    '''
    Convert file to 720p at 2Mbps and 30fps
    '''
    global COUNT_HQ, QUEUE_HQ, TOTAL, done_HQ
    while True:
        if not QUEUE_HQ.empty():
            done_HQ = False
            print("[FFMPEG_HQ]Working on the "+str(COUNT_HQ+1)+" job.")
            single_file = QUEUE_HQ.get()
            info = "ffmpeg -i "+single_file+" -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+str(COUNT_HQ)+"_HQ.mp4"
            subprocess.check_call(info.split(" "))
            COUNT_HQ += 1
            
            print("[FFMPEG_HQ]Finished "+str(COUNT_HQ + COUNT)+" now. "+str(TOTAL - COUNT - COUNT_HQ)+" left.")
            time.sleep(3)
            done_HQ = True
        else:
            # idle for 30 seconds and end thread
            time.sleep(3)
            if QUEUE.empty():
                break


def ffmpeg():
    '''
    Convert file to 480p at 1Mbps and 30fps
    '''
    global COUNT, COUNT_HQ, QUEUE, TOTAL, done
    while True:
        if not QUEUE.empty():
            done = False
            print("[FFMPEG]Working on the "+str(COUNT+1)+" job.")
            single_file = QUEUE.get()
            info = "ffmpeg -i "+single_file+" -b 1M -r 30 -f mp4 -s hd480 -loglevel quiet "+str(COUNT)+".mp4"
            subprocess.check_call(info.split(" "))
            
            COUNT += 1
            print("[FFMPEG]Finished "+str(COUNT + COUNT_HQ)+" now. "+str(TOTAL - COUNT - COUNT_HQ)+" left.")
            time.sleep(3)
            done = True
            '''
            if not Path(str(COUNT)+".mp4").is_file():
                raise RuntimeError(f'did not convert {single_file}')
            '''
        else:
            time.sleep(3)
            if QUEUE.empty():
                break


def inmodule(filepath):
    '''
    Get file path from user's input
    '''
    global QUEUE, QUEUE_HQ, TOTAL, TMP
    fir_time = True
    while True:
        if QUEUE.empty() and QUEUE_HQ.empty() and TOTAL - COUNT - COUNT_HQ == 0:
            # python ffmpeg.py ~/Videos
            # path = pathlib.Path(sys.argv[1])
            # filelist = path.glob('*.mp4')
            if fir_time:
                # filepath = sys.argv[1:]
                # filepath ="/Users/zifanwang/Downloads/test.mp4"
                if filepath:
                    print("[Input]Input path confirmed")
                    TMP = list(filepath)
                    TOTAL += 2 * len(TMP)
                    for item in TMP:
                        QUEUE.put(item)
                        QUEUE_HQ.put(item)
                    fir_time = False
        else:
            break
            '''
            TMP = input("[Input]Previous work finished. Give file paths, split by space:\n")
            if TMP:
                TOTAL += 2 * len(TMP)
                for item in TMP:
                    QUEUE.put(item)
                    QUEUE_HQ.put(item)
            '''

           
def checkstatus():
    global done, done_HQ
    if done and done_HQ:
        return True
    else:
        return False


def run(filepath):
    THREADS = []
    T1 = Thread(target=ffmpeg_hq)
    THREADS.append(T1)
    T2 = Thread(target=ffmpeg)
    THREADS.append(T2)


    # T3 = Thread(target=inmodule,args=filepath)
    # THREADS.append(T3)

    inmodule(filepath)

    for thread in THREADS:
        thread.setDaemon(True)
        thread.start()

if __name__ == "__main__":
    filepath = ""
    run(filepath)
