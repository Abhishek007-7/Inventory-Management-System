```markdown
# Inventory Management System

## Description

The Inventory Management System is a Python-based application designed to manage product inventories effectively. It provides functionalities for sorting products, searching for specific items, and determining optimal stock replenishment within a specified budget using the knapsack algorithm.

## Features

- **Product Class**: Represents a product with an ID, name, price, and quantity.
- **Sort Inventory**: Sorts the inventory based on product names.
- **Search Product**: Searches for a product by its name and returns its details if found.
- **Knapsack Replenishment**: Calculates the optimal stock replenishment based on a specified budget, maximizing the quantity of products purchased.

## Getting Started

### Prerequisites

- Python 3.x
- No additional libraries are required; the code uses built-in Python functionality.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/inventory-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd inventory-management-system
   ```

### Usage

1. Run the main script:

   ```bash
   python inventory_management.py
   ```

2. Follow the prompts to:
   - View the sorted inventory.
   - Search for a specific product by name.
   - Input a replenishment budget to determine the optimal stock replenishment.

### Example

When prompted, the system will display the sorted inventory, ask for a product name, desired quantity, and replenishment budget. Based on your inputs, it will provide the optimal stock replenishment suggestions.

```plaintext
Sorted Inventory:
Doodad - $5.0 - Quantity: 30
Thingamajig - $8.0 - Quantity: 25
Widget - $10.0 - Quantity: 20
Gadget - $15.0 - Quantity: 15

Enter the target product name: Widget
Enter the desired quantity: 5

Widget found in the inventory. Quantity: 20

Enter the replenishment budget: 30.0

Optimal Stock Replenishment within Budget:
Doodad - Quantity: 5
Thingamajig - Quantity: 3
```

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or additional features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
