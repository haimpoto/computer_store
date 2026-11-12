from prints import print_products_management_menu, print_all_products, print_sesrch_menu, print_product
from validators import get_valid_num, get_valid_string, get_valid_float
from helpers import creat_product_id, is_product_in_categories
import inventory


def products_management_menu() -> None:
    while True:
        print_products_management_menu()
        user_choose = get_valid_num("Choose an option: ")
        if user_choose == "1":
            add_product()
        elif user_choose == "2":
            print_all_products()
        elif user_choose == "3":
            search_product_menu()
        elif user_choose == "6":
            break
        else:
            print(f"{user_choose} isn't valid option")


def add_product():
    product_name = get_valid_string("Enter product name: ")
    product_category = get_valid_string("Enter product catergory: ")
    if not is_product_in_categories(product_category):
        print("Invalid category")
        return
    product_price = get_valid_float("Enter product price: ")
    product_quantity = int(get_valid_num("Enter product quantity: "))
    prodeact_id = creat_product_id()
    inventory.products.append({"id": prodeact_id, "name": product_name, "category": product_category.capitalize() , "price": product_price, "stock": product_quantity, "active": True})

    print(inventory.products)


def search_product_menu() -> None:
    while True:
        print_sesrch_menu()
        user_choose = get_valid_num("Choose an option: ")
        if user_choose == "1":
            user_id_to_search = get_valid_string("Enter id product to search: ")
            the_product = search_product("id", user_id_to_search)
            print_product(the_product) if the_product else print("The product is not found.")
        elif user_choose == "2":
            user_name_to_search = get_valid_string("Enter name product to search: ")
            the_product = search_product("name", user_name_to_search)
            print_product(the_product) if the_product else print("The product is not found.")
        elif user_choose == "3":
            user_cat_to_search = get_valid_string("Enter category product to search: ")
            the_product = search_product("category", user_cat_to_search)
            print_product(the_product) if the_product else print("The product is not found.")
        elif user_choose == "4":
            break
        else:
            print(f"{user_choose} isn't valid option")


def search_product(search_option: str, value: str) -> dict | None:
    for product in inventory.products:
        if value.lower() in str(product[search_option]).lower():
            return product
    return None