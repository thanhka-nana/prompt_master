# notepad_clone/controller/xu_ly_menu.py

class XuLyMenu:
    def __init__(self, view, model_tab, model_snippet, model_template):
        self.view = view
        self.model_tab = model_tab
        self.model_snippet = model_snippet
        self.model_template = model_template

    def tao_tab_moi(self):
        moi = self.model_tab.tao_tab_moi(f"Untitled {len(self.model_tab.danh_sach_tab) + 1}")
        tab_view = self.view.notebook.them_tab(moi)
        # Cần gắn auto-save cho tab mới này (sẽ xử lý ở main hoặc qua event)
        self.view.event_generate("<<TabMoiDuocTao>>")
        return tab_view

    def dong_tab(self):
        tid = self.view.notebook.dong_tab_hien_tai()
        if tid:
            self.model_tab.xoa_tab(tid)

    def chen_text(self, text):
        tid, tab_view = self.view.notebook.lay_tab_active()
        if tab_view:
            tab_view.text_area.insert("insert", text)

    def luu_template(self):
        tid, tab_view = self.view.notebook.lay_tab_active()
        if tab_view:
            # Lấy vùng text đang chọn, nếu không chọn thì lấy toàn bộ
            try:
                content = tab_view.text_area.get("sel.first", "sel.last")
            except:
                content = tab_view.text_area.get("1.0", "end-1c")
            
            if content.strip():
                self.model_template.them_template("Chung", content)
                self.view.menu_bar.cap_nhat_templates(
                    [t[2] for t in self.model_template.danh_sach]
                )
