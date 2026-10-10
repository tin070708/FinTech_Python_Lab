ma_giao_dich = "GD001-5000000-VND"
so_tien = int(ma_giao_dich[6:13])
if so_tien >= 5000000:
   print("Giao dịch cần xác thực OTP")
else:
   print("Giao dịch thành công")
