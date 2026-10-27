# Khai báo tham số
F = 1_000_000.0    # Mệnh giá
c = 0.09           # Lãi suất coupon 9%/năm
N = 10             # Thời hạn (năm)
y = 0.085          # YTM 8.5%/năm

# 1. Tiền lãi coupon hàng năm
C = F * c
print("=== ĐỊNH GIÁ TRÁI PHIẾU COUPON ===")
print(f"Mệnh giá F = {F:,.0f} VNĐ | Coupon = {c:.1%} | N = {N} năm | YTM = {y:.1%}")
print(f"Tiền lãi coupon hàng năm C = {C:,.0f} VNĐ\n")

# 2. PV từng khoản coupon
tong_pv_coupon = 0.0
header = f"{'Năm':<5} | {'Coupon':>15} | {'PV coupon':>17}"
print(header)
print("-" * len(header))

for t in range(1, N + 1):
    pv_c = C / ((1 + y) ** t)
    tong_pv_coupon += pv_c
    print(f"{t:<5} | {C:>11,.0f} VNĐ | {pv_c:>13,.0f} VNĐ")

print("-" * len(header))
print(f"Tổng PV coupon: {tong_pv_coupon:,.0f} VNĐ\n")

# 3. PV của mệnh giá nhận lại cuối năm N
pv_f = F / ((1 + y) ** N)
print(f"PV của mệnh giá (năm {N}): {pv_f:,.0f} VNĐ")

# 4. Giá lý thuyết và phân loại
gia_trai_phieu = tong_pv_coupon + pv_f
print(f"Giá lý thuyết P0: {gia_trai_phieu:,.0f} VNĐ")

if gia_trai_phieu > F:
    print("=> Trái phiếu bán CAO HƠN mệnh giá (Premium) vì coupon > YTM.")
elif gia_trai_phieu < F:
    print("=> Trái phiếu bán THẤP HƠN mệnh giá (Discount) vì coupon < YTM.")
else:
    print("=> Trái phiếu bán ĐÚNG mệnh giá (Par) vì coupon = YTM.")
