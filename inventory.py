categories = ["Gaming", "Accessories", "Computers", "Components", "Monitors", "Audio", "Networking", "Storage"]

products = [
    {"id": 1, "name": "Gaming Mouse", "category": "Gaming", "price": 150.0, "stock": 20, "active": True},
    {"id": 2, "name": "Mechanical Keyboard", "category": "Accessories", "price": 350.0, "stock": 10, "active": True},
    {"id": 3, "name": "Gaming Headset", "category": "Gaming", "price": 280.0, "stock": 4, "active": True},
    {"id": 4, "name": "RGB Mouse Pad XL", "category": "Gaming", "price": 89.9, "stock": 35, "active": True},
    {"id": 5, "name": "Gaming Chair Pro", "category": "Gaming", "price": 1199.0, "stock": 3, "active": True},
    {"id": 6, "name": "Wireless Mouse", "category": "Accessories", "price": 99.0, "stock": 42, "active": True},
    {"id": 7, "name": "USB-C Hub 7-in-1", "category": "Accessories", "price": 179.0, "stock": 0, "active": True},
    {"id": 8, "name": "Laptop Stand Aluminum", "category": "Accessories", "price": 129.0, "stock": 18, "active": True},
    {"id": 9, "name": "Webcam Full HD 1080p", "category": "Accessories", "price": 249.0, "stock": 2, "active": True},
    {"id": 10, "name": "Gaming Laptop 15.6\"", "category": "Computers", "price": 5899.0, "stock": 5, "active": True},
    {"id": 11, "name": "Ultrabook 14\"", "category": "Computers", "price": 4290.0, "stock": 7, "active": True},
    {"id": 12, "name": "Mini PC i5", "category": "Computers", "price": 2390.0, "stock": 0, "active": True},
    {"id": 13, "name": "Graphics Card RTX 4060", "category": "Components", "price": 1490.0, "stock": 6, "active": True},
    {"id": 14, "name": "SSD NVMe 1TB", "category": "Components", "price": 329.0, "stock": 25, "active": True},
    {"id": 15, "name": "RAM DDR5 16GB", "category": "Components", "price": 219.0, "stock": 1, "active": True},
    {"id": 16, "name": "Power Supply 750W", "category": "Components", "price": 459.0, "stock": 9, "active": True},
    {"id": 17, "name": "Monitor 27\" 144Hz", "category": "Monitors", "price": 1290.0, "stock": 8, "active": True},
    {"id": 18, "name": "Monitor 24\" Full HD", "category": "Monitors", "price": 599.0, "stock": 12, "active": True},
    {"id": 19, "name": "Bluetooth Speaker", "category": "Audio", "price": 199.0, "stock": 15, "active": True},
    {"id": 20, "name": "Studio Headphones", "category": "Audio", "price": 549.0, "stock": 0, "active": True},
    {"id": 21, "name": "WiFi 6 Router", "category": "Networking", "price": 399.0, "stock": 11, "active": True},
    {"id": 22, "name": "Network Switch 8-Port", "category": "Networking", "price": 149.0, "stock": 3, "active": True},
    {"id": 23, "name": "External HDD 2TB", "category": "Storage", "price": 389.0, "stock": 14, "active": True},
    {"id": 24, "name": "USB Flash Drive 64GB", "category": "Storage", "price": 39.9, "stock": 60, "active": True},
    {"id": 25, "name": "VGA Cable 1.5m", "category": "Accessories", "price": 19.9, "stock": 30, "active": False},
    {"id": 26, "name": "DVD Writer External", "category": "Storage", "price": 149.0, "stock": 0, "active": False},
]

sales = [
    {
        "id": 1,
        "items": [
            {"product_id": 1, "name": "Gaming Mouse", "quantity": 2, "unit_price": 139.0, "total": 278.0},
            {"product_id": 2, "name": "Mechanical Keyboard", "quantity": 1, "unit_price": 350.0, "total": 350.0},
        ],
        "subtotal": 628.0,
        "discount": 0.0,
        "total": 628.0,
    },
    {
        "id": 2,
        "items": [
            {"product_id": 24, "name": "USB Flash Drive 64GB", "quantity": 5, "unit_price": 39.9, "total": 199.5},
        ],
        "subtotal": 199.5,
        "discount": 0.0,
        "total": 199.5,
    },
    {
        "id": 3,
        "items": [
            {"product_id": 10, "name": "Gaming Laptop 15.6\"", "quantity": 1, "unit_price": 5899.0, "total": 5899.0},
            {"product_id": 4, "name": "RGB Mouse Pad XL", "quantity": 1, "unit_price": 89.9, "total": 89.9},
            {"product_id": 1, "name": "Gaming Mouse", "quantity": 1, "unit_price": 150.0, "total": 150.0},
        ],
        "subtotal": 6138.9,
        "discount": 613.89,
        "total": 5525.01,
    },
    {
        "id": 4,
        "items": [
            {"product_id": 14, "name": "SSD NVMe 1TB", "quantity": 2, "unit_price": 349.0, "total": 698.0},
            {"product_id": 15, "name": "RAM DDR5 16GB", "quantity": 2, "unit_price": 219.0, "total": 438.0},
        ],
        "subtotal": 1136.0,
        "discount": 0.0,
        "total": 1136.0,
    },
    {
        "id": 5,
        "items": [
            {"product_id": 6, "name": "Wireless Mouse", "quantity": 3, "unit_price": 99.0, "total": 297.0},
        ],
        "subtotal": 297.0,
        "discount": 0.0,
        "total": 297.0,
    },
    {
        "id": 6,
        "items": [
            {"product_id": 17, "name": "Monitor 27\" 144Hz", "quantity": 2, "unit_price": 1290.0, "total": 2580.0},
            {"product_id": 8, "name": "Laptop Stand Aluminum", "quantity": 2, "unit_price": 129.0, "total": 258.0},
        ],
        "subtotal": 2838.0,
        "discount": 425.7,
        "total": 2412.3,
    },
    {
        "id": 7,
        "items": [
            {"product_id": 3, "name": "Gaming Headset", "quantity": 1, "unit_price": 280.0, "total": 280.0},
            {"product_id": 4, "name": "RGB Mouse Pad XL", "quantity": 2, "unit_price": 89.9, "total": 179.8},
            {"product_id": 1, "name": "Gaming Mouse", "quantity": 2, "unit_price": 150.0, "total": 300.0},
        ],
        "subtotal": 759.8,
        "discount": 0.0,
        "total": 759.8,
    },
    {
        "id": 8,
        "items": [
            {"product_id": 21, "name": "WiFi 6 Router", "quantity": 1, "unit_price": 399.0, "total": 399.0},
            {"product_id": 22, "name": "Network Switch 8-Port", "quantity": 1, "unit_price": 149.0, "total": 149.0},
        ],
        "subtotal": 548.0,
        "discount": 0.0,
        "total": 548.0,
    },
    {
        "id": 9,
        "items": [
            {"product_id": 24, "name": "USB Flash Drive 64GB", "quantity": 4, "unit_price": 39.9, "total": 159.6},
            {"product_id": 23, "name": "External HDD 2TB", "quantity": 1, "unit_price": 389.0, "total": 389.0},
        ],
        "subtotal": 548.6,
        "discount": 27.43,
        "total": 521.17,
    },
    {
        "id": 10,
        "items": [
            {"product_id": 13, "name": "Graphics Card RTX 4060", "quantity": 1, "unit_price": 1490.0, "total": 1490.0},
            {"product_id": 16, "name": "Power Supply 750W", "quantity": 1, "unit_price": 459.0, "total": 459.0},
            {"product_id": 14, "name": "SSD NVMe 1TB", "quantity": 1, "unit_price": 329.0, "total": 329.0},
        ],
        "subtotal": 2278.0,
        "discount": 227.8,
        "total": 2050.2,
    },
    {
        "id": 11,
        "items": [
            {"product_id": 6, "name": "Wireless Mouse", "quantity": 2, "unit_price": 99.0, "total": 198.0},
            {"product_id": 4, "name": "RGB Mouse Pad XL", "quantity": 1, "unit_price": 89.9, "total": 89.9},
        ],
        "subtotal": 287.9,
        "discount": 0.0,
        "total": 287.9,
    },
    {
        "id": 12,
        "items": [
            {"product_id": 19, "name": "Bluetooth Speaker", "quantity": 1, "unit_price": 199.0, "total": 199.0},
        ],
        "subtotal": 199.0,
        "discount": 0.0,
        "total": 199.0,
    },
    {
        "id": 13,
        "items": [
            {"product_id": 11, "name": "Ultrabook 14\"", "quantity": 1, "unit_price": 4290.0, "total": 4290.0},
            {"product_id": 6, "name": "Wireless Mouse", "quantity": 1, "unit_price": 99.0, "total": 99.0},
            {"product_id": 8, "name": "Laptop Stand Aluminum", "quantity": 1, "unit_price": 129.0, "total": 129.0},
        ],
        "subtotal": 4518.0,
        "discount": 0.0,
        "total": 4518.0,
    },
    {
        "id": 14,
        "items": [
            {"product_id": 1, "name": "Gaming Mouse", "quantity": 3, "unit_price": 150.0, "total": 450.0},
            {"product_id": 3, "name": "Gaming Headset", "quantity": 1, "unit_price": 280.0, "total": 280.0},
        ],
        "subtotal": 730.0,
        "discount": 146.0,
        "total": 584.0,
    },
    {
        "id": 15,
        "items": [
            {"product_id": 18, "name": "Monitor 24\" Full HD", "quantity": 1, "unit_price": 599.0, "total": 599.0},
            {"product_id": 2, "name": "Mechanical Keyboard", "quantity": 1, "unit_price": 350.0, "total": 350.0},
        ],
        "subtotal": 949.0,
        "discount": 0.0,
        "total": 949.0,
    },
]
