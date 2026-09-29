# Nhập giá trị 3 sản phẩm
X = float(input("nhập tổng tiền hóa đơn x"))
Y = float(input("Nhập phần trăm tip Y: "))
N = int(input("Nhập số người N: "))

# Tính tiền tip
tip = X * Y / 100

# Tổng tiền sau khi tip
total = X + tip

# Số tiền mỗi người phải trả
money_per_person = round(total / N)

# In kết quả
print("Số tiền mỗi người phải trả:", money_per_person)
