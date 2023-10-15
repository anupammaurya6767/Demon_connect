from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from demon_connect.features.extras.get_list_of_messages import get_list_of_messages
def fetch_all_unread_chats(driver, limit=True, top=50):
    """📬 Fetches all unread chats.

    Retrieve all unread chats.

    Args:
        limit (boolean): Should we limit the counting to a certain number of chats (True) or count all (False)? [default = True]
        top (int): Once limiting, what is the *approximate* number of chats that should be considered? [generally, there are natural chunks of 10-22]

    DISCLAIMER: Apparently, fetch_all_unread_chats functionality works on most updated browser versions
    (for example, Chrome Version 102.0.5005.115 (Official Build) (x86_64)). If it fails with you, please
    consider updating your browser while we work on an alternative for non-updated browsers.

    """
    try:
        counter = 0
        pane = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@id="pane-side"]/div[2]')
            )
        )
        list_of_messages = get_list_of_messages(driver)
        read_names = []
        names = []
        names_data = []

        while True:
            last_counter = counter
            for item in list_of_messages:
                name = item["sender"]
                if name not in read_names:
                    read_names.append(name)
                    counter += 1
                if item["unread"]:
                    if name not in names:
                        names.append(name)
                        names_data.append(item)

            pane.send_keys(Keys.PAGE_DOWN)
            pane.send_keys(Keys.PAGE_DOWN)

            list_of_messages = get_list_of_messages(driver)
            if (
                last_counter == counter
                and counter
                >= int(
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//div[@id="pane-side"]/div[2]')
                        )
                    ).get_attribute("aria-rowcount")
                )
                * 0.9
            ):
                break
            if limit and counter >= top:
                break

            print(f"The counter value at this chunk is: {counter}.")

        if limit:
            print(
                f"The list of unread chats, considering the first {counter} messages, is: {names}."
            )
        else:
            print(f"The list of all unread chats is: {names}.")
        return names_data

    except Exception as bug:
        print(f"Exception raised while getting first chat: {bug}")
        return []
