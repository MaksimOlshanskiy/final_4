purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases: list):
    result = 0
    for i in purchases:
        result += i['quantity']*i['price']
    return f'Общая выручка: {result}'


def items_by_category(purchases):
    my_dict = {}
    for i in purchases:
        my_dict.setdefault(i["category"], []).append(i['item'])
    return f'Товары по категориям: {my_dict}'


def expensive_purchases(purchases, min_price):
    result = []
    for i in purchases:
        if i["price"] >= min_price:
            result.append(i)
    return f'Покупки дороже {min_price}: {result}'


def average_price_by_category(purchases):
    my_dict = {}
    for i in purchases:
        my_dict.setdefault(i["category"], []).append(i["price"])
    for key, value in my_dict.items():
        my_dict[key] = sum(value) / len(value)
    return f'Средняя цена по категориям: {my_dict}'


def most_frequent_category(purchases):
    category = ''
    sold_max = 0
    for i in purchases:
        if i['quantity'] > sold_max:
            category = i['category']
            sold_max = i['quantity']
    return f'Категория с наибольшим количеством проданных товаров: {category}'


print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))

