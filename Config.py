name = ""
labels = ['TrinhDo', 'ChuyenNganh']
# full_labels = ['GioiTinh', 'NamSinh', 'ThangSinh', 'NgaySinh', 'DangVien', 'TrinhDo', 'ChuyenNganh', 'NamCongTac']
full_labels = ['thoi_tiet', 'csphat_olt', 'csthu_olt', 'csphat_tbc', 'csthu_tbc', 'sh_download', 'sh_upload', 'kc_tb',
               'model']

data_link = f"./Dataset/{name}Data.csv"
data_label_link = f"./Dataset/{name}Label.json"
model_link = f"./Dataset/{name}Model.sav"
tuongquan_link = f"./Dataset/{name}TuongQuan.json"
className = 'ChucVu'

labels_name = {'GioiTinh': "Giới tính", 'NamSinh': "Năm sinh", 'ThangSinh': "Tháng sinh", 'NgaySinh': "Ngày sinh",
               'DangVien': "Đảng viên", 'TrinhDo': "Trình độ học vấn", 'ChuyenNganh': "Chuyên ngành",
               'NamCongTac': "Năm công tác"}
