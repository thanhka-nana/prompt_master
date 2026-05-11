# notepad_clone/view/cua_so_chinh.py
import tkinter as tk
from tkinter import ttk
from .notebook_tab import NotebookTab
from .thanh_menu import ThanhMenu
from .thanh_cong_cu import ThanhCongCu
from .thanh_trang_thai import ThanhTrangThai
from ..cau_hinh import TEN_UNG_DUNG, KICH_THUOC_MAC_DINH

try:
    import sv_ttk
    HAS_SV_TTK = True
except ImportError:
    HAS_SV_TTK = False


class CuaSoChinh(tk.Tk):
    def __init__(self, callbacks):
        super().__init__()
        self.callbacks = callbacks
        self.title(TEN_UNG_DUNG)
        self.geometry(KICH_THUOC_MAC_DINH)

        self._thiet_lap_theme()
        self._khoi_tao_ui()
        self._bind_phim_tat()

    def _thiet_lap_theme(self):
        if HAS_SV_TTK:
            sv_ttk.set_theme("dark")
        else:
            style = ttk.Style()
            style.theme_use("clam")

    def _khoi_tao_ui(self):
        # Menu
        self.menu_bar = ThanhMenu(self, self.callbacks)
        self.config(menu=self.menu_bar)

        # Toolbar snippet
        self.toolbar = ThanhCongCu(self, self.callbacks.get("chen_text"))
        self.toolbar.pack(side="top", fill="x")

        # Notebook chính
        self.notebook = NotebookTab(self)
        self.notebook.pack(fill="both", expand=True, padx=2, pady=2)

        # Thanh trạng thái (dùng widget riêng)
        self.status_bar = ThanhTrangThai(self)
        self.status_bar.pack(side="bottom", fill="x")

    def _bind_phim_tat(self):
        self.bind("<Control-n>", lambda e: self.callbacks.get("moi")())
        self.bind("<Control-w>", lambda e: self.callbacks.get("dong")())

    def cap_nhat_trang_thai(self, text):
        """Giữ tương thích ngược với controller hiện tại."""
        self.status_bar.cap_nhat(text)
