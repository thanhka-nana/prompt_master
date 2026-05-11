# notepad_clone/co_so_du_lieu/snippet_dao.py
from .ket_noi import KetNoiCSDL

class SnippetDAO:
    def __init__(self):
        self.conn = KetNoiCSDL().lay_ket_noi()

    def lay_tat_ca(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, ten_nut, van_ban_chen, la_tag FROM snippets")
        return cursor.fetchall()

    def them(self, ten, van_ban, la_tag=1):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO snippets (ten_nut, van_ban_chen, la_tag) VALUES (?, ?, ?)",
            (ten, van_ban, la_tag)
        )
        self.conn.commit()
        return cursor.lastrowid

    def xoa(self, snippet_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM snippets WHERE id=?", (snippet_id,))
        self.conn.commit()
