full_name  = input("nhập họ tên đầy đủ: ")
year = input("nhập năm sinh: ")
name = full_name.split()[-1]
name_code = name[0:3].upper()
discount_code = name_code + "-" + year + "-VIP"
print("mã ưu đãi:", discount_code)
