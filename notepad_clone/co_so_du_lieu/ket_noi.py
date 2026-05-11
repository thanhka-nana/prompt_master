# notepad_clone/co_so_du_lieu/ket_noi.py
import sqlite3
from ..cau_hinh import DB_PATH

class KetNoiCSDL:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KetNoiCSDL, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect(DB_PATH, check_same_thread=False)
            cls._instance._khoi_tao_schema()
        return cls._instance

    def _khoi_tao_schema(self):
        cursor = self.connection.cursor()
        
        # Bảng lưu các tab soạn thảo
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tabs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tieu_de TEXT DEFAULT 'Untitled',
                noi_dung TEXT DEFAULT '',
                vi_tri_con_tro TEXT DEFAULT '1.0',
                ty_le_cuon REAL DEFAULT 0.0,
                ngay_cap_nhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Bảng lưu snippets (nút chèn nhanh)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS snippets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ten_nut TEXT NOT NULL,
                van_ban_chen TEXT NOT NULL,
                la_tag INTEGER DEFAULT 1
            )
        ''')

        # Bảng lưu templates (cho menu Prompt/Gợi ý)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS templates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                the_loai TEXT NOT NULL,
                noi_dung TEXT NOT NULL
            )
        ''')

        # Bảng lưu cài đặt
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                khoa TEXT PRIMARY KEY,
                gia_tri TEXT
            )
        ''')
        
        self.connection.commit()

    def lay_ket_noi(self):
        return self.connection

def khoi_tao_csdl():
    return KetNoiCSDL()
