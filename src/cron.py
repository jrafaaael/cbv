import os
from crontab import CronTab

PATH = os.getcwd()
MAIN_SCRIPT_PATH = f"{PATH}/src/main.py"

cron = CronTab(True)
job = cron.new(command=f"python3 {MAIN_SCRIPT_PATH}")
job.every(1).hours()
cron.write()
