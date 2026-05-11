# notepad_clone/view/popup_cai_dat.py
import tkinter as tk
from tkinter import ttk

class PopupCaiDat(tk.Toplevel):
    def __init__(self, parent, callbacks):
        super().__init__(parent)
        self.title("Cài đặt")
        self.geometry("500x400")
        self.callbacks = callbacks
        self._khoi_tao_ui()

    def _khoi_tao_ui(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Tab Quản lý Snippets
        self.tab_snippet = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_snippet, text="Snippets")
        self._ui_snippets()
        
    def _ui_snippets(self):
        lbl = ttk.Label(self.tab_snippet, text="Tên nút:")
        lbl.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.ent_ten = ttk.Entry(self.tab_snippet)
        self.ent_ten.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        lbl2 = ttk.Label(self.tab_snippet, text="Nội dung chèn:")
        lbl2.grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.txt_content = tk.Text(self.tab_snippet, height=5, font=("Consolas", 10))
        self.txt_content.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        btn_add = ttk.Button(self.tab_snippet, text="Thêm Snippet", command=self._on_add)
        btn_add.grid(row=2, column=1, sticky="e", padx=5, pady=5)

    def _on_add(self):
        ten = self.ent_ten.get()
        noi_dung = self.txt_content.get("1.0", "end-1c")
        if ten and noi_dung:
            self.callbacks.get("them_snippet")(ten, noi_dung)
            self.ent_ten.delete(0, "end")
            self.txt_content.delete("1.0", "end")
