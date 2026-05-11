# notepad_clone/controller/xu_ly_cong_cu.py


class XuLyCongCu:
    """Xử lý sự kiện click trên thanh snippet toolbar."""

    def __init__(self, view):
        self.view = view

    def chen_snippet(self, van_ban):
        """Chèn nội dung snippet vào vị trí con trỏ của tab đang active."""
        tid, tab_view = self.view.notebook.lay_tab_active()
        if tab_view:
            tab_view.text_area.insert("insert", van_ban)
            tab_view.text_area.focus_set()
