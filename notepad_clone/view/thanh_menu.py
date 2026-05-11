# notepad_clone/view/thanh_menu.py
import tkinter as tk

class ThanhMenu(tk.Menu):
    def __init__(self, parent, callbacks):
        super().__init__(parent)
        self.callbacks = callbacks # dict chứa các hàm callback
        self._khoi_tao_menu()

    def _khoi_tao_menu(self):
        # Menu File
        file_menu = tk.Menu(self, tearoff=0)
        file_menu.add_command(label="Tab mới (Ctrl+N)", command=self.callbacks.get("moi"))
        file_menu.add_command(label="Đóng tab (Ctrl+W)", command=self.callbacks.get("dong"))
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.callbacks.get("thoat"))
        self.add_cascade(label="File", menu=file_menu)

        # Menu Prompt
        self.prompt_menu = tk.Menu(self, tearoff=0)
        self.prompt_menu.add_command(label="Lưu thành template...", command=self.callbacks.get("luu_template"))
        self.prompt_menu.add_separator()
        # Các template sẽ được load động ở đây
        self.add_cascade(label="Prompt", menu=self.prompt_menu)

        # Menu Cài đặt
        setting_menu = tk.Menu(self, tearoff=0)
        setting_menu.add_command(label="Cấu hình...", command=self.callbacks.get("cai_dat"))
        self.add_cascade(label="Cài đặt", menu=setting_menu)

    def cap_nhat_templates(self, danh_sach_templates):
        # Xóa các item cũ sau separator
        # (Giả sử separator ở index 1)
        while self.prompt_menu.index("end") > 1:
            self.prompt_menu.delete("end")
        
        for item in danh_sach_templates:
            self.prompt_menu.add_command(
                label=item[:30] + "...", 
                command=lambda content=item: self.callbacks.get("chen_text")(content)
            )
