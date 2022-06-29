import pandas as pd
import numpy as np
# file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\data_url\\chuaCheck\\HoChiMinh_list_1.txt"
# file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\raw_data_01\\QuangNinh_list.txt"
file_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Quangninh.csv"
save_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\detail_data\\data_again\\Quangninh_again.csv"

# # Check trung nhau
# lines_seen = set()  # holds lines already seen

# with open(file_dir, "r+") as f:
#     d = f.readlines()
#     f.seek(0)
#     for i in d:
#         if i not in lines_seen:
#             f.write(i)
#             lines_seen.add(i)
#     f.truncate()

#Replace data
df = pd.read_csv(file_dir)
#print(df)
print("\n--------------------\n")
m = df.replace("Quảng Ninh", "Hạ Long")
#print(m)
m.to_csv(save_dir, index=False, encoding='utf8')
k = pd.read_csv(save_dir)
print(k)


# check_dir = "E:\\STUDY\\UNIVERSITY\\Sem_20212\\Tich_hop_du_lieu\\BTL\\crawl_data\\crawl_traveloka\\QuangNinh_list.csv"

# k = pd.read_csv(check_dir)
# m = k["Description"][6]
# print(m)
# print(type(m))
# print(len(m))
# print("\n------------------\n")
# l = k["Description"].value_counts()['[]']
# print(l)
# print("percent: "+str(l/len(k)*100))
