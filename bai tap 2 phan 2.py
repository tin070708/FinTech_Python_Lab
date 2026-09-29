
# Nhập dữ liệu đầu vào từ người dùng
Initial_Investment = float ("nhập Tổng vốn ban đầu")
Final_Value = float("Tổng giá trị bán ra")
# Tính toán lợi nhuận ròng và ROI
net_profit = final_value - initial_investment
roi = (net_profit / initial_investment) * 100
# Hiển thị kết quả (làm tròn 2 chữ số thập phân)
print(f"Lợi nhuận ròng (Net Profit): {net_profit:,.2f}")
print(f"Tỷ lệ ROI: {roi:.2f}%")
