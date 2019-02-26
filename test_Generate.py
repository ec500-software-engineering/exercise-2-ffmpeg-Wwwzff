import pytest
from ffmpeg import run
import subprocess
from probe import ffprobe_sync
from time import sleep


@pytest.fixture
def genpat(tmp_path):
    vidfn = tmp_path/"test.mp4"

    subprocess.check_call(['ffmpeg', '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', 5., str(vidfn)])
    return vidfn


def test_duration():
    fnin = ['test.mp4']
    fnout = ['0.mp4']
    fnout_720 = ['0_HQ.mp4']

    orig_meta = ffprobe_sync(fnin[0])
    orig_duration = float(orig_meta['streams'][0]['duration'])

    run(fnin)
    sleep(100)  # waiting for job to be finished

    meta_480 = ffprobe_sync(fnout[0])
    duration_480 = float(meta_480['streams'][0]['duration'])

    meta_720 = ffprobe_sync(fnout_720[0])
    duration_720 = float(meta_720['streams'][0]['duration'])

    assert orig_duration == pytest.approx(duration_480)
    # assert orig_duration == pytest.approx(duration_720)


if __name__ == "__main__":
    # genpat("./")
    test_duration()
