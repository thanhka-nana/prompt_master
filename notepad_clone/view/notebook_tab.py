# notepad_clone/view/notebook_tab.py
from tkinter import ttk
from .tab_soan_thao import TabSoanThao

class NotebookTab(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.tabs_dict = {} # tab_id: TabSoanThao instance

    def them_tab(self, tab_model):
        frame = TabSoanThao(self, tab_model)
        self.add(frame, text=tab_model.tieu_de)
        self.tabs_dict[tab_model.id] = frame
        self.select(frame)
        return frame

    def lay_tab_active(self):
        current = self.select()
        if not current: return None
        for tid, frame in self.tabs_dict.items():
            if str(frame) == current:
                return tid, frame
        return None, None

    def dong_tab_hien_tai(self):
        tid, frame = self.lay_tab_active()
        if tid:
            self.forget(frame)
            del self.tabs_dict[tid]
            return tid
        return None
