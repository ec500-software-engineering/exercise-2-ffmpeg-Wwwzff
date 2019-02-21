import pytest
import ffmpeg
import os


@pytest.mark.asyncio
async def test_ffmpeg():
    dur = await ffmpeg.run()
    assert dur == pytest.approx(5.)

if __name__ == '__main__':
    pytest.main(['-x',__file__])
