def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(r) :
    area = str(3.14*r*r)
    return area
    

r = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
area = get_circle_area(r)
r = str(r)
result = "3.14 x " + r + " x " + r + " = " + area
print("반지름 " + r + "인 원의 넓이 = " + result)