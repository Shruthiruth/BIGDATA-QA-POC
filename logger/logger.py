from datetime import datetime

LOG_FILE = "logs/application.log"

def write_log(level, message):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{current_time}] [{level}] {message}"

    print(log_message)

    with open(LOG_FILE, "a") as file:
        file.write(log_message + "\n")