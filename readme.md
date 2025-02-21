# 🤖 Automated Chat Responder

## 🚀 Overview
This project automates chat responses using **PyAutoGUI** for UI automation and **OpenAI's GPT-4o-mini** for generating replies. The script reads incoming messages, generates a response, and sends it automatically, making interactions more seamless and efficient. 🎯

## 🔥 Features
✅ **Real-time message monitoring** 📩  
✅ **Auto-generates responses using AI** 🧠  
✅ **Mimics human-like conversation** 💬  
✅ **Automates typing and sending messages** ✍️  
✅ **Customizable response logic** 🛠️  

## 🛠️ Tech Stack
- **Python** 🐍
- **PyAutoGUI** (for UI automation) 🖱️
- **OpenAI API** (for AI-generated replies) 🤖
- **Pyperclip** (for clipboard handling) 📋
- **OS & Time modules** (for execution control) ⏳

## ⚙️ Requirements
1️⃣ **Install dependencies:**  
   ```bash
   pip install openai pyautogui pyperclip
   ```  
2️⃣ **Set up OpenAI API Key** as an environment variable:
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```
3️⃣ **Adjust chat application coordinates** in the script as per your screen resolution.
4️⃣ **Run the script and let AI handle your chats!** 🤖✨

## 🔧 How It Works
1. The script continuously checks for new messages.
2. If a specific sender (e.g., "Prashant More") sends a message, the script captures it.
3. The message is sent to OpenAI's GPT-4o-mini for processing.
4. The generated response is copied and pasted into the chat automatically.
5. The script ensures a natural, human-like flow of conversation.

## 🚀 Run the Script
Simply execute the script:
```bash
python chat_responder.py
```

## 📌 Notes
- Make sure your chat application is open and active.
- Adjust **coordinates** for text selection and sending messages accordingly.
- Use responsibly and tweak AI responses as needed.

## 📂 Repository
🔗 **Check out the full project on GitHub:**  
👉 [Automated Chat Responder](https://github.com/dhirajdurgade7758/ChatBot-AI)

## 📢 Let's Connect!
💬 Got ideas for improvements? Feel free to contribute or drop a suggestion! 🚀  

#Python #Automation #AI #ChatBot #GPT4o #PyAutoGUI #OpenAI #100DaysOfCode
