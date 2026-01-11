

alice_inventory = {
    "sword":{
        "type": "tgrt",
        "rarity":"rare",
        "quantity": 1,
        "value": 500
        },
    "potion":{
        "type": "consumable",
        "rarity": "common",
        "quantity": 5,
        "value": 50
        },
    "shield":{
        "type": "armor",
        "rarity": "uncommon",
        "quantity": 1,
        "value": 200
        }
    }
bob_inventory = {}

def get_inventory_info(inventory: dict):
    inventory_value = item_count = 0
    categories = {}
    for k, v in inventory.items():
        sum_gold = v.get("quantity") * v.get("value")
        item_type = v.get("type")
        item_rarity = v.get("rarity")
        item_quantity = v.get("quantity")
        item_value = v.get("value")
        inventory_value += sum_gold
        item_count += item_quantity
        categories.update({item_type: item_quantity}) 
        print(
            f"{k} ({item_type}, {item_rarity}): "
            f"{item_quantity}x @ {item_value} gold each = {sum_gold} gold"
            )
    print()

    print(f"Inventory value: {inventory_value} gold")
    
    print(f"Item count: {item_count} items")
    
    print("Categories:", end=' ')
    formatted = []
    for k, v in categories.items():
        formatted.append(f"{k}({v})")
    print(", ".join(formatted))

def transaction(alice_inv, bob_inv, item, many):
    if alice_inv.get(item):
        alice_inv[item]["quantity"] -= many
        print("!!!!!")
item = "sword"
get_inventory_info(alice_inventory)
transaction(alice_inventory, bob_inventory, item, 2)