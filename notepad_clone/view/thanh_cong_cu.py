# notepad_clone/view/thanh_cong_cu.py
import tkinter as tk
from tkinter import ttk

class ThanhCongCu(ttk.Frame):
    def __init__(self, parent, callback_chen):
        super().__init__(parent)
        self.callback_chen = callback_chen
        self.buttons = []
        self._khoi_tao_ui()

    def _khoi_tao_ui(self):
        self.label = ttk.Label(self, text=" Snippets: ")
        self.label.pack(side="left")
        
    def hien_thi_snippets(self, danh_sach_snippets):
        # Xóa các nút cũ
        for btn in self.buttons:
            btn.destroy()
        self.buttons = []

        for sid, ten, noi_dung, la_tag in danh_sach_snippets:
            # Tạo nút với giao diện bo góc (nếu sv-ttk hỗ trợ)
            btn = ttk.Button(
                self, text=ten, 
                command=lambda c=noi_dung: self.callback_chen(c)
            )
            btn.pack(side="left", padx=2, pady=2)
            self.buttons.append(btn)
