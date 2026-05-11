# notepad_clone/model/quan_ly_tab.py
from ..co_so_du_lieu.tab_dao import TabDAO
from .tab_model import TabModel

class QuanLyTab:
    def __init__(self):
        self.dao = TabDAO()
        self.danh_sach_tab = []
        self._load_tu_db()

    def _load_tu_db(self):
        records = self.dao.lay_tat_ca_tab()
        for r in records:
            tab = TabModel(r[0], r[1], r[2], r[3], r[4])
            self.danh_sach_tab.append(tab)

    def tao_tab_moi(self, tieu_de="Untitled"):
        tab_id = self.dao.them_tab(tieu_de)
        moi = TabModel(tab_id, tieu_de)
        self.danh_sach_tab.append(moi)
        return moi

    def xoa_tab(self, tab_id):
        self.dao.xoa_tab(tab_id)
        self.danh_sach_tab = [t for t in self.danh_sach_tab if t.id != tab_id]

    def luu_tab(self, tab_id, noi_dung, con_tro, cuon):
        for tab in self.danh_sach_tab:
            if tab.id == tab_id:
                tab.cap_nhat(noi_dung, con_tro, cuon)
                self.dao.cap_nhat_tab(tab_id, noi_dung, con_tro=con_tro, cuon=cuon)
                break
