from agno.models.groq import Groq
from agno.models.message import Message  
from dotenv import load_dotenv
from tkinter import Tk, Frame, Entry, Button, WORD, END, NORMAL, DISABLED, scrolledtext
load_dotenv()
model = Groq(id="llama-3.3-70b-versatile") 
window = Tk()
window.title("Henrique ChatAI")
frame_chat = Frame(window)
f_chat_up = Frame(frame_chat, bg='light green')
f_chat_up.grid(column=0, row=0, pady=(0, 20))
e = Entry(f_chat_up, width=100)
e.grid(column=0, row=0, padx=(0, 30))
user_msg = Message(role="user", content="Olá !")
assistant_msg = Message(role="assistant", content='')

def send():
    resp['state'] = NORMAL
    resp.delete(1.0, END)
    user_msg = Message(
        role="user",
        content=e.get() + ' (Pule uma linha a cada mais ou menos 150 caracteres)'
    )
    try:
        resp.insert(END, model.invoke(messages=[user_msg], assistant_message=assistant_msg).content)
    except Exception as ex:
        msg = str(ex).lower()
        if "api key" in msg or "authentication" in msg or "401" in msg or "invalid_api_key" in msg:
            resp.insert(END, "You need to put a valid API key on .env")
        elif "too long" in msg or "context" in msg or "token" in msg or "413" in msg or "max_tokens" in msg:
            resp.insert(END, "Your prompt is too long")
        else: resp.insert(END, f"Error: {ex}")
    resp['state'] = DISABLED
    e.delete(0, END)

send_b = Button(f_chat_up, text="Send", command=send)
send_b.grid(column=1, row=0)
f_chat_dw = Frame(frame_chat)
f_chat_dw.grid(column=0, row=1)
resp = scrolledtext.ScrolledText(
            f_chat_dw,
            wrap=WORD,
            width=80,
            height=25,
            state=DISABLED
        )
resp.grid(column=0, row=0)
send()
frame_chat.pack()
window.resizable(False, False)
window.mainloop()
