# main.py - Điểm vào chương trình Notepad++ Style Master
import sys
import os

# Đảm bảo import package notepad_clone hoạt động
sys.path.insert(0, os.path.dirname(__file__))

from notepad_clone.co_so_du_lieu.ket_noi import khoi_tao_csdl
from notepad_clone.model.quan_ly_tab import QuanLyTab
from notepad_clone.model.snippet_model import QuanLySnippet
from notepad_clone.model.template_model import QuanLyTemplate
from notepad_clone.model.cai_dat_model import CaiDatModel
from notepad_clone.view.cua_so_chinh import CuaSoChinh
from notepad_clone.controller.xu_ly_menu import XuLyMenu
from notepad_clone.controller.xu_ly_cong_cu import XuLyCongCu
from notepad_clone.controller.quan_ly_luu_tu_dong import QuanLyLuuTuDong
from notepad_clone.controller.quan_ly_goi_y import QuanLyGoiY
from notepad_clone.controller.quan_ly_phien import QuanLyPhien
from notepad_clone.controller.xu_ly_cai_dat import XuLyCaiDat


def main():
    # Bước 1: Khởi tạo database và schema
    khoi_tao_csdl()

    # Bước 2: Tạo các model
    model_tab = QuanLyTab()
    model_snippet = QuanLySnippet()
    model_template = QuanLyTemplate()
    model_cai_dat = CaiDatModel()

    # Bước 3: Chuẩn bị controller tạm (cần view trước)
    xu_ly_cong_cu = None
    xu_ly_menu = None
    xu_ly_cai_dat_ctrl = None

    # Callback placeholder - sẽ được gán sau khi tạo controller
    def _moi():
        if xu_ly_menu:
            tab_view = xu_ly_menu.tao_tab_moi()
            _gan_cho_tab(tab_view)

    def _dong():
        if xu_ly_menu:
            xu_ly_menu.dong_tab()

    def _chen(text):
        if xu_ly_cong_cu:
            xu_ly_cong_cu.chen_snippet(text)

    def _luu_tmpl():
        if xu_ly_menu:
            xu_ly_menu.luu_template()

    def _cai_dat():
        if xu_ly_cai_dat_ctrl:
            xu_ly_cai_dat_ctrl.hien_thi_cai_dat()

    def _thoat():
        view.destroy()

    callbacks = {
        "moi": _moi,
        "dong": _dong,
        "chen_text": _chen,
        "luu_template": _luu_tmpl,
        "cai_dat": _cai_dat,
        "thoat": _thoat,
    }

    # Bước 4: Tạo view
    view = CuaSoChinh(callbacks)

    # Bước 5: Tạo controller chính thức
    xu_ly_cong_cu = XuLyCongCu(view)
    xu_ly_menu = XuLyMenu(view, model_tab, model_snippet, model_template)
    xu_ly_cai_dat_ctrl = XuLyCaiDat(view, model_snippet)
    goi_y = QuanLyGoiY(view, model_template)
    phien = QuanLyPhien(model_cai_dat, model_tab)

    # Bước 6: Khôi phục phiên trước đó (hoặc tạo tab mặc định)
    ds_tab_view = phien.khoi_phuc_phien(view.notebook)

    # Hàm gắn auto-save + gợi ý cho một tab
    def _gan_cho_tab(tab_view):
        luu_tu_dong._gan_debounce_cho_tab(tab_view)
        goi_y.thiet_lap_cho_tab(tab_view)

    # Bước 7: Tạo auto-save controller (sau khi đã có tab)
    luu_tu_dong = QuanLyLuuTuDong(view, model_tab, phien)

    # Gắn auto-save + gợi ý cho tất cả tab đã khôi phục
    for tab_view in ds_tab_view:
        _gan_cho_tab(tab_view)

    # Bước 8: Load dữ liệu ban đầu cho toolbar và menu
    view.toolbar.hien_thi_snippets(model_snippet.danh_sach)
    view.menu_bar.cap_nhat_templates(
        [t[2] for t in model_template.danh_sach]
    )

    # Bind sự kiện khi tạo tab mới (để gắn auto-save + gợi ý)
    view.bind("<<TabMoiDuocTao>>", lambda e: None)

    # Bước 9: Chạy vòng lặp chính
    view.mainloop()


if __name__ == "__main__":
    main()
