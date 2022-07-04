import pandas as pd

Hanoi_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Hanoi.csv"
HCM_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\HoChiMinh.csv"
Dalat_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Dalat.csv"
Danang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Danang.csv"
Nhatrang_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Nhatrang.csv"
Phuquoc_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Phuquoc.csv"
Vungtau_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Vungtau.csv"
Quangninh_f = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Quangninh_again.csv"
Quangninh_f1 = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Halong.csv"

save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\All_data_traveloka.csv"

Hanoi_df = pd.read_csv(Hanoi_f)
# print(Hanoi_df)
HCM_df = pd.read_csv(HCM_f)
# print(HCM_df)
Dalat_df = pd.read_csv(Dalat_f)
# print(Dalat_df)
Danang_df = pd.read_csv(Danang_f)
# print(Danang_df)
Nhatrang_df = pd.read_csv(Nhatrang_f)
# print(Nhatrang_df)
Phuquoc_df = pd.read_csv(Phuquoc_f)
# print(Phuquoc_df)
Vungtau_df = pd.read_csv(Vungtau_f)
# print(Vungtau_df)
Quangninh_df = pd.read_csv(Quangninh_f)
# print(Quangninh_df)
Quangninh_df1 = pd.read_csv(Quangninh_f1)
# print(Quangninh_df1)

frames = [Hanoi_df, HCM_df, Dalat_df, Danang_df, Nhatrang_df,
          Phuquoc_df, Vungtau_df, Quangninh_df, Quangninh_df1]

data_res = pd.concat(frames)

data_res.to_csv(save_dir, index=False, encoding='utf8')

check_df = pd.read_csv(save_dir)
# print(check_df)
print("Tat ca so ban ghi la: " + str(len(check_df)))
print(check_df.info())
