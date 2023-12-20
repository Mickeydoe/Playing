import pywhatkit
import time

# Replace the phone number with the recipient's phone number
recipient_number = "+233248570832"

# Replace the message with the desired message
message = "Testing my spam bot"

# Specify the interval between messages in seconds
message_interval = 1

# Infinite loop to send messages
while True:
    
    pywhatkit.sendwhatmsg(recipient_number, message, 18, 43)
    
    # Sleep for the specified interval before sending the next message
    pywhatkit.press("enter")
    time.sleep(message_interval)





