
import os
import re
import subprocess
from tempfile import NamedTemporaryFile

from clamapi import app, __version__
from fastapi import File, UploadFile

rverdict = re.compile(r'/tmp/[^:]+:\s([^\n]+)')


@app.get("/")
def read_root():
    return {"clamapi": f"{__version__}"}


@app.post("/scan/")
def scan_file(file: UploadFile = File(...)):
    tmpfile = NamedTemporaryFile(delete=False)
    tmpfile.write(file.file.read())
    tmpfile.close()

    ret = subprocess.run(["/usr/bin/clamdscan", tmpfile.name],
                         encoding="utf8", universal_newlines=True, capture_output=True)

    os.remove(tmpfile.name)

    verdict = rverdict.search(ret.stdout)
    if not verdict:
        verdict = "error: unable to locate verdict in scan output"
    else:
        verdict = verdict.group(1)

    return {file.filename: verdict}
