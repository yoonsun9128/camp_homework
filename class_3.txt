from pprint import pprint
import profile

class introduce():
    def __init__(self):
        self.profile = {
            "name": "-",
            "gender": "-",
            "birthday": "-",
            "age": "-",
            "phone": "-",
            "email": "-",
        }
    def show(self,profile):
        self.profile = profile
    def get_name(self):
        return guest1.show["name"]
    def get_gender(self):
        return guest1.show["gender"]
    def get_birthday(self):
        return guest1.show["birthday"]
    def get_phone(self):
        return guest1.show["phone"]
    def get_email(self):
        return guest1.show["email"]
    def get_age(self):    
        return guest1.show["age"]
    

guest1 = introduce()
pprint(guest1.profile)
guest1.show = ({
    "name": "yoonsun",
    "gender": "women",
    "birthday": "5/20",
    "age": "28",
    "phone": "01096399128",
    "email": "bristol9128@naver.com",
    })
# print(guest1.show["name"])

print(guest1.get_name())
print(guest1.get_gender())
print(guest1.get_birthday())
print(guest1.get_age())
print(guest1.get_phone())
print(guest1.get_email())