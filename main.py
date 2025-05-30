from weather import get_daily_message
from line import push_line_message
import os

def handler():
    city = os.getenv("CITY", "Tokyo")
    user_id = os.getenv("LINE_USER_ID")
    message = get_daily_message(city)
    push_line_message(user_id, message)

if __name__ == "__main__":
    handler()
