# notepad_clone/model/snippet_model.py
from ..co_so_du_lieu.snippet_dao import SnippetDAO

class QuanLySnippet:
    def __init__(self):
        self.dao = SnippetDAO()
        self.danh_sach = self.dao.lay_tat_ca()

    def lam_moi(self):
        self.danh_sach = self.dao.lay_tat_ca()

    def them_snippet(self, ten, van_ban):
        self.dao.them(ten, van_ban)
        self.lam_moi()
