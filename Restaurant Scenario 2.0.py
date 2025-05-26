# Se toma el código de Restaurant Scenario y se le hacen algunos cambios:

class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
    
    def calculate_total_price(self, quantity: int) -> float:
        return self._price * quantity

    # Getter y Setter para name

    def get_name(self):
        return self._name 
    
    def set_name(self, name: str):
        self._name = name

    # Getter y Setter para price

    def get_price(self):
        return self._price
    
    def set_price(self, price: float):
        if price > 0 and price < 100000:
            self._price = price
            return True
        else:
            return False

# Como aquí ya se habían creado las subclases de MenuItem, se les agregan 
# setters y getters.

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super().__init__(name, price)
        self._size = size

    # Getter y Setter para size

    def get_name(self):
        return self._size
    
    def set_size(self, size: str):
        if size in ["small", "medium", "large"]:
            self._size = size
        else:
            raise ValueError("Size must be 'small', 'medium', or 'large'.")
    
    def calculate_total_price(self, quantity: int) -> float:
        # Ahora no se va a añadir un impuesto a las bebidas, sino un descuento
        return super().calculate_total_price(quantity) * 0.8
    
class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, flavor: str):
        super().__init__(name, price)
        self._flavor = flavor

    # Getter y Setter para flavor

    def get_flavor(self):
        return self._flavor
    
    def set_flavor(self, flavor: str):
        if flavor in ["salty", "sweet"]:
            self._flavor = flavor
            return True
        else:
            raise ValueError("Flavor must be saltyor sweet.")

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type_of_cooking: str):
        super().__init__(name, price)
        self._type_of_cooking = type_of_cooking

    # Getter y Setter para type_of_cooking

    def get_type_of_cooking(self):
        return self._type_of_cooking       

    def set_type_of_cooking(self, type_of_cooking: str):
        if type_of_cooking in ["Italian food", "Colombian food", \
                               "Japanese food", "Indian food", "Mexican food"]:
            self._type_of_cooking = type_of_cooking
            return True
        else:
            raise ValueError("Type of cooking must be Italian, Colombian, \
                             Japanese, Indian or Mexican food.")
        
class Dessert(MenuItem):
    def __init__(self, name: str, price: float, type_of_dessert: str):
        super().__init__(name, price)
        self._type_of_dessert = type_of_dessert
    
    # Getter y Setter para type_of_dessert

    def get_type_of_dessert(self):
        return self._type_of_dessert
    
    def set_type_of_dessert(self, type_of_dessert: str):
        if type_of_dessert in ["Ice Cream", "Cake", "Brownie"]:
            self._type_of_dessert = type_of_dessert
            return True
        else:
            raise ValueError("Type of dessert must be Ice Cream, Cake or\
                               Brownie.")

# Ahora se vuelve a usar la clase Order
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: MenuItem, quantity: int):
        self.items.append((item, quantity))
    
    def calculate_total_bill(self): # -> float:
        total = 0
        for item, quantity in self.items:
            total += item.calculate_total_price(quantity)
        return total
    
    def apply_discount(self, discount_percentaje: float=0):
        total = self.calculate_total_bill()
        if total > 100000:
        # Aplica un descuento adicional del 5% si el total es mayor a 100
            discount_percentaje += 10 
        elif total > 50000:
            discount_percentaje += 5
        
        discount = total * (discount_percentaje / 100)

        return total - discount
    
    def print_order(self):
        print("Los detalles del pedido son:")
        for item, quantity in self.items:
            print(f"{item._name} (x{quantity}): "
        f"${item.calculate_total_price(quantity):.2f}")
        print(f"Total sin descuento: ${self.calculate_total_bill():.2f}")
        print(f"Total con descuento: ${self.apply_discount():.2f}")

    
# Pero se añade la clase Payment

class Payment:
    def __init__(self):
        pass
    
    def pay(self, amount: Order):
        raise NotImplementedError("Subclasses must implement Pay()")
    
class Tarjeta(Payment):
    def __init__(self, number: int, cvv: int, owner: str):
        super().__init__()
        self.__number = number
        self.__cvv = cvv
        self._owner = owner
    
    # Getters

    def get_number(self):
        return self.__number
    
    def get_cvv(self):
        return self.__cvv
    
    def get_owner(self):
        return self._owner
    
    # Setters

    def set_number(self, number: int):
        self.__number = number
    
    def set_cvv(self, cvv: int):
        self.__cvv = cvv
    
    def set_owner(self, owner: str):
        self._owner = owner

    def pay(self, order: Order):
        amount = order.apply_discount()
        print(f"Pagando ${amount: .2f} con tarjeta *****{str(self.__number)[-4:]} \
de {self._owner}")
        
class Efectivo(Payment):
    def __init__(self, delivered_amount: float, client: str):
        super().__init__()
        self._delivered_amount = delivered_amount
        self._client = client
    
    # Getters

    def get_delivered_amount(self):
        return self._delivered_amount
    
    def get_client(self):
        return self._client
    
    # Setters 

    def set_delivered_amount(self, delivered_amount: float):
        if delivered_amount > 0:
            self._delivered_amount = delivered_amount
            return True
        else:
            return False
        
    def set_client(self, client: str):
        self._client = client

    def pay(self, amount: float):
        amount = order.apply_discount()
        if self._delivered_amount >= amount:
            print(f"Payment made in cash by {self._client}. Change: \
{self._delivered_amount - amount}")
        else:
            print(f"Insufficient funds. {amount - self._delivered_amount} \
are missing to complete the payment.")
            
# En este caso solo quiero a añadir un ejemplo de prueba:

main_course = MainCourse("Ajiaco", 20000, "Colombian Food")
beverage = Beverage("Limonada", 5000, "medium")
dessert = Dessert("Helado de Chocolate", 7000, "Ice Cream")

order = Order()
order.add_item(main_course, 2)
order.add_item(beverage, 3)
order.add_item(dessert, 1)

order.print_order()

total_to_pay = order.apply_discount()

print("Cash payment.")
efectivo = Efectivo(100000, "Pepito Pérez")
efectivo.pay(order)

print("\n--- Payment by card ---")
tarjeta = Tarjeta(12345678910, 777, "Pepito Pérez")
tarjeta.pay(order)