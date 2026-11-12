import inventory



def print_main_menu():
    print("""
=================================
       COMPUTER STORE SYSTEM
=================================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit
"""
)
    return


def print_products_management_menu() -> None:
    print("""
--------- PRODUCTS MANAGEMENT ---------

1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu
"""
)
    return


def print_sesrch_menu() -> None:
    print("""
----- SEARCH MEMU -----
1. Search by id
2. Search by name
3. Search by category
4. Beck to Products Management
"""
)
    return


def print_product(product: dict) -> None:
    print(f"id: {product["id"]}, name: {product["name"]}, category: {product["category"]}, price: {product["price"]}, stock: {product["stock"]}, active: {product["active"]}")
    return


def print_all_products() -> None:
    print("|id\t|name\t\t\t\t|category\t\t|price\t|stock\t|active\t|")
    print("-----------------------------------------------------------------------------------------")
    for product in inventory.products:
        print(f"|{product["id"]}\t|{product["name"]}\t\t{"\t" if len(product["name"]) < 15  else ""}|{product["category"]}\t\t{"\t" if len(product["category"]) < 7  else ""}|{product["price"]}\t|{product["stock"]}\t|{product["active"]}\t|")
        return