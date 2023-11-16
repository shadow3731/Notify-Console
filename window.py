import tkinter as tk

from widget import Widget

class Window():
    
    def __init__(self):
        self.widget_obj = Widget()
    
    def show(self, root: tk.Tk):
        self._center_window(root)
        self._show_widgets(root)
        
        root.title('Notify Console')
        root.mainloop()
        
    def _center_window(self, root: tk.Tk):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        x = (screen_width - 600) // 2
        y = (screen_height - 600) // 2
        
        root.geometry(f'{600}x{600}+{x}+{y}')
        
    def _show_widgets(self, root: tk.Tk):
        self.widget_obj.show_main_frame(root)
        self.widget_obj.show_main_buttons(root)