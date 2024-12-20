class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer_name, registered_by):
        """
        Инициализирует корзину с именем покупателя и пользователем, зарегистрировавшим покупки.
        """
        self.customer_name = customer_name
        self.registered_by = registered_by
        self.items = []

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        if not self.items:
            return f"Покупатель: {self.customer_name}\nКорзина пуста.\nЗарегистрировал покупки пользователь: {self.registered_by}"
        
        details = f"Покупатель: {self.customer_name}\n"
        details += "Корзина покупок:\n"
        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общая сумма: {self.get_total()} руб\n"
        details += f"Зарегистрировал покупки пользователь: {self.registered_by}"
        return details