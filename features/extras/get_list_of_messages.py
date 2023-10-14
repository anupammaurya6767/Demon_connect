from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def get_list_of_messages(driver):
    """🗂️ Gets the list of messages in the page.

    Gets the list of messages in the page.
    """
    messages = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//*[@id="pane-side"]/div[2]/div/div/child::div')
        )
    )

    clean_messages = []
    for message in messages:
        _message = message.text.split("\n")
        if len(_message) == 2:
            clean_messages.append(
                {
                    "sender": _message[0],
                    "time": _message[1],
                    "message": "",
                    "unread": False,
                    "no_of_unread": 0,
                    "group": False,
                }
            )
        elif len(_message) == 3:
            clean_messages.append(
                {
                    "sender": _message[0],
                    "time": _message[1],
                    "message": _message[2],
                    "unread": False,
                    "no_of_unread": 0,
                    "group": False,
                }
            )
        elif len(_message) == 4:
            clean_messages.append(
                {
                    "sender": _message[0],
                    "time": _message[1],
                    "message": _message[2],
                    "unread": _message[-1].isdigit(),
                    "no_of_unread": int(_message[-1]) if _message[-1].isdigit() else 0,
                    "group": False,
                }
            )
        elif len(_message) == 5:
            clean_messages.append(
                {
                    "sender": _message[0],
                    "time": _message[1],
                    "message": "",
                    "unread": _message[-1].isdigit(),
                    "no_of_unread": int(_message[-1]) if _message[-1].isdigit() else 0,
                    "group": True,
                }
            )
        elif len(_message) == 6:
            clean_messages.append(
                {
                    "sender": _message[0],
                    "time": _message[1],
                    "message": _message[4],
                    "unread": _message[-1].isdigit(),
                    "no_of_unread": int(_message[-1]) if _message[-1].isdigit() else 0,
                    "group": True,
                }
            )
        else:
            print(f"🤔 Unknown message format: {_message}")
    return clean_messages
