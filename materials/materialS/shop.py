from classes.products import Electronics, Clothing, HouseholdChemicals
from classes.users import Customer, Admin
from classes.shopping_carts import ShoppingCart

if __name__ == "__main__":
    # Создаем продукты
    laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
    tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
    soap = HouseholdChemicals(name="Мыло", price=200, brand="Safeguard", purpose="Мытьё лица", ingredients="Триклозан", category="твёрдое мыло")

    # Создаем пользователей
    customer = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
    admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

    # Создаем корзину покупок и добавляем товары
    cart = ShoppingCart(customer_name=customer.username, registered_by=admin.username)
    cart.add_item(laptop, 1)
    cart.add_item(tshirt, 3)
    cart.add_item(soap, 3)

    # Выводим детали корзины
    print(cart.get_details())

