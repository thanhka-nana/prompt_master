# notepad_clone/co_so_du_lieu/cai_dat_dao.py
from .ket_noi import KetNoiCSDL

class CaiDatDAO:
    def __init__(self):
        self.conn = KetNoiCSDL().lay_ket_noi()

    def lay_gia_tri(self, khoa, mac_dinh=None):
        cursor = self.conn.cursor()
        cursor.execute("SELECT gia_tri FROM settings WHERE khoa=?", (khoa,))
        row = cursor.fetchone()
        return row[0] if row else mac_dinh

    def luu_gia_tri(self, khoa, gia_tri):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO settings (khoa, gia_tri) VALUES (?, ?)",
            (khoa, str(gia_tri))
        )
        self.conn.commit()
