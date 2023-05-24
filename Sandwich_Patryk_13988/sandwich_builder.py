from enum import Enum
import time

SandwichProcess = Enum('SandwichStart','queue preparation heating ready')
SanwichRoll = Enum('SanwichRoll','zwykła bawarska')
SandwichIngrediens = Enum('SandwichIngrediens','salate chicken cheese double_cheese tomato ham mushrooms beef')
SanwichSouce= Enum('SandwichSouce','mayonnaise mustard ketchup barbecue pesto')
STEP_DELAY = 4

class Sandwich:
    def __init__(self,name):
        self.name = name
        self.roll = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_roll(self,roll):
        self.roll = roll

        print(f'Przygotowywanie twoje bułki ({self.roll.name}) do twojej kanapki: {self}')
        time.sleep(STEP_DELAY)
        print(f'Rodzaj bułki: {self.roll.name}')

#Tradycyjna Kanapka
class TraditionalSandwich:
    def __init__(self):
        self.sandwich = Sandwich('Tradycyjna kanapka')
        self.progress = SandwichProcess.queue
        self.heating_time = 8

    def prepare_roll(self):
        self.progress = SandwichProcess.preparation
        self.sandwich.prepare_roll(SanwichRoll.zwykła)

    def add_ingrediens(self):
        ingredients_addition = 'ser, sałata, pomidory'
        time.sleep(2)
        topping_items = (SandwichIngrediens.salate , SandwichIngrediens.cheese, SandwichIngrediens.tomato)
        print(f'Dodawanie składników ({ingredients_addition}) do twojej kanapki')
        time.sleep(5)
        self.sandwich.topping.append([t for t in topping_items])
        print(f'Dodano składniki: {ingredients_addition}')

    def add_sauce(self):
        time.sleep(2)
        print(f'Dodawanie sosu: Mojonez do twojej kanapki')
        self.sandwich.sauce = SanwichSouce.mayonnaise
        time.sleep(5)
        print(f'Dodano majonez')
        time.sleep(2)

    def heating(self):
        self.progress = SandwichProcess.heating
        print(f'Podgrzewanie twojej kanapki: {self.heating_time} s')
        time.sleep(self.heating_time)
        self.progress = SandwichProcess.ready

#Kanapka z kurczakiem
class ChickenSandwich:
    def __init__(self):
        self.sandwich = Sandwich('Kanapka z kurczakiem')
        self.progress = SandwichProcess.queue
        self.heating_time = 10

    def prepare_roll(self):
        self.progress = SandwichProcess.preparation
        self.sandwich.prepare_roll(SanwichRoll.zwykła)

    def add_ingrediens(self):
        ingredients_addition = 'ser, sałata, pomidory, kurczak'
        time.sleep(2)
        topping_items = (SandwichIngrediens.chicken, SandwichIngrediens.salate, SandwichIngrediens.cheese, SandwichIngrediens.tomato)
        print(f'Dodawanie składników ({ingredients_addition}) do twojej kanapki')
        time.sleep(5)
        self.sandwich.topping.append([t for t in topping_items])
        print(f'Dodano składniki: {ingredients_addition}')

    def add_sauce(self):
        time.sleep(2)
        print(f'Dodawanie sosu: Musztarda, Keczup do twoje kanapki')
        self.sandwich.sauce1 = SanwichSouce.mustard
        self.sandwich.sauce2 = SanwichSouce.ketchup
        time.sleep(5)
        print(f'Dodano musztarde')
        time.sleep(2)
        print(f'Dodano ketchup')
        time.sleep(2)


    def heating(self):
        self.progress = SandwichProcess.heating
        print(f'Podgrzewanie twojej kanapki: {self.heating_time} s')
        time.sleep(self.heating_time)
        self.progress = SandwichProcess.ready


#Kanapka z Pieczarkami
class MushroomSandwich:
    def __init__(self):
        self.sandwich = Sandwich('Kanapka z pieczarkami')
        self.progress = SandwichProcess.queue
        self.heating_time = 12

    def prepare_roll(self):
        self.progress = SandwichProcess.preparation
        self.sandwich.prepare_roll(SanwichRoll.bawarska)

    def add_ingrediens(self):
        ingredients_addition = 'ser, sałata, pomidory, pieczarki'
        time.sleep(2)
        topping_items = (SandwichIngrediens.salate, SandwichIngrediens.cheese, SandwichIngrediens.tomato, SandwichIngrediens.mushrooms)
        print(f'Dodawanie składników ({ingredients_addition}) do twojej kanapki')
        time.sleep(5)
        self.sandwich.topping.append([t for t in topping_items])
        print(f'Dodano składniki: {ingredients_addition}')

    def add_sauce(self):
        time.sleep(2)
        print(f'Dodawanie sosu: Pesto do twoje kanapki')
        self.sandwich.sauce = SanwichSouce.pesto
        time.sleep(5)
        print(f'Dodano Pesto')
        time.sleep(2)


    def heating(self):
        self.progress = SandwichProcess.heating
        print(f'Podgrzewanie twojej kanapki: {self.heating_time} s')
        time.sleep(self.heating_time)
        self.progress = SandwichProcess.ready

#Kanapka z Szynką i serem
class HamSandwich:
    def __init__(self):
        self.sandwich = Sandwich('Kanapka z szynką i podwójnym serem')
        self.progress = SandwichProcess.queue
        self.heating_time = 6

    def prepare_roll(self):
        self.progress = SandwichProcess.preparation
        self.sandwich.prepare_roll(SanwichRoll.bawarska)

    def add_ingrediens(self):
        ingredients_addition = '2 x ser, sałata, szynak, pomidory, pieczarki,'
        time.sleep(2)
        topping_items = (SandwichIngrediens.double_cheese, SandwichIngrediens.salate, SandwichIngrediens.tomato, SandwichIngrediens.ham)
        print(f'Dodawanie składników ({ingredients_addition}) do twojej kanapki')
        time.sleep(5)
        self.sandwich.topping.append([t for t in topping_items])
        print(f'Dodano składniki: {ingredients_addition}')

    def add_sauce(self):
        time.sleep(2)
        print(f'Dodawanie sosu: Ketchup do twoje kanapki')
        self.sandwich.sauce = SanwichSouce.pesto
        time.sleep(5)
        print(f'Dodano Ketchup')
        time.sleep(2)


    def heating(self):
        self.progress = SandwichProcess.heating
        print(f'Podgrzewanie twojej kanapki: {self.heating_time} s')
        time.sleep(self.heating_time)
        self.progress = SandwichProcess.ready


#Kanapka z Wołowiną i barbecue
class BeefSandwich:
    def __init__(self):
        self.sandwich = Sandwich('Kanapka z wołowiną i sosem barbecue')
        self.progress = SandwichProcess.queue
        self.heating_time = 12

    def prepare_roll(self):
        self.progress = SandwichProcess.preparation
        self.sandwich.prepare_roll(SanwichRoll.bawarska)

    def add_ingrediens(self):
        ingredients_addition = 'ser, sałata, wołowina, barbacue'
        time.sleep(2)
        topping_items = (SandwichIngrediens.cheese, SandwichIngrediens.salate, SandwichIngrediens.beef)
        print(f'Dodawanie składników ({ingredients_addition}) do twojej kanapki')
        time.sleep(5)
        self.sandwich.topping.append([t for t in topping_items])
        print(f'Dodano składniki: {ingredients_addition}')

    def add_sauce(self):
        time.sleep(2)
        print(f'Dodawanie sosu: Barbecue do twoje kanapki')
        self.sandwich.sauce = SanwichSouce.pesto
        time.sleep(5)
        print(f'Dodano Barbacue')
        time.sleep(2)


    def heating(self):
        self.progress = SandwichProcess.heating
        print(f'Podgrzewanie twojej kanapki: {self.heating_time} s')
        time.sleep(self.heating_time)
        self.progress = SandwichProcess.ready



class Waiter:
    def __init__(self):
        self.builder = None

    def construct_sandwich(self,builder):
        try:
            self.builder = builder
            steps = (builder.prepare_roll,
                     builder.add_ingrediens,
                     builder.add_sauce,
                     builder.heating)
            [step() for step in steps]
        except:
            print("Nie mamy takiej kanaki w jadłospisie")

    @property
    def sandwich(self):
        return self.builder.sandwich


def validate_style(builders):
    input_order = 'Witam, na jaką kanapkę ma Pan ochotę: [t]Tradycyjna, [k]Kurczak, [p]Pieczarki, [s]Szynka, [w]wołowina? '
    sandwich_style = input(input_order)
    while(True == True):
        try:
            builder = builders[sandwich_style]()
            break
        except:
            input_order = 'Niestety nie mamy takiej kanapki, do wyboru: [t]Tradycyjna, [k]Kurczak, [p]Pieczarki, [s]Szynka, [w]wołowina? '
            sandwich_style = input(input_order)
    valid_input = True

    return (valid_input, builder)

def main():
    builders = dict(t=TraditionalSandwich, k=ChickenSandwich, p=MushroomSandwich, s=HamSandwich, w=BeefSandwich)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print("\n")
    waiter= Waiter()
    waiter.construct_sandwich(builder)
    sandwich = waiter.sandwich

    print("\n")

    print(f'Twoja kanapka: {sandwich}. Jest gotowa. Smacznego :)')


if __name__ == '__main__':
    main()

