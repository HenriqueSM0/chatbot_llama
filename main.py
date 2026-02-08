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

user_msg = Message(
    role="user",
    content="Olá !"
)
assistant_msg = Message(role="assistant", content='')

def send():
    resp['state'] = NORMAL
    resp.delete(1.0, END)
    user_msg = Message(
        role="user",
        content=e.get() + ' (Pule uma linha a cada mais ou menos 150 caracteres)'
    )
    resp.insert(END, model.invoke(messages=[user_msg], assistant_message=assistant_msg).content)
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
            state = DISABLED
        )
resp.grid(column=0, row=0)

send()

frame_chat.pack()
window.resizable(False, False)
window.mainloop()