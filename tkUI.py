import tkinter as tk
from tkinter import scrolledtext

class ChatInterface:
    def __init__(self, master):
        self.master = master
        master.title("Chat Interface")
        master.geometry("900x500")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=20)
        self.chat_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Input frame
        input_frame = tk.Frame(master)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        # Configure grid weights
        input_frame.grid_columnconfigure(1, weight=1)

        # Button frame
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Start button (green)
        self.start_button = tk.Button(button_frame, text="Start", command=self.start_action, bg="green", fg="black")
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Stop button (red)
        self.stop_button = tk.Button(button_frame, text="Stop", command=self.stop_action, bg="red", fg="black", state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Exit button
        self.exit_button = tk.Button(button_frame, text="Exit", command=self.exit_action, bg="gray", fg="black")
        self.exit_button.pack(side=tk.LEFT, padx=5)

        self.is_chatting = False

    def start_action(self):
        if not self.is_chatting:
            self.is_chatting = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.add_message("Call Started!", "green")

    def stop_action(self):
        if self.is_chatting:
            self.is_chatting = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.add_message("Call Ended.", "red")

    def exit_action(self):
        self.master.quit()

    def add_message(self, message, sender="bot"):
        self.chat_area.config(state=tk.NORMAL)
        if sender == "user":
            self.chat_area.insert(tk.END, "You: " + message + "\n", "user")
            self.chat_area.tag_configure("user", justify="right", foreground="yellow")
        elif sender == "bot":
            self.chat_area.insert(tk.END, "Bot: " + message + "\n", "bot")
            self.chat_area.tag_configure("bot", justify="left", foreground="blue")
        elif sender in ["green", "red"]:
            self.chat_area.insert(tk.END, message + "\n", sender)
            self.chat_area.tag_configure(sender, justify="center", foreground=sender)
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.see(tk.END)