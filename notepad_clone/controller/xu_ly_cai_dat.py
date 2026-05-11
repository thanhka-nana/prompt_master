# notepad_clone/controller/xu_ly_cai_dat.py
from ..view.popup_cai_dat import PopupCaiDat

class XuLyCaiDat:
    def __init__(self, view, model_snippet):
        self.view = view
        self.model_snippet = model_snippet

    def hien_thi_cai_dat(self):
        callbacks = {
            "them_snippet": self._them_snippet
        }
        PopupCaiDat(self.view, callbacks)

    def _them_snippet(self, ten, noi_dung):
        self.model_snippet.them_snippet(ten, noi_dung)
        # Cập nhật toolbar ngay lập tức
        self.view.toolbar.hien_thi_snippets(self.model_snippet.danh_sach)
