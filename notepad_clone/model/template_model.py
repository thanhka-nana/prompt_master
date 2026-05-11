# notepad_clone/model/template_model.py
from ..co_so_du_lieu.template_dao import TemplateDAO

class QuanLyTemplate:
    def __init__(self):
        self.dao = TemplateDAO()
        self.danh_sach = self.dao.lay_tat_ca()

    def lay_theo_the_loai(self):
        kq = {}
        for _, cat, content in self.danh_sach:
            if cat not in kq: kq[cat] = []
            kq[cat].append(content)
        return kq

    def them_template(self, cat, content):
        self.dao.them(cat, content)
        self.danh_sach = self.dao.lay_tat_ca()
