'''
This script is used for processing on a batch of videos and
using FFMPEG to do series of jobs

Copyright 2019 chesterw@bu.edu by Zifan Wang
'''

import os
from threading import Thread
import time

QUEUE = []
QUEUE_HQ = []

COUNT_HQ = 0
COUNT = 0
i = 0


def ffmpeg_hq():
    '''
    Convert file to 720p at 2Mbps and 30fps
    '''
    global COUNT_HQ, i
    while QUEUE_HQ:
        print("[FFMPEG_HQ]Working on the "+str(COUNT_HQ+1)+" job.")
        single_file = QUEUE_HQ[0]
        os.system("ffmpeg -i "+single_file+" -b 2M -r 30 -f mp4 -s 1280x720 -loglevel quiet "+str(COUNT_HQ)+"_HQ.mp4")
        QUEUE_HQ.pop(0)
        COUNT_HQ += 1
        print("[FFMPEG_HQ]Finished "+str(COUNT_HQ+COUNT)+" now. "+str(i*2-COUNT_HQ-COUNT)+" left.")
        time.sleep(3)
    ffmpeg()


def ffmpeg():
    '''
    Convert file to 480p at 1Mbps and 30fps
    '''
    global COUNT, i, COUNT_HQ
    while QUEUE:
        print("[FFMPEG]Working on the "+str(COUNT+1)+" job.")
        single_file = QUEUE[0]
        os.system("ffmpeg -i "+single_file+" -b 1M -r 30 -f mp4 -s 640x480 -loglevel quiet "+str(COUNT)+".mp4")
        QUEUE.pop(0)
        COUNT += 1
        print("[FFMPEG]Finished "+str(COUNT+COUNT_HQ)+" now. "+str(i*2-COUNT_HQ-COUNT)+" left.")
        time.sleep(3)
    print("[Finished]All works are done. You may now input other files to work on.")
    inmodule()


def inmodule():
    '''
    Get file path from user's input
    '''
    global i
    try:
        i = int(input("[Input]How many jobs do you wanna take:\n"))
    except ValueError:
        exit(0)

    while len(QUEUE) < i or len(QUEUE_HQ) < i:
        single = input("[Input]Give another file path:\n")
        if single:
            QUEUE.append(single)
            QUEUE_HQ.append(single)
            print("[Input]File added. There're " + str(len(QUEUE)) + " file waiting in queue")
        time.sleep(0.5)


THREADS = []
T1 = Thread(target=ffmpeg())
THREADS.append(T1)
T2 = Thread(target=ffmpeg_hq())
THREADS.append(T2)
T3 = Thread(target=inmodule())
THREADS.append(T3)

for thread in THREADS:
    thread.start()
