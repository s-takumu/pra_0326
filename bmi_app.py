import calc_bmi

print("BMI計算アプリ")
w = int(input("体重(kg):"))
h = int(input("身長(cm):"))
h = h / 100
for i in range(2):
    print(f"BMI:{calc_bmi.bmi_calc(h, w)}")
