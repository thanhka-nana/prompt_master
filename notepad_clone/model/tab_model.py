# notepad_clone/model/tab_model.py

class TabModel:
    def __init__(self, tab_id, tieu_de, noi_dung="", con_tro="1.0", cuon=0.0):
        self.id = tab_id
        self.tieu_de = tieu_de
        self.noi_dung = noi_dung
        self.vi_tri_con_tro = con_tro
        self.ty_le_cuon = cuon
        self.da_thay_doi = False

    def cap_nhat(self, noi_dung, con_tro="1.0", cuon=0.0):
        if self.noi_dung != noi_dung:
            self.noi_dung = noi_dung
            self.da_thay_doi = True
        self.vi_tri_con_tro = con_tro
        self.ty_le_cuon = cuon
