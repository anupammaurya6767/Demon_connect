from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def add_caption(driver, message: str, media_type: str = "image"):
    """📝 Adds a caption to media (image, video, or file) before sending.

    Args:
        message (str): The caption text to add.
        media_type (str, optional): The type of media to add the caption to (image, video, or file). Defaults to "image".
    """
    xpath_map = {
        "image": "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]",
        "video": "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]",
        "file": "/html/body/div[1]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[1]/div[1]",
    }

    inp_xpath = xpath_map[media_type]
    input_box = driver.wait.until(
        EC.presence_of_element_located((By.XPATH, inp_xpath))
    )

    for line in message.split("\n"):
        input_box.send_keys(line)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
            Keys.ENTER
        ).key_up(Keys.SHIFT).perform()
        print(f"📝 Caption added: {line}")
