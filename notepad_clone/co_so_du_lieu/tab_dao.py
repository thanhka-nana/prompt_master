# notepad_clone/co_so_du_lieu/tab_dao.py
from .ket_noi import KetNoiCSDL

class TabDAO:
    def __init__(self):
        self.conn = KetNoiCSDL().lay_ket_noi()

    def lay_tat_ca_tab(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, tieu_de, noi_dung, vi_tri_con_tro, ty_le_cuon FROM tabs ORDER BY id")
        return cursor.fetchall()

    def them_tab(self, tieu_de="Untitled", noi_dung=""):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO tabs (tieu_de, noi_dung) VALUES (?, ?)",
            (tieu_de, noi_dung)
        )
        self.conn.commit()
        return cursor.lastrowid

    def cap_nhat_tab(self, tab_id, noi_dung, tieu_de=None, con_tro="1.0", cuon=0.0):
        cursor = self.conn.cursor()
        if tieu_de:
            cursor.execute(
                "UPDATE tabs SET noi_dung=?, tieu_de=?, vi_tri_con_tro=?, ty_le_cuon=?, ngay_cap_nhat=CURRENT_TIMESTAMP WHERE id=?",
                (noi_dung, tieu_de, con_tro, cuon, tab_id)
            )
        else:
            cursor.execute(
                "UPDATE tabs SET noi_dung=?, vi_tri_con_tro=?, ty_le_cuon=?, ngay_cap_nhat=CURRENT_TIMESTAMP WHERE id=?",
                (noi_dung, con_tro, cuon, tab_id)
            )
        self.conn.commit()

    def xoa_tab(self, tab_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tabs WHERE id=?", (tab_id,))
        self.conn.commit()
