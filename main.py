import tkinter as tk
from tkUI import ChatInterface
from ai_assistant import AI, init_context, end_call
from functions import say, speechToText
from threading import Thread
import signal
import sys

def chat(ui):
    try:
        print("Welcome to the Customer Service Bot!")
        chat_context = init_context()
        ai_answer = AI("namaste", chat_context)
        ui.add_message(ai_answer, "bot")
        print(ai_answer)
        say(ai_answer)

        while ui.is_chatting:
            userResponse = speechToText()
            print(f"USER: {userResponse}")
            ui.add_message(userResponse, "user")

            if "stop listening" in userResponse.lower() or not ui.is_chatting:
                break

            if userResponse:
                ai_answer = AI(userResponse, chat_context)
                print(ai_answer)
                say(ai_answer)
                ui.add_message(ai_answer, "bot")

        end_call(chat_context)
        print("\nThank you for the interview!")
        say("Customer Service me sampark karne ke liye aapka dhanyavad. aapka din mangalmay ho!")
    except Exception as e:
        print(f"An error occurred: {e}")
        ui.add_message(f"An error occurred: {e}", "red")
    finally:
        ui.is_chatting = False
        ui.master.after(0, lambda: ui.start_button.config(state=tk.NORMAL))
        ui.master.after(0, lambda: ui.stop_button.config(state=tk.DISABLED))

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.chat_interface = ChatInterface(master)
        self.chat_thread = None

        # Override the start and stop actions
        self.chat_interface.start_button.config(command=self.start_chat)
        self.chat_interface.stop_button.config(command=self.stop_chat)

    def start_chat(self):
        if not self.chat_interface.is_chatting:
            self.chat_interface.start_action()
            self.chat_thread = Thread(target=chat, args=(self.chat_interface,))
            self.chat_thread.start()

    def stop_chat(self):
        if self.chat_interface.is_chatting:
            self.chat_interface.stop_action()
            if self.chat_thread:
                if sys.platform.startswith('win'):
                    self.chat_thread.stop_flag = True
                else:
                    signal.pthread_kill(self.chat_thread.ident, signal.SIGTERM)
                self.chat_thread.join()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()