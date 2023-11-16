import tkinter as tk

class Widget():
    def __init__(self):
        self.frame = None
    
    def show_main_frame(self, root: tk.Tk):
        canvas = tk.Canvas(
            master=root,
            width=580,
            height=530
        )
        canvas.place(
            x=0,
            y=0
        )
        
        scrollbar = tk.Scrollbar(
            master=root,
            command=canvas.yview
        )
        scrollbar.place(
            x=585,
            y=0,
            height=530
        )
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.frame = tk.Frame(master=canvas)
        canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor=tk.NW
        )
        
        canvas.bind(
            sequence='<Configure>',
            func=lambda event: canvas.configure(scrollregion=canvas.bbox('all'))
        )
    
    def show_main_buttons(self, root: tk.Tk):
        add_button = tk.Button(
            master=root,
            text='Add',
            command=self.add_task
        )
        add_button.place(
            x=20,
            y=550,
            width=100,
            height=30
        )
        
        remove_button = tk.Button(
            master=root,
            text='Remove'
        )
        remove_button.place(
            x=140,
            y=550,
            width=100,
            height=30    
        )
        
    def add_task(self):
        task_frame = tk.Frame(
            master=self.frame,
            width=580,
            height=40,
            borderwidth=1,
            relief='solid'
        )
        task_frame.pack(pady=5)
        
        