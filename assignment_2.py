class person:
        def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age

        def greet(self):
            if age >= 20:
                print(f"안녕하세요 {self.name} 성인이시군요!")

            else:
                 print(f"안녕하세요 {self.name} 성인이 아니시군요!")


    
        def disply(self):
                print(f'이름 : {self.name}, 성별 : {self.gender}')  # 한 칸 띄우게 출력 
                print(f'나이 : {self.age}')
                return self.greet()
        
name = str(input("이름을 입력하세요 : "))
while(True):
        try:
            gender = str(input("성별을 입력하세요 (male/female) : "))          
            if gender.lower() not in ["male", "female"]:
                raise ValueError 
            break
        except ValueError:
            print("male이나 female을 입력하세요.")
age = int(input("나이를 입력하세요 : "))
Person = person(name,gender,age)
Person.disply()