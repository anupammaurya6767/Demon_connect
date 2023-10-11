# main.py
from utils.constants import BROWSER
from utils.constants import USR_DIR
from utils.constants import CHROME_DRIVER_PATH
from api.whatsapp_api import Demon

def main():
    whatsapp_demon = None
    try:

        # Create an instance of the Demon class
        whatsapp_demon = Demon(BROWSER,USR_DIR,CHROME_DRIVER_PATH)

        # Log in to WhatsApp Web
        whatsapp_demon.login()

        # Send a message
        message = "heyy"
        contact = "Anupam Maurya 3rd Year"
        whatsapp_demon.send_message(contact,message )

        # Receive messages
        received_messages = whatsapp_demon.receive_message()
        print("Received Messages:")
        for message in received_messages:
            print(message)
            
        # Send an image (provide the path to the image file)
        image_path = r"C:\Users\hp\Pictures\WhatsApp Image 2021-12-11 at 7.19.40 PM.jpeg"
        whatsapp_demon.send_image(contact,image_path)

        # Send a video (provide the path to the video file)
        video_path = "path/to/your/video.mp4"
        whatsapp_demon.send_video(video_path)

        # Send a group message
        group_name = "YourGroupName"
        group_message = "This is a group message."
        whatsapp_demon.send_group_message(group_name, group_message)

        # Delete a message in a group chat
        group_name = "YourGroupName"
        message_to_delete = "Message to delete"
        whatsapp_demon.delete_message(group_name, message_to_delete)

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the browser when done
        if whatsapp_demon is not None:
            whatsapp_demon.close()

if __name__ == "__main__":
    main()
