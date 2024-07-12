from datetime import datetime
import os
import locale


def load_openai_key():
    with open("openai.key", "r") as f:
        os.environ["OPENAI_API_KEY"] = f.read().strip()



def parse_to_date_object(date_str: str) -> datetime:
    locale.setlocale(locale.LC_TIME, 'de_DE')
    date_obj = datetime.strptime(date_str, "%d. %B %Y")
    return date_obj