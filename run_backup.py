import subprocess
import os
from multiprocessing import Pool

# Fill directory
# Remote directory : <username>@<host_or_IP>:<dir>
# Local directory : <dir>

src = "<Source directory>"
dest = "<Destination directory>"

def sync(src):
	subprocess.call(["rsync", "-arq", src, dest])

if __name__== '__main__':
  	src_sub_dir = [str(src+dir) for dir in os.listdir(src)]
	p = Pool(len(src_sub_dir))
  	p.map(sync, src_sub_dir)
