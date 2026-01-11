

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
		"quntity": 1,
		"value": 200
		}
	}
bob_inventory = {}

sum_gold = alice_inventory['sword'].get("quantity") * alice_inventory["sword"].get("value")
item_type = alice_inventory['sword'].get("type")
item_rarity = alice_inventory['sword'].get("rarity")
item_quantity = alice_inventory['sword'].get("quantity")
item_value = alice_inventory['sword'].get("value")

print(f"sword ({item_type}, {item_rarity}): {item_quantity}x @ {item_value} gold each = {sum_gold} gold")
