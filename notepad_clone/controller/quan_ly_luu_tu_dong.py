# notepad_clone/controller/quan_ly_luu_tu_dong.py
from datetime import datetime
from ..tien_ich.debounce import debounce
from ..cau_hinh import THOI_GIAN_DEBOUNCE


class QuanLyLuuTuDong:
    def __init__(self, view, model_quan_ly_tab, quan_ly_phien=None):
        self.view = view
        self.model = model_quan_ly_tab
        self.quan_ly_phien = quan_ly_phien
        self._thiet_lap_binding()

    def _thiet_lap_binding(self):
        # Bind sự kiện phím cho tất cả các tab hiện có
        for tid, tab_view in self.view.notebook.tabs_dict.items():
            self._gan_debounce_cho_tab(tab_view)

        # Bind khi chuyển tab để lưu ngay lập tức
        self.view.notebook.bind(
            "<<NotebookTabChanged>>", self._khi_chuyen_tab
        )

        # Bind khi đóng ứng dụng
        self.view.protocol("WM_DELETE_WINDOW", self._khi_dong_app)

    def _gan_debounce_cho_tab(self, tab_view):
        """Tạo hàm lưu được debounce và bind vào KeyRelease."""
        luu_func = debounce(
            tab_view.text_area,
            lambda e=None: self._thuc_hien_luu(tab_view),
            THOI_GIAN_DEBOUNCE
        )
        tab_view.text_area.bind("<KeyRelease>", luu_func)

    def _thuc_hien_luu(self, tab_view):
        noi_dung, con_tro, cuon = tab_view.lay_thong_tin_hien_tai()
        self.model.luu_tab(
            tab_view.model.id, noi_dung, con_tro, cuon
        )
        gio = datetime.now().strftime("%H:%M:%S")
        self.view.cap_nhat_trang_thai(
            f"Đã lưu tab \"{tab_view.model.tieu_de}\" lúc {gio}"
        )

    def _khi_chuyen_tab(self, event):
        """Lưu tab hiện tại ngay khi chuyển sang tab khác."""
        tid, tab_view = self.view.notebook.lay_tab_active()
        if tab_view:
            self._thuc_hien_luu(tab_view)

    def _khi_dong_app(self):
        """Lưu tất cả tab + phiên làm việc rồi đóng cửa sổ."""
        for tid, tab_view in self.view.notebook.tabs_dict.items():
            self._thuc_hien_luu(tab_view)

        # Lưu phiên làm việc nếu có quản lý phiên
        if self.quan_ly_phien:
            self.quan_ly_phien.luu_phien(self.view.notebook)

        self.view.destroy()
