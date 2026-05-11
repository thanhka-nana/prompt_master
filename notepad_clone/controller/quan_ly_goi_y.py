# notepad_clone/controller/quan_ly_goi_y.py
from ..view.popup_goi_y import PopupGoiY

class QuanLyGoiY:
    def __init__(self, view, model_template):
        self.view = view
        self.model = model_template
        self.popup = None

    def thiet_lap_cho_tab(self, tab_view):
        tab_view.text_area.bind("<KeyRelease>", lambda e: self._kiem_tra_kich_hoat(tab_view, e), add="+")

    def _kiem_tra_kich_hoat(self, tab_view, event):
        if event.char in ["/", "@"]:
            self._hien_popup(tab_view)

    def _hien_popup(self, tab_view):
        # Lấy tọa độ con trỏ
        bbox = tab_view.text_area.bbox("insert")
        if not bbox: return
        
        x = tab_view.text_area.winfo_rootx() + bbox[0]
        y = tab_view.text_area.winfo_rooty() + bbox[1] + 20
        
        items = [t[2] for t in self.model.danh_sach]
        
        if self.popup: self.popup.destroy()
        self.popup = PopupGoiY(self.view, lambda c: self._chen_goi_y(tab_view, c))
        self.popup.hien_thi(items, x, y)

    def _chen_goi_y(self, tab_view, content):
        # Xóa ký tự kích hoạt vừa gõ (/ hoặc @)
        tab_view.text_area.delete("insert-1c", "insert")
        tab_view.text_area.insert("insert", content)
