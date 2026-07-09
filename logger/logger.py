from datetime import datetime
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "application.log")

os.makedirs(LOG_FOLDER, exist_ok=True)


def write_log(level, message):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"[{current_time}] [{level}] {message}"

    print(log)

    with open(LOG_FILE, "a") as file:
        file.write(log + "\n")