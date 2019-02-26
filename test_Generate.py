import pytest
from ffmpeg import run, checkstatus
import subprocess
from probe import ffprobe_sync


@pytest.fixture
def genpat(tmp_path):
    vidfn = tmp_path/"test.mp4"

    subprocess.check_call(['ffmpeg', '-v', 'warning', '-f', 'lavfi', '-i', 'smptebars', '-t', 5., str(vidfn)])
    return vidfn


def test_duration():
    fnin = ['test.mp4']
    fnout = ['0.mp4']
    
    orig_meta = ffprobe_sync(fnin[0])
    orig_duration = float(orig_meta['streams'][0]['duration'])

    run(fnin)
    
    if checkstatus():
        meta_480 = ffprobe_sync(fnout[0])
        duration_480 = float(meta_480['streams'][0]['duration'])
        assert orig_duration == pytest.approx(duration_480)

        
        
def test_duration_720():
    fnout_720 = ['0_HQ.mp4']
    duration_720 = float(meta_720['streams'][0]['duration'])
    meta_720 = ffprobe_sync(fnout_720[0])
    assert orig_duration == pytest.approx(duration_720)
    
    
if __name__ == "__main__":
    # genpat("./")
    test_duration()
