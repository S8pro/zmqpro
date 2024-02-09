import subprocess
from threading import Thread

from serverclass import dupserver

dupserver = dupserver()
duplication_server_thread = Thread(target=lambda: dupserver.server(address="tcp://*:5545"), daemon=True)
duplication_server_thread.start()

target_dir = "testtarget"
# docker build -t my-basic-image .
command = f'docker run --network="host" -it -v {target_dir}:/data/targetDir my-basic-image:latest '
command += f"python -m client.py"
command += f"docker volume inspect testtarget"
subprocess.run(command, check=True)