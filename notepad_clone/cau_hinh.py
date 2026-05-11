# notepad_clone/cau_hinh.py
import os

# Đường dẫn database
DB_PATH = os.path.join(os.path.dirname(__file__), "du_lieu.db")

# Cấu hình giao diện
TEN_UNG_DUNG = "Notepad++ Style Master"
KICH_THUOC_MAC_DINH = "1000x700"

# Font và màu sắc
FONT_MAC_DINH = ("Consolas", 12)
THEME_MAC_DINH = "dark"  # dark hoặc light

# Cấu hình auto-save
THOI_GIAN_DEBOUNCE = 2000  # ms
