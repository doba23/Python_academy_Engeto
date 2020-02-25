#convert height 1' = 0.025 m'
def convert_height (inches: int):
    return inches * 0.025
#convert weight 1 lb = 0.45 kg
def convert_weight (pounds: int):
    return pounds * 0.45
#calculate BMI
def bmi (inches, pounds):
    return (convert_weight(pounds) / convert_height(inches))

print( bmi (160, 70))

