import pyautogui
import time
import pyperclip
from openai import OpenAI
# Allow some time to switch to the correct screen

def is_last_message_from_sender(chat_log, sender="Prashant More (SIT)"):
    message = chat_log.strip().split("/2025]")[-1]
    if sender in message:
        return True
    
    return False



time.sleep(2)

# Click on the icon at (1071, 1045)
pyautogui.click(1071, 1045)
time.sleep(1)  # Wait for any UI changes

while(True):
    # Click and drag to select text from (547, 136) to (1794, 927)
    time.sleep(5)
    pyautogui.moveTo(683, 267)
    pyautogui.mouseDown()
    pyautogui.moveTo(1848, 882, duration=1)  # Smooth movement
    pyautogui.mouseUp()
    time.sleep(0.5)  # Allow UI to process selection
    # Copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for text to be copied
    pyautogui.click(1848, 882)

    # Retrieve copied text
    chatHistory = pyperclip.paste()

    if is_last_message_from_sender(chatHistory):

        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": '''You are a person named dhiraj who speaks in both language marathi and hindi. 
                you are from india and  you are coder and chill friend. You analyze chat history and roast people in a funny way replay should be short like human replay. Output should be the next chat response give text message only do not include '[5:26 pm, 21/2/2025] Dhiraj:' this in text message '''},
                {
                    "role": "user",
                    "content": chatHistory
                }
            ]
        )

        responce = pyperclip.copy(completion.choices[0].message.content)
        print(responce)
        # Click at (921, 955) to focus the input field
        pyautogui.click(921, 955)
        time.sleep(0.5)  # Ensure focus

        # Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # Press Enter
        pyautogui.press('enter')
