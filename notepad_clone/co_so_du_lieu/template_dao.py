# notepad_clone/co_so_du_lieu/template_dao.py
from .ket_noi import KetNoiCSDL

class TemplateDAO:
    def __init__(self):
        self.conn = KetNoiCSDL().lay_ket_noi()

    def lay_tat_ca(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, the_loai, noi_dung FROM templates")
        return cursor.fetchall()

    def them(self, the_loai, noi_dung):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO templates (the_loai, noi_dung) VALUES (?, ?)",
            (the_loai, noi_dung)
        )
        self.conn.commit()
        return cursor.lastrowid
