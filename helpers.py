import inventory


def creat_product_id() -> int:
    return max(inventory.products, key=lambda product: product["id"])["id"] + 1


def is_product_in_categories(product_category: str) -> bool:
    for category in inventory.categories:
        if category.lower() == product_category.lower():
            return True
    return False