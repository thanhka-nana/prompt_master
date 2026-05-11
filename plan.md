```markdown
# KẾ HOẠCH PHÁT TRIỂN ỨNG DỤNG NOTEPAD++ STYLE (PYTHON + TKINTER)

## 1. TỔNG QUAN DỰ ÁN
- Ứng dụng soạn thảo văn bản với giao diện giống Notepad++.
- Giao diện: tkinter + ttk, sử dụng theme `sv-ttk` (Sun Valley) để có giao diện hiện đại.
- Kiến trúc: Model-View-Controller (MVC) để dễ bảo trì, mở rộng.
- Môi trường: PyCharm 2024+, Python 3.11, SQLite3. Thư viện bổ trợ: `sv-ttk`.
- Tiêu chuẩn code: PEP 8, comment tiếng Việt, file ≤ 100 dòng (View có thể linh động ≤ 130 dòng), tên file không dấu, phân cách gạch dưới.
- Tính năng chính:
  + Soạn thảo đa tab.
  + Menu Prompt (template chèn nhanh).
  + Thanh Snippet (tag kèm text).
  + Auto-save thông minh (debounce 2 giây + lưu khi chuyển tab/đóng app).
  + Gợi ý tự động (kích hoạt bởi `/` hoặc `@`).
  + Cài đặt linh hoạt (font, theme, quản lý snippet).
  + Khôi phục phiên làm việc trước đó (bao gồm danh sách tab, vị trí con trỏ và trạng thái cuộn).

## 2. CẤU TRÚC THƯ MỤC & FILE
```
notepad_clone/
│
├── main.py                         # Điểm vào chương trình, khởi tạo Model, View, Controller
├── cau_hinh.py                     # Hằng số cấu hình (đường dẫn DB, kích thước, font, theme)
│
├── co_so_du_lieu/                  # Tầng truy xuất dữ liệu (Data Access Object)
│   ├── __init__.py
│   ├── ket_noi.py                  # Tạo/mở kết nối SQLite, khởi tạo schema
│   ├── tab_dao.py                  # CRUD cho bảng tabs
│   ├── snippet_dao.py              # CRUD cho bảng snippets
│   ├── template_dao.py             # CRUD cho bảng templates
│   └── cai_dat_dao.py              # Đọc/ghi bảng settings (theme, font...)
│
├── model/                          # Tầng dữ liệu nghiệp vụ
│   ├── __init__.py
│   ├── tab_model.py                # Dữ liệu của một tab (id, tiêu đề, nội dung)
│   ├── quan_ly_tab.py              # Quản lý danh sách tab, load/save vào DB
│   ├── snippet_model.py            # Quản lý danh sách snippet
│   ├── template_model.py           # Quản lý danh sách template, phân loại
│   └── cai_dat_model.py            # Đọc/ghi cấu hình từ DB vào cache
│
├── view/                           # Tầng giao diện (chỉ vẽ và bind)
│   ├── __init__.py
│   ├── cua_so_chinh.py             # JFrame/MainWindow chứa Menu, Toolbar, Notebook, Status
│   ├── thanh_menu.py                # Tạo menu bar (File, Prompt, Cài đặt)
│   ├── thanh_cong_cu.py            # Thanh snippet với các nút bấm
│   ├── notebook_tab.py             # Notebook quản lý các tab soạn thảo
│   ├── tab_soan_thao.py            # Widget Text + Scrollbar + binding sự kiện
│   ├── thanh_trang_thai.py         # Thanh trạng thái dưới cùng
│   ├── popup_goi_y.py              # Popup danh sách gợi ý (Listbox)
│   └── popup_cai_dat.py            # Cửa sổ cài đặt (Toplevel)
│
├── controller/                     # Tầng điều khiển (xử lý sự kiện, logic)
│   ├── __init__.py
│   ├── xu_ly_menu.py               # Xử lý sự kiện từ menu chính
│   ├── xu_ly_cong_cu.py            # Xử lý nút bấm trên thanh snippet
│   ├── quan_ly_luu_tu_dong.py      # Debounce + auto-save vào SQLite
│   ├── quan_ly_goi_y.py            # Logic bắt phím kích hoạt, lọc và hiển thị gợi ý
│   ├── quan_ly_phien.py            # Lưu/khôi phục các tab đang mở khi đóng/mở app
│   └── xu_ly_cai_dat.py            # Xử lý lưu cài đặt từ popup vào model
│
└── tien_ich/                       # Tiện ích chung
    ├── __init__.py
    └── debounce.py                 # Hàm trì hoãn gọi hàm bằng after_id

```

## 3. MÔ TẢ CHI TIẾT TỪNG FILE (≤ 100 DÒNG/FILE)

### 3.1. main.py
- Khởi tạo kết nối database (gọi `ket_noi.khoi_tao_csdl`).
- Tạo instance `QuanLyTab` (model).
- Tạo instance `CuaSoChinh` (view).
- Tạo các controller cần thiết và gắn vào view.
- Chạy vòng lặp `mainloop()`.

### 3.2. cau_hinh.py
- Hằng số: `DB_PATH`, `FONT_MAC_DINH`, `CO_FONT`, `THEME_SANG`, `THEME_TOI`, `THOI_GIAN_DEBOUNCE = 2000`.
- Không chứa hàm, chỉ khai báo biến toàn cục dùng chung.

### 3.3. co_so_du_lieu/
- **ket_noi.py**: Tạo kết nối SQLite, tạo bảng TABS, SNIPPETS, TEMPLATES, SETTINGS nếu chưa tồn tại.
- **tab_dao.py**: Các hàm `lay_tat_ca_tab()`, `them_tab(tieu_de, noi_dung)`, `cap_nhat_tab(id, noi_dung, tieu_de, vi_tri_con_tro, ty_le_cuon)`, `xoa_tab(id)`.
- **snippet_dao.py**: CRUD tương tự cho snippets.
- **template_dao.py**: CRUD cho templates (có trường `category`).
- **cai_dat_dao.py**: Hàm `lay_cai_dat(key)`, `dat_cai_dat(key, gia_tri)`.

### 3.4. model/
- **tab_model.py**: Lớp `Tab` với thuộc tính `id`, `tieu_de`, `noi_dung`, `ngay_cap_nhat`. 
- **quan_ly_tab.py**: Lớp `QuanLyTab` chứa danh sách `Tab`, quản lý thêm/xóa, tự động load từ DB khi khởi tạo. Gọi DAO để đồng bộ.
- **snippet_model.py**: Lớp `QuanLySnippet` tương tự.
- **template_model.py**: Lớp `QuanLyTemplate` tương tự, có thêm phương thức lọc theo category.
- **cai_dat_model.py**: Lớp `CaiDatModel` đọc/ghi cache settings, cập nhật DB.

### 3.5. view/
- **cua_so_chinh.py**: Kế thừa `tk.Tk`. Tạo `ThanhMenu`, `ThanhCongCu`, `NotebookTab`, `ThanhTrangThai`. Cung cấp phương thức lấy notebook để controller thao tác.
- **thanh_menu.py**: Kế thừa `tk.Menu`, tạo các menu Prompt, Cài đặt. Menu Prompt động thêm “Lưu template mới”. Gửi sự kiện cho controller qua callback.
- **thanh_cong_cu.py**: Là `ttk.Frame`, chứa các nút snippet. Các nút được tạo động từ danh sách snippet. Khi click, gọi callback `khi_click_snippet(ten_nut, van_ban)`.
- **notebook_tab.py**: `ttk.Notebook`, có phương thức `them_tab()`, `dong_tab()`, `lay_tab_hien_tai()`.
- **tab_soan_thao.py**: `ttk.Frame` chứa `tk.Text` + `tk.Scrollbar`. Bind `<KeyRelease>` để trigger auto-save và gợi ý. Bind `<FocusIn>` để cập nhật thanh trạng thái. Có phương thức `lay_noi_dung()`, `cap_nhat_noi_dung(text)`.
- **thanh_trang_thai.py**: `ttk.Label` hiển thị thông tin (đã lưu lúc, số ký tự).
- **popup_goi_y.py**: `tk.Toplevel` với `tk.Listbox`. Hiển thị danh sách gợi ý, tự hủy khi mất focus.
- **popup_cai_dat.py**: Cửa sổ cài đặt, chứa các tab con: Snippets (thêm/xóa/sửa), Giao diện (font, theme). Tương tác qua controller.

### 3.6. controller/
- **xu_ly_menu.py**: Lớp `XuLyMenu`, nhận instance của `CuaSoChinh` và `QuanLyTab`. Xử lý: mở tab mới, lưu, lưu template, chèn template vào tab hiện tại.
- **xu_ly_cong_cu.py**: Lớp `XuLyCongCu`, gắn với `ThanhCongCu`. Khi nhận sự kiện click, lấy nội dung snippet và chèn vào vị trí con trỏ của tab đang active.
- **quan_ly_luu_tu_dong.py**: Lớp `QuanLyLuuTuDong`:
  + Giữ tham chiếu đến `QuanLyTab` và `NotebookTab`.
  + Đăng ký sự kiện `<KeyRelease>` trên mỗi tab: gọi `debounce.debounce(self._luu_tab_hien_tai, THOI_GIAN_DEBOUNCE)`.
  + `_luu_tab_hien_tai()`: lấy nội dung từ widget, cập nhật model và gọi DAO.
  + Bind `<<NotebookTabChanged>>` để lưu tab cũ khi chuyển.
  + Bind `WM_DELETE_WINDOW` để lưu toàn bộ và đóng.
- **quan_ly_goi_y.py**: Lớp `QuanLyGoiY`:
  + Theo dõi sự kiện `<KeyRelease>` trên Text.
  + Kiểm tra ký tự trước con trỏ có phải `/` hoặc `@` không.
  + Nếu có, tạo popup `PopupGoiY`, gửi danh sách template phù hợp.
  + Xử lý chọn (Enter, click): xóa ký tự kích hoạt, chèn template vào vị trí hiện tại.
  + Hủy popup khi không còn ký tự kích hoạt.
- **quan_ly_phien.py**: Lưu danh sách tab đang mở (id) vào DB hoặc file JSON khi thoát, khôi phục khi khởi động.
- **xu_ly_cai_dat.py**: Lớp `XuLyCaiDat` kết nối popup với model `CaiDatModel`, `QuanLySnippet`. Khi lưu, cập nhật DB và refresh giao diện.

### 3.7. tien_ich/debounce.py
- Hàm `debounce(func, delay)` trả về wrapper. Dùng `after_id` để hủy lịch cũ. Ví dụ:
```python
# Logic debounce sử dụng after() của Tkinter để không chặn main loop
def debounce(widget, func, delay):
    after_id = None
    def wrapper(*args, **kwargs):
        nonlocal after_id
        if after_id:
            widget.after_cancel(after_id)
        after_id = widget.after(delay, lambda: func(*args, **kwargs))
    return wrapper
```

## 4. CƠ SỞ DỮ LIỆU (SQLITE3)
```sql
CREATE TABLE IF NOT EXISTS tabs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tieu_de TEXT DEFAULT 'Untitled',
    noi_dung TEXT DEFAULT '',
    vi_tri_con_tro TEXT DEFAULT '1.0',
    ty_le_cuon REAL DEFAULT 0.0,
    ngay_cap_nhat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS snippets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_nut TEXT NOT NULL,
    van_ban_chen TEXT NOT NULL,
    la_tag INTEGER DEFAULT 1   -- 1: tag (nút), 0: hiển thị chuỗi và có thể sửa trực tiếp
);

CREATE TABLE IF NOT EXISTS templates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    the_loai TEXT NOT NULL,    -- 'Hình ảnh', 'Code', ...
    noi_dung TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS settings (
    khoa TEXT PRIMARY KEY,
    gia_tri TEXT
);
```

## 5. LUỒNG HOẠT ĐỘNG CHÍNH
1. **Khởi động**:
   - `ket_noi.khoi_tao_csdl()`.
   - `QuanLyTab` load tất cả tab từ DB → tạo widget tương ứng trong `NotebookTab`.
   - `QuanLyPhien` khôi phục tab đang mở trước đó (nếu có).
   - Gắn controller auto-save, gợi ý vào từng tab.
2. **Người dùng gõ phím**:
   - `Text` widget kích hoạt `<KeyRelease>`.
   - `QuanLyLuuTuDong` nhận sự kiện, debounce 2 giây → lưu tab vào model và DB.
   - `QuanLyGoiY` kiểm tra ký tự kích hoạt, hiển thị popup nếu cần.
3. **Chuyển tab**:
   - Lưu tab cũ ngay lập tức.
   - Cập nhật thanh trạng thái (số ký tự, trạng thái lưu).
4. **Click snippet trên toolbar**:
   - `XuLyCongCu` lấy text từ model snippet, chèn vào vị trí con trỏ của tab hiện tại.
5. **Chọn template từ menu Prompt**:
   - `XuLyMenu` chèn nội dung template vào tab active.
6. **Đóng ứng dụng**:
   - `QuanLyLuuTuDong` lưu tất cả tab.
   - `QuanLyPhien` lưu danh sách tab đang mở.
   - Hủy cửa sổ.

## 6. TIÊU CHUẨN CODE VÀ COMMENT
- **PEP 8**: Dùng `snake_case` cho biến/hàm, `CamelCase` cho lớp, 4 spaces thụt lề.
- **Comment bằng tiếng Việt**: Chỉ giải thích "tại sao" làm như vậy, không miêu tả code.
- **Ví dụ**:
  ```python
  # Sử dụng after_id để hủy lịch cũ tránh chồng lấn timer
  self._after_id = self.after(2000, self._luu)
  ```
- **Giới hạn dòng**: Mỗi file chỉ chứa 1 lớp chính. Model, Controller, DAO giữ nghiêm ngặt ≤ 100 dòng. Các file View có thể linh động tối đa 130 dòng để đảm bảo khai báo giao diện đầy đủ mà vẫn tách biệt logic.

## 7. PHÂN CÔNG PHÁT TRIỂN (THEO BƯỚC)
1. **Bước 1**: Tạo cấu trúc thư mục, `__init__.py`, file `cau_hinh.py`.
2. **Bước 2**: Xây dựng `co_so_du_lieu/ket_noi.py` và các DAO.
3. **Bước 3**: Viết `model` (Tab, Snippet, Template) và các lớp quản lý.
4. **Bước 4**: Dựng giao diện cơ bản: `CuaSoChinh` + `NotebookTab` + `TabSoanThao`.
5. **Bước 5**: Tích hợp Menu và Toolbar (`thanh_menu`, `thanh_cong_cu`).
6. **Bước 6**: Thêm controller `XuLyMenu`, `XuLyCongCu` để chèn nội dung.
7. **Bước 7**: Hoàn thiện auto-save với `QuanLyLuuTuDong` và `debounce`.
8. **Bước 8**: Phát triển gợi ý tự động `QuanLyGoiY` + `PopupGoiY`.
9. **Bước 9**: Cài đặt, quản lý phiên, thanh trạng thái.
10. **Bước 10**: Kiểm tra và tối ưu, đảm bảo mỗi file không quá 100 dòng.

## 8. LƯU Ý KỸ THUẬT QUAN TRỌNG
- **Debounce**: Khi gõ liên tục, timer cũ bị hủy, chỉ khi dừng 2s mới gọi lưu DB. Điều này giảm tải I/O đáng kể.
- **Auto-save khi mất focus tab**: Đảm bảo không mất dữ liệu khi chuyển tab.
- **Popup gợi ý**: Tính toán vị trí dựa trên `bbox("insert")` để hiển thị đúng chỗ.
- **Khôi phục phiên**: Lưu mảng id tab vào settings dạng JSON, khi mở lại load tuần tự.
- **Snippet dạng tag hay text**: Nếu `la_tag = 1`, nút chỉ hiển thị tên ngắn, không cho sửa. Nếu `0`, thanh toolbar hiện luôn văn bản và có thể sửa trực tiếp (cần bind double-click để chỉnh sửa).

Với kế hoạch chi tiết này, bạn có thể bắt đầu lập trình từng bước một cách khoa học, đảm bảo mã nguồn sạch sẽ, dễ bảo trì và mở rộng.
```