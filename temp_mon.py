#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime

log_path = "/mnt/data/logs/temp_log.txt"

def get_temp():
    result = subprocess.run(
        ["/usr/bin/vcgencmd", "measure_temp"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def main():
    while True:
        timestamp = datetime.now().isoformat()
        temp = get_temp().replace("temp=", "").replace("'C", "")
        try:
            if float(temp) > 50:
                with open(log_path, "a") as f:
                    f.write(f"{timestamp} = {temp}\n")
        except ValueError:
            pass  # skip bad output
        time.sleep(10)

if __name__ == "__main__":
    main()
