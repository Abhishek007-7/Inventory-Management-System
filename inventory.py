class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

def sort_inventory(products):
    return sorted(products, key=lambda x: x.name)

def search_product(products, target_name):
    for product in products:
        if product.name == target_name:
            return product
    return None

def knapsack_replenishment(products, budget):
    n = len(products)
    
    # Cast the budget to an integer to avoid the TypeError
    budget = int(budget)
    
    dp = [0] * (budget + 1)

    for i in range(n):
        for j in range(budget, 0, -1):
            if products[i].price <= j:
                dp[j] = max(dp[j], dp[j - int(products[i].price)] + products[i].quantity)

    optimal_replenishment = []
    remaining_budget = budget

    for i in range(n - 1, -1, -1):
        if dp[remaining_budget] != dp[remaining_budget - int(products[i].price)] + products[i].quantity:
            optimal_replenishment.append(products[i])
            remaining_budget -= int(products[i].price)

    return optimal_replenishment

if __name__ == "__main__":
    inventory = [
        Product(1, "Widget", 10.0, 20),
        Product(2, "Gadget", 15.0, 15),
        Product(3, "Doodad", 5.0, 30),
        Product(4, "Thingamajig", 8.0, 25)
    ]

    sorted_inventory = sort_inventory(inventory)
    print("Sorted Inventory:")
    for product in sorted_inventory:
        print(f"{product.name} - ${product.price} - Quantity: {product.quantity}")

    target_product_name = input("Enter the target product name: ")
    desired_quantity = int(input("Enter the desired quantity: "))

    found_product = search_product(sorted_inventory, target_product_name)
    if found_product:
        print(f"\n{target_product_name} found in the inventory. Quantity: {found_product.quantity}")
    else:
        print(f"\n{target_product_name} not found in the inventory.")

    replenishment_budget = float(input("Enter the replenishment budget: "))
    optimal_replenishment = knapsack_replenishment(sorted_inventory, replenishment_budget)
    
    print("\nOptimal Stock Replenishment within Budget:")
    for product in optimal_replenishment:
        print(f"{product.name} - Quantity: {min(desired_quantity, product.quantity)}")
