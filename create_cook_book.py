def create_cook_book(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]  
        i = 0
        while i < len(lines):
            dish_name = lines[i]
            ingredient_count = int(lines[i + 1])
            ingredients = []
            for j in range(ingredient_count):
                ingredient_info = lines[i + 2 + j].split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = float(ingredient_info[1].replace(',', '.')) 
                measure = ingredient_info[2]
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            i += ingredient_count + 2
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity

    return shop_list

file_path = 'C:\\Users\\Artem\\Desktop\\cook_book\\Files\\recipes.txt'
cook_book = create_cook_book(file_path)

print("cook_book = {")
for dish, ingredients in cook_book.items():
    print(f"  '{dish}': [")
    for ingredient in ingredients:
        print(f"    {ingredient},")
    print("  ],")
print("}")

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print("{")
for ingredient, info in shop_list.items():
    print(f"  '{ingredient}': {info},")
print("}")
