
alice_inventory = {
    "sword":{
        "type": "weapon",
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

bob_inventory = {
    "magic_ring":{
        "type": "accessory",
        "rarity": "rare",
        "quantity": 1,
        "value": 300
        }
}

def get_inventory_info(inventory: dict) -> None:
    """Display detailed inventory information including items, values, and categories."""
    inventory_value = item_count = 0
    categories = {}
    print("\n=== Alice's Inventory ===")
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
	
    print()

def transaction(alice_inv: dict, bob_inv: dict, item: str, many: int) -> None:
    """Transfer items from Alice's inventory to Bob's inventory."""
    if alice_inv.get(item):
        item_quantity = alice_inv[item].get("quantity")
        if many == 0:
           print("Error: Cannot give 0 items!")
        elif item_quantity >= many:
            alice_inv[item]["quantity"] -= many
            if bob_inv.get(item):
                bob_inv[item]["quantity"] += many
            else:
                bob_inv.update({item: {k: v} for k, v in alice_inv[item].items()})
                bob_inv[item]["quantity"] = many
            if alice_inv[item].get("quantity") == 0:
                alice_inv.pop(item)
            print(f"=== Transaction: Alice gives Bob {many} {item} ===\nTransaction successful!")
        else:
            print(f"Error: '{item}' quantity not enough!")
    else:
        print("Error: alice doesn't have that item!")
    print()
    print("=== Updated Inventories ===")
    
    if alice_inv.get(item):
        alice_qty = alice_inv[item].get("quantity")
    else:
        alice_qty = 0
    
    if bob_inv.get(item):
        bob_qty = bob_inv[item].get("quantity")
    else:
        bob_qty = 0

    
    print(f"Alice {item}: {alice_qty}")
	
    print(f"Bob {item}: {bob_qty}")

def most_valuable(alice_inv, bob_inv):
    print("=== Inventory Analytics ===")
    alice_gold = bob_gold = alice_items = bob_items = 0
    rare_items = []
    for k, v in alice_inv.items():
        gold = v.get("quantity") * v.get("value")
        alice_gold += gold
        alice_items += v.get("quantity")
        if v.get("rarity") == "rare":
            rare_items.append(k)
    for k, v in bob_inv.items():
        gold = v.get("quantity") * v.get("value")
        bob_gold += gold
        bob_items += v.get("quantity")
        if v.get("rarity") == "rare":
            rare_items.append(k)
    
    if bob_gold > alice_gold:
        print(f"Most valuable player: Bob ({bob_gold} gold)")
    elif alice_gold > bob_gold:
        print(f"Most valuable player: Alice ({alice_gold} gold)")
    
    if bob_items > alice_items:
        print(f"Most items: Bob ({bob_items} items)")
    elif alice_items > bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    
    print("Rarest items:", end=' ')

    print(", ".join(rare_items))


print("=== Player Inventory System ===")

item = "potion"

get_inventory_info(alice_inventory)

transaction(alice_inventory, bob_inventory, item, 2)

print()

most_valuable(alice_inventory, bob_inventory)