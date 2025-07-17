#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime

log_path = "/mnt/data/logs/temp_mon.log"

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
        raw_temp = get_temp().replace("temp=", "").replace("'C", "")

        try:
            temp = float(raw_temp)
            level = "INFO"
            if temp > 70:
                level = "WARN"
            log_line = f"{timestamp} - temp_mon - {level} - Temp: {temp}°C\n"
            with open(log_path, "a") as f:
                f.write(log_line)
        except ValueError:
            # Bad output, skip
            pass

        time.sleep(10)

if __name__ == "__main__":
    main()

