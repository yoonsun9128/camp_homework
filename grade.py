
def test(a):
    if a > 90 and a <= 100:
        return "A"
    elif a > 80 and a < 91:
        return "B"
    elif a > 70 and a < 81:
        return "C"
    else:
        return "F"

a = int(input())
grade = test(a)
print(grade)
