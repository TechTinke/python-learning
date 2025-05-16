#DECORATOR FUNCTIONS  
def prepare(func, food):
    def preheat():
       print("Oven is at 40 degrees")
       func(food)
    return preheat
class Sufuria():
    def __init__(self):
        self.color = "Silver"
        self.material = "Aluminium"
        print("Initialized")
    
    def cook(self, food):
     print(f"{food} is ready")

sufuria1 = Sufuria()

prepare()
prepared_cook = prepare(sufuria1.cook, "Chicken")
print(prepared_cook)
prepared_cook()

    