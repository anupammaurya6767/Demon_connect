# features/delete/delete_message.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def delete_message(driver, group_name, message):
    try:
        # locate the sent message and delete it
        sent_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//div[@class="copyable-text selectable-text"]//*[contains(text(), "{message}")]'))
        )

        # Right-click on the message and select "Delete" from the context menu
        from selenium.webdriver.common.action_chains import ActionChains
        actions = ActionChains(driver)
        actions.context_click(sent_message).perform()
        delete_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/span[4]/div/ul/div[5]/li[1]'))
        )
        delete_option.click()

        print(f"Message deleted in group {group_name}: {message}")

    except Exception as e:
        print(f"An error occurred while deleting the message: {str(e)}")

# Usage Example:
# Call delete_message(driver, group_name, message) function in your main.py script
# to delete a specific message in a WhatsApp group.
