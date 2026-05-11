# notepad_clone/view/popup_goi_y.py
import tkinter as tk

class PopupGoiY(tk.Toplevel):
    def __init__(self, parent, select_callback):
        super().__init__(parent)
        self.overrideredirect(True) # Không viền
        self.select_callback = select_callback
        
        self.listbox = tk.Listbox(self, font=("Consolas", 10), width=40, height=10)
        self.listbox.pack()
        
        self.listbox.bind("<Double-Button-1>", self._on_select)
        self.listbox.bind("<Return>", self._on_select)
        self.bind("<FocusOut>", lambda e: self.destroy())

    def hien_thi(self, items, x, y):
        self.listbox.delete(0, "end")
        for item in items:
            self.listbox.insert("end", item)
        self.geometry(f"+{x}+{y}")
        self.listbox.focus_set()
        if items:
            self.listbox.selection_set(0)

    def _on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            content = self.listbox.get(selection[0])
            self.select_callback(content)
        self.destroy()
