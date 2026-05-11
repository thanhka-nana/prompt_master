# notepad_clone/model/cai_dat_model.py
from ..co_so_du_lieu.cai_dat_dao import CaiDatDAO
from ..cau_hinh import THEME_MAC_DINH

class CaiDatModel:
    def __init__(self):
        self.dao = CaiDatDAO()
        self._cache = {}

    def lay(self, khoa, mac_dinh=None):
        if khoa not in self._cache:
            self._cache[khoa] = self.dao.lay_gia_tri(khoa, mac_dinh)
        return self._cache[khoa]

    def luu(self, khoa, gia_tri):
        self._cache[khoa] = gia_tri
        self.dao.luu_gia_tri(khoa, gia_tri)

    def lay_theme(self):
        return self.lay("theme", THEME_MAC_DINH)
