import subprocess
import json
from pathlib import Path
import shutil
if not shutil.which('ffprobe'):
    raise FileNotFoundError('ffprobe not found')

def ffprobe_sync(filein: Path) -> dict:
    """ get media metadata """

    if not Path(filein).is_file():
        raise FileNotFoundError(f'{filein} not found')

    meta = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams','-show_format',str(filein)],universal_newlines=True)
    return json.loads(meta)
