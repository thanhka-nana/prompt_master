# notepad_clone/controller/quan_ly_phien.py
import json


class QuanLyPhien:
    """Lưu và khôi phục danh sách tab đang mở giữa các phiên làm việc."""

    KHOA_PHIEN = "phien_tab_ids"

    def __init__(self, model_cai_dat, model_tab):
        self.cai_dat = model_cai_dat
        self.model_tab = model_tab

    def luu_phien(self, notebook):
        """Lưu danh sách id các tab đang mở vào settings."""
        tab_ids = list(notebook.tabs_dict.keys())
        self.cai_dat.luu(self.KHOA_PHIEN, json.dumps(tab_ids))

    def khoi_phuc_phien(self, notebook):
        """Khôi phục các tab từ phiên trước. Trả về danh sách TabSoanThao mới."""
        raw = self.cai_dat.lay(self.KHOA_PHIEN, "[]")
        try:
            tab_ids = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            tab_ids = []

        ds_tab_view = []
        for tid in tab_ids:
            tab_model = self._tim_tab(tid)
            if tab_model:
                frame = notebook.them_tab(tab_model)
                ds_tab_view.append(frame)

        # Nếu không có tab nào, tạo tab mặc định
        if not ds_tab_view:
            moi = self.model_tab.tao_tab_moi("Untitled 1")
            frame = notebook.them_tab(moi)
            ds_tab_view.append(frame)

        return ds_tab_view

    def _tim_tab(self, tab_id):
        """Tìm tab model theo id trong danh sách đã load."""
        for tab in self.model_tab.danh_sach_tab:
            if tab.id == tab_id:
                return tab
        return None
