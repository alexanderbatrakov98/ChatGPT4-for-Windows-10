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

        self.language_var = tk.StringVar(value="English")

        self.language_label = tk.Label(master, text="Choose Language:", bg='black', fg='white', font=('Courier', 12))
        self.language_label.pack(padx=20, pady=10)

        self.language_menu = ttk.Combobox(master, textvariable=self.language_var)
        self.language_menu['values'] = ("English", "Русский")
        self.language_menu.bind("<<ComboboxSelected>>", self.change_language)
        self.language_menu.pack(pady=10)

        self.message_label = tk.Label(master, text="Input Field:", bg='black', fg='white', font=('Courier', 12))
        self.message_label.pack(padx=20, pady=20)

        self.text_input = tk.Entry(master, font=("Courier", 12), bg='black', fg='white')
        self.text_input.pack(ipadx=150, ipady=10)

        self.response_label = tk.Label(master, text="Response Field:", bg='black', fg='white', font=('Courier', 12))
        self.response_label.pack(padx=20, pady=20)

        self.text_area = scrolledtext.ScrolledText(master, width=50, height=10, bg='black', fg='white', font=('Courier', 12))
        self.text_area.pack(padx=10, pady=10)

        self.copy_button = tk.Button(master, text="Copy", command=self.copy_content, bg='red', fg='white')
        self.copy_button.pack(padx=10, pady=10, side='left')

        self.send_button = tk.Button(master, text="Send", command=self.send_message, bg='red', fg='white')
        self.send_button.pack(padx=10, pady=10, side='right')

        self.change_language()

    def change_language(self, event=None):
        selected_language = self.language_var.get()
        if selected_language == "English":
            self.message_label.config(text="Input Field:")
            self.response_label.config(text="Response Field:")
            self.copy_button.config(text="Copy")
            self.send_button.config(text="Send")
            self.language_label.config(text="Choose Language:")
        elif selected_language == "Русский":
            self.message_label.config(text="Поле ввода:")
            self.response_label.config(text="Поле ответа:")
            self.copy_button.config(text="Копировать")
            self.send_button.config(text="Отправить")
            self.language_label.config(text="Выберите язык:")

    def send_message(self):
        message: str = self.text_input.get()
        if message:  
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": message}]
            )
            self.text_area.insert(tk.END, f"Response: {response.choices[0].message.content}\\n")
        else:
            messagebox.showerror("Error", "Please enter a message!")

    def copy_content(self):
        content = self.text_area.get("1.0", tk.END)
        if content.strip():
            pyperclip.copy(content.strip())
            messagebox.showinfo("ChatGPT", "Text copied.")
        else:
            messagebox.showwarning("Warning", "No text to copy.")




        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.configure(bg='blue')
    root.resizable(False, False)
    app = MessageSenderApp(root)
    root.mainloop()

