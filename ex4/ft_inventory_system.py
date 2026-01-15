import sys

def main():
    if (len(sys.argv) > 2):

        args = sys.argv[1:]
        inventory = dict()
        
        for arg in args:
            parts = arg.split(':')
            name = parts[0]
            quantity = int(parts[1])
            inventory.update({name: quantity})

        total_items = sum(inventory.values())
        unique_items = len(inventory)

        print("=== Inventory System Analysis ===")
        print(f"Total items in inventory: {total_items}")
        print(f"Unique item types: {unique_items}")

        items_list = []
        for k, v in inventory.items():
            items_list.append((k, v))

        n = len(items_list)
        i = 0
        while i < n:
            j = 0
            while j < n - i - 1:
                if items_list[j][1] < items_list[j+1][1]:
                    temp = items_list[j]
                    items_list[j] = items_list[j+1]
                    items_list[j+1] = temp
                j += 1
            i += 1

        print("\n=== Current Inventory ===")
        for item in items_list:
            name = item[0]
            qty = item[1]
            percentage = (qty / total_items) * 100

            if qty == 1:
                label = "unit"
            else:
                label = "units"
                
            print(f"{name}: {qty} {label} ({percentage:.1f}%)")

        print("\n=== Inventory Statistics ===")

        most_data = items_list[0]
        least_data = items_list[-1]

        m_label = "unit" if most_data[1] == 1 else "units"
        l_label = "unit" if least_data[1] == 1 else "units"

        print(f"Most abundant: {most_data[0]} ({most_data[1]} {m_label})")
        print(f"Least abundant: {least_data[0]} ({least_data[1]} {l_label})")

        print("\n=== Item Categories ===")
        moderate = dict()
        scarce = dict()
        
        for k, v in inventory.items():
            if v > 3:
                moderate.update({k: v})
            else:
                scarce.update({k: v})
                
        print(f"Moderate: {moderate}")
        print(f"Scarce: {scarce}")

        print("\n=== Management Suggestions ===")
        restock = []

        for k, v in inventory.items():
            if v < 2:
                restock.append(k)
                
        print(f"Restock needed: {restock}")

        print("\n=== Dictionary Properties Demo ===")

        keys_list = []
        for k in inventory.keys():
            keys_list.append(k)
            
        vals_list = []
        for v in inventory.values():
            vals_list.append(v)
            
        print(f"Dictionary keys: {keys_list}")
        print(f"Dictionary values: {vals_list}")

        check = "sword"

        has_sword = inventory.get(check) is not None
        print(f"Sample lookup - '{check}' in inventory: {has_sword}")


main()
