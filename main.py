shopping_dict = {
    "Piekarnia": ["Chleb", "Pączek", "Bułki"],
    "Warzywniak": ["Marchew", "Pomidor", "Ogórek"]
}

total_quantity = 0

print("Lista zakupów")

for shop in shopping_dict:
    products = shopping_dict[shop]
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")
    total_quantity += len(products)

print(f"W sumie kupuję: {total_quantity} produktów.")

