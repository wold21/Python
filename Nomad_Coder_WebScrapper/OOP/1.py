# # 5. inherit, override
# class Car():
#     def __init__(self, **kwargs):
#         self.wheels = 4
#         self.doors = 4
#         self.windows = 4
#         self.seat = 4
#         self.color = kwargs.get("color", "black")
#         self.price = kwargs.get("price", "$20")
#
#     def __str__(self):
#         return f"Car with{self.wheels} wheels"
#
#
# class Convartable_Car(Car):
#
#     # __init__ 재정의
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.time = kwargs.get("time", 10)
#
#
#     def take_off(self):
#         return "take off"
#
#     # __str__ 재정의
#     def __str__(self):
#         return f"Car with no roof"
#
# class Something(Convartable_Car):
#     pass
#
#
# porche = Convartable_Car(color="green", price="$40")
# porche.take_off()
# porche.wheels
# print(porche.color)



# # 4.dir(Class), __init__, __str__
# class Car():
#     def __init__(self, **kwargs):
#         self.wheels = 4
#         self.doors = 4
#         self.windows = 4
#         self.seat = 4
#         self.color = kwargs.get("color", "black")
#         self.price = kwargs.get("price", "$20")
#
#     # 자동으로 실행되는 메서드들이 있다.
#     def __str__(self):
#         return f"Car with{self.wheels} wheels"
#
#
# # print(dir(Car))
# porche = Car(color="green", price="$40")
# print(porche.color, porche.price)
#
# mini = Car()
# print(mini.color, mini.price)


# # 3. self
# class Car():
#     wheels = 4
#     doors = 4
#     windows = 4
#     seat = 4
#     def start(self):
#         print(self.doors)
#         print(self.color)
#         print("I Started")
#     # 파이썬의 모든 함수는 하나의 인자와 함께 사용함.
#     # self
#     # 메소드를 호출하는 인스턴스이다.
#
# porche = Car()
# porche.color = "Red is Red"
# porche.start()
# # print(dir(Car))


# # 2. Func, Method
# # 여기의 def는 Method
# class Start():
#     def start(self):
#         pass
# # Class 바깥의 def는 Func
# def start_():
#     pass


# # 1.
# class Car():
#     wheels = 4
#     doors = 4
#     windows = 4
#     seat = 4
# # Car의 인스턴스 porche
# porche = Car()
# porche.color = "Red"
#
# # Car의 인스턴스 ferrari
# ferrari = Car()
# ferrari.color = "Yellow"