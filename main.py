from validators import get_valid_num
import products
import prints


def main() -> None:
    while True:
        prints.print_main_menu()
        user_choose = get_valid_num("Choose an option: ")
        if user_choose == "1":
            products.products_management_menu()
        elif user_choose == "5":
            print("Bye bye :)")
            break
        else:
            print(f"{user_choose} isn't valid option")


if __name__== "__main__":
    main()
