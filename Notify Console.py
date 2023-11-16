from win10toast import ToastNotifier

import tkinter as tk
import threading

from window import Window

def start():
    root = tk.Tk()
    
    thread = threading.Thread(
        target=show_notifiacation
    )
    thread.start()
    
    Window().show(root)
    
def show_notifiacation():
    toaster = ToastNotifier()
    toaster.show_toast('Title', 'Message')
    
    
if __name__ == '__main__':
    start()