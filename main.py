import calc_bmi

print("BMI計算アプリ")
w = int(input("体重(kg):"))
h = int(input("身長(cm):"))
h = h / 100
print(f"{calc_bmi.bmi_calc(h, w)}")
