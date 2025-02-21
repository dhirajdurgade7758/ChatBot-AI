import os
import pyautogui
import time
import pyperclip
from openai import OpenAI

# Function to check if the last message is from "Prashant More (SIT)"
def is_last_message_from_sender(chat_log, sender="Prashant More (SIT)"):
    message = chat_log.strip().split("/2025]")[-1]
    return sender in message

# Function to get clipboard text reliably
def get_clipboard_text():
    prev_text = pyperclip.paste()
    for _ in range(10):  # Retry for 5 seconds
        time.sleep(0.5)
        new_text = pyperclip.paste()
        if new_text != prev_text:
            return new_text
    return prev_text  # Return old text if no update

# Allow time to switch to the chat window
time.sleep(2)

# Click on the chat app icon (adjust coordinates if necessary)
pyautogui.click(1071, 1045)
time.sleep(1)

# Initialize OpenAI client (Replace 'your-api-key' with your actual API key)
try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"Failed to initialize OpenAI: {e}")
    exit(1)

# Main loop for chat monitoring
while True:
    try:
        
        # Select chat messages
        pyautogui.moveTo(683, 267)
        pyautogui.mouseDown()
        pyautogui.moveTo(1848, 882, duration=1)
        pyautogui.mouseUp()

        # Copy to clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        pyautogui.click(1848, 882)

        # Retrieve copied text
        chatHistory = get_clipboard_text()

        if is_last_message_from_sender(chatHistory):
            # Generate roast response
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                # messages=[
                #     {"role": "system", "content": '''You are Dhiraj, a coder and chill friend from India who speaks Marathi and Hindi. 
                #     Your replies are **based on the conversation context** and can be funny, sarcastic, helpful, or serious depending on the previous messages. 
                #     The reply should be natural and **not forced to be funny** every time. Respond **like a real person would in a chat.** 
                #     Avoid including timestamps or sender names in the message.'''},
                #     {"role": "user", "content": chatHistory}
                # ]
                messages=[
                    {"role": "system", "content": '''You are Dhiraj, a friendly and casual person from India who speaks Marathi and Hindi. 
                    Your replies should be **short (1-2 lines)**, natural, and relevant to the conversation. 
                    They can be helpful, engaging, or slightly humorous if the context allows, but avoid unnecessary sarcasm or roasting. 
                    Reply **as a real person would in a chat**, keeping it conversational and natural. 
                    Avoid including timestamps or sender names in the message.'''},
                    {"role": "user", "content": chatHistory}
                ]
            )

            response_text = completion.choices[0].message.content
            pyperclip.copy(response_text)

            # Paste response in chat
            pyautogui.click(921, 955)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.5)
            pyautogui.press('enter')

            print(f"Sent Response: {response_text}")
            time.sleep(5)


    except Exception as e:
        print(f"Error: {e}")
