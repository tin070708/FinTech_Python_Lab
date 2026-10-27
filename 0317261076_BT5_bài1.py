# Khởi tạo
tuoi = 25
so_du = 0.0
tien_gui = 60_000_000.0
lai_suat = 0.10
tang_tien_gui = 0.08
muc_tieu = 10_000_000_000.0
nam = 0

print("=== BÁO CÁO TÍCH LŨY QUỸ HƯU TRÍ ===")
header = (f"{'Năm':<4} | {'Tuổi':<4} | {'Số tiền gửi mới':>17} | "
          f"{'Tiền lãi trong năm':>20} | {'Tổng tài sản cuối năm':>23}")
print(header)
print("-" * len(header))

while so_du < muc_tieu:
    nam += 1
    tien_lai = so_du * lai_suat                  # lãi trên số dư đầu kỳ
    so_du = so_du + tien_lai + tien_gui          # số dư cuối năm

    print(f"{nam:<4} | {tuoi:<4} | {tien_gui:>13,.0f} VNĐ | "
          f"{tien_lai:>16,.0f} VNĐ | {so_du:>19,.0f} VNĐ")

    tuoi_dat_muc_tieu = tuoi                     # lưu tuổi của năm vừa tính
    tien_gui *= (1 + tang_tien_gui)              # năm sau gửi nhiều hơn 8%
    tuoi += 1

print("-" * len(header))
print(f"Đạt mục tiêu sau {nam} năm tích lũy, vào năm {tuoi_dat_muc_tieu} tuổi.")
print(f"Tổng tài sản: {so_du:,.0f} VNĐ")
