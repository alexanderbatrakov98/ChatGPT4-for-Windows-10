from g4f.client import Client

client = Client()

import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk 

import pyperclip

class MessageSenderApp:

    def __init__(self, master):
        self.master = master
        master.title('GPT-4')


        self.message_label = tk.Label(master, text="Поле ввода:", bg='black', fg='white', font=('Courier', 12))
        self.message_label.pack(padx=20, pady=20)

        self.text_input = tk.Entry(master, font=("Courier", 12), bg='black', fg='white')
        self.text_input.pack(ipadx=150, ipady=10)

        self.message_label = tk.Label(master, text="Поле ответа:", bg='black', fg='white', font=('Courier', 12))
        self.message_label.pack(padx=20, pady=20)

        self.text_area = scrolledtext.ScrolledText(master, width=50, height=10, bg='black', fg='white', font=('Courier', 12))
        self.text_area.pack(padx=10, pady=10)

        self.copy_button = tk.Button(master, text="Копировать", command=self.copy_content, bg='red', fg='white')
        self.copy_button.pack(padx=10, pady=10, side='left')

        self.send_button = tk.Button(master, text="Отправить", command=self.send_message, bg='red', fg='white')
        self.send_button.pack(padx=10, pady=10, side='right')


    def send_message(self):
        message: str = self.text_input.get()
        if message:  
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": message}]
            )
            self.text_area.insert(tk.END, f"Ответ: {response.choices[0].message.content}")
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите сообщение!")

    def copy_content(self):
        content = self.text_area.get("1.0", tk.END)
        if content.strip():
            pyperclip.copy(content.strip())
            messagebox.showinfo("ChatGPT", "Текст скопирован.")
        else:
            messagebox.showwarning("Внимание", "Нет текста для копирования.")




        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.configure(bg='blue')
    root.resizable(False, False)
    app = MessageSenderApp(root)
    root.mainloop()

