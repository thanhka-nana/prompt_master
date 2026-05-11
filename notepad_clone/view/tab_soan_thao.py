# notepad_clone/view/tab_soan_thao.py
import tkinter as tk
from tkinter import ttk
from ..cau_hinh import FONT_MAC_DINH

class TabSoanThao(ttk.Frame):
    def __init__(self, parent, tab_model):
        super().__init__(parent)
        self.model = tab_model
        self._khoi_tao_ui()
        self.load_du_lieu()

    def _khoi_tao_ui(self):
        # Text widget với thanh cuộn
        self.text_area = tk.Text(
            self, undo=True, wrap="none", 
            font=FONT_MAC_DINH, 
            padx=10, pady=10,
            borderwidth=0, highlightthickness=0
        )
        
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.text_area.pack(side="left", fill="both", expand=True)

        # Bind sự kiện để cập nhật thanh trạng thái
        self.text_area.bind("<FocusIn>", lambda e: self.master.master.cap_nhat_trang_thai(f"Tab: {self.model.tieu_de} | Ký tự: {self.lay_so_ky_tu()}"))
        self.text_area.bind("<KeyRelease>", lambda e: self.master.master.cap_nhat_trang_thai(f"Tab: {self.model.tieu_de} | Ký tự: {self.lay_so_ky_tu()}"), add="+")

    def load_du_lieu(self):
        self.text_area.insert("1.0", self.model.noi_dung)
        self.text_area.mark_set("insert", self.model.vi_tri_con_tro)
        self.text_area.see("insert")
        # Cuộn theo tỷ lệ
        self.text_area.yview_moveto(self.model.ty_le_cuon)

    def lay_thong_tin_hien_tai(self):
        noi_dung = self.text_area.get("1.0", "end-1c")
        con_tro = self.text_area.index("insert")
        cuon = self.text_area.yview()[0]
        return noi_dung, con_tro, cuon

    def lay_so_ky_tu(self):
        return len(self.text_area.get("1.0", "end-1c"))
