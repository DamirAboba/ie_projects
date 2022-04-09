
#                                  --
from typing_extensions import ParamSpec


class IWrite:  #                     |
    def write(self):  #              |
        pass  #                      |
#                                    | -> Interface Segregation
#                                    |
class IRead:  #                      |
    def read(self):  #               |
        return  #                    |
#                                  --

class FileMaster(IWrite, IRead):  # Single Responsobility, Open Closed, Liskov Substitution, Encapsulation, Inheritence
    __last_written_file = ""
    _count_of_written_files = 0

    def write(self, file_name, to_write):
        with open(file_name, "w") as file:
            file.write(to_write)

        FileMaster._count_of_written_files += 1
        self.set_last_written_file(file_name)

    def read(self, file_name):
        with open(file_name, "r") as file:
            return file.read()

    def set_last_written_file(self, file_name):
        self.__last_written_file = file_name


class JsonMaster(FileMaster):  # Single Responsobility, Inheritence
    import json

    def write(self, file_name, to_write):
        with open(f"{file_name}.json", "w", encoding="utf-8") as file:
            self.json.dump(to_write, file, indent=4, ensure_ascii=False)

    def read(self, file_name):
        with open(f"{file_name}.json") as file:
            return self.json.loads(file.read())


print_key_and_value = lambda dict_: [print(f"{k}: {v}") for k, v in dict_.items()] # Lambda, List Comprehension |
print_all_keys = lambda dict_: print(", ".join([k for k, _ in dict_.items()])) # Lambda, List Comprehension            |
#                                                                                                       Single Responsible


def greeting(greeting_text): # Decorator
    def my_decorator(func):
        def wrapper(arg):
            print(f"""{'-' * len(greeting_text)}
{greeting_text}
{'-' * len(greeting_text)}""")
            func(arg)
        return wrapper
    return my_decorator


get_guess = lambda str_: input(f"{str_} ").lower()


class Shop:  # Single Responsibility, Open Closed
    def __init__(self, assortment: dict):
        self.assortment = assortment

    @greeting("Welcome to my shop!")
    def start_shopping(self):
        bag = []

        print("We have in our shop:")
        print_all_keys(self.assortment)

        while True:
            user_input = get_guess("What do you want to buy? (Exit/exit for exit) ")
        
            if user_input == "exit":
                break

            if user_input in self.assortment.keys():
                print(f"It costs {self.assortment[user_input]}soms")

                if get_guess("Do you want to buy it ? (Y/n) ") == "y":
                    bag.append(user_input)

        if len(bag) > 0:
            summa = sum([self.assortment[item] for item in bag]) # List Comprehension
            print("Your bag:")
            print(", ".join(bag))
            print(f"It all costs {summa}soms")
            
            koshelek = int(get_guess("How much money did you have ? "))

            if koshelek > summa:
              print(f"Your exchange {koshelek - summa}soms")
              print("Have a nice day !")
            elif koshelek == summa:
              print("Have a nice day !")
            else:
              print("You don`t have enough money !")

        print("Cya")


class DamirShop(Shop, JsonMaster):  # Inheritence, Encapsulation
    def __init__(self, name_of_assortment):
        self._set_assortment(name_of_assortment)

    def _set_assortment(self, name_of_assortment):
        assortment = self.read(name_of_assortment)
        super().__init__(assortment)

    @staticmethod # Decorator
    def create_assortment(name, dict_):
        super(DamirShop, DamirShop).write(JsonMaster, name, dict_)



DamirShop.create_assortment("assortment_1",
  {
    "milk": 60,
    "bread": 22,
    "djalal-abad": 40,
    "butter": 100,
    "sausages": 250
  }
)

damir_shop = DamirShop("assortment_1")
damir_shop.start_shopping()
