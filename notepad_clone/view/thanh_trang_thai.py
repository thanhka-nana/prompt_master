# notepad_clone/view/thanh_trang_thai.py
from tkinter import ttk


class ThanhTrangThai(ttk.Frame):
    """Thanh trạng thái ở dưới cùng cửa sổ, hiển thị thông tin tab hiện tại."""

    def __init__(self, parent):
        super().__init__(parent, relief="sunken")
        self._khoi_tao_ui()

    def _khoi_tao_ui(self):
        # Label trạng thái chính (bên trái)
        self.lbl_trang_thai = ttk.Label(self, text="Sẵn sàng", anchor="w")
        self.lbl_trang_thai.pack(side="left", fill="x", expand=True, padx=5)

        # Label số ký tự (bên phải)
        self.lbl_ky_tu = ttk.Label(self, text="Ký tự: 0", anchor="e")
        self.lbl_ky_tu.pack(side="right", padx=10)

        # Label vị trí con trỏ (bên phải)
        self.lbl_vi_tri = ttk.Label(self, text="Dòng: 1 | Cột: 0", anchor="e")
        self.lbl_vi_tri.pack(side="right", padx=10)

    def cap_nhat(self, text):
        """Cập nhật nội dung thanh trạng thái chính."""
        self.lbl_trang_thai.config(text=text)

    def cap_nhat_ky_tu(self, so_ky_tu):
        """Cập nhật số ký tự hiển thị."""
        self.lbl_ky_tu.config(text=f"Ký tự: {so_ky_tu}")

    def cap_nhat_vi_tri(self, dong, cot):
        """Cập nhật vị trí con trỏ hiển thị."""
        self.lbl_vi_tri.config(text=f"Dòng: {dong} | Cột: {cot}")
