class Product:
    name = "Ручка"
    price = 1_000_000_000

    def show_info(self):
        print("Название:", self.name)
        print("Цена:", self.price)

    def is_age_suitable(self, age):
        return True


class Toy(Product):
    name = "Мишка"
    price = 6767
    manufacturer = "Мишлен"
    material = "Нержавеющая сталь"
    age_range = (6, 10)

    def show_info(self):
        print("Название:", self.name)
        print("Цена:", self.price)
        print("Производитель:", self.manufacturer)
        print("Материал:", self.material)
        print("Возрастной диапазон:", self.age_range)

    def is_age_suitable(self, age):
        return self.age_range[0] <= age <= self.age_range[1]


class Book(Product):
    name = "Рофлы. Что такое и как их понимать"
    author = None
    price = 10_000
    publishing = "Пикабу"
    age_range = (14, 18)

    def show_info(self):
        print("Название:", self.name)
        print("Автор:", self.author)
        print("Цена:", self.price)
        print("Издатель:", self.publishing)
        print("Возрастной диапазон:", self.age_range)

    def is_age_suitable(self, age):
        return self.age_range[0] <= age <= self.age_range[1]


class SportInventory(Product):
    name = "Конь гимнастический"
    price = 999
    manufacturer = "ООО \"Рога и копыта\""
    age_range = (18, 60)

    def show_info(self):
        print("Название:", self.name)
        print("Цена:", self.price)
        print("Производитель:", self.manufacturer)
        print("Возрастной диапазон:", self.age_range)

    def is_age_suitable(self, age):
        return self.age_range[0] <= age <= self.age_range[1]


class ProductList:
    products = []

    def show_all(self):
        print("Все товары:")
        for product in self.products:
            product.show_info()
            print()

    def search_by_age(self, age):
        print("Товары подходящие по возрасту:")
        for product in self.products:
            if product.is_age_suitable(age):
                product.show_info()
                print()

    def most_expensive(self, age):
        return max(self.products, key=lambda product: product.price)


product_list = ProductList()
product_list.products = [Toy(), Book(), SportInventory()]

product_list.show_all()

product_list.search_by_age(18)

print("Наиболее дорогой товар:")
product_list.most_expensive(18).show_info()