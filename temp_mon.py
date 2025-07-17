#!/usr/bin/env python3

import subprocess
import time
import os
from datetime import datetime

log_path = os.path.expanduser("var/log/temp_log.txt")

def get_temp():
    result = subprocess.run(
    ["/usr/bin/vcgencmd", "measure_temp"],
    capture_output=True,
    text=True
    )
    return result.stdout.strip()

def main():
    timestamp = datetime.now().isoformat()
    temp = get_temp().replace("temp=", "").replace("'C", "")
    if(float(temp) > 60):
        with open(log_path, "a") as f:
            f.write(f"{timestamp} = {temp}\n")
        time.sleep(1)

main()
