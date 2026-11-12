def get_valid_num(massege: str) -> str:
    user_input = input(massege)
    while not user_input.strip().isdigit():
        print(f"Enter only number, {user_input} is invalid")
        user_input = input(massege)
    return user_input


def get_valid_string(massege: str) -> str:
    user_input = input(massege)
    while not user_input.strip():
        user_input = input(massege)
    return user_input


def get_valid_float(massege: str) -> float:
    while True:
        user_input = input(massege)
        try:
            user_input = float(user_input)
        except ValueError:
            print(f"Enter only number, {user_input} is invalid")
        else:
            if user_input <= 0:
                print("Enter positive number")
            else:
                break
    return user_input
