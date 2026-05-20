n = int(input('Nhập số ngày: '))
count = 0
total_income = 0

for i in range (1, n+1):
    daily_income_input = float(input(f'Nhập doanh thu ngày {i}: '))
    
    total_income += daily_income_input

    if daily_income_input >= 5000000:
        count += 1

average_income = total_income / n

print('--- Báo cáo doanh thu tuần ---')
print(f'Tổng doan thu cả tuần: {total_income}')
print(f'Doan thu trung bình mỗi ngày: {average_income}')
print(f'Số ngày đạt doanh thu mục tiêu (>= 5000000 VND): {count} ngày')
    
    