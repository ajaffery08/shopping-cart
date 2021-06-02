

# 1. Capture product IDs until we're done
#    Use Infinite While Loop

selected_ids = []
while True:
    selected_id = input("Please select / scan a valid product id: ")
    if selected_id.upper() == "DONE":
        break
    else:
        selected_ids.append(selected_id)
    print(selected_id)
print("WE HAVE REACHED THE END OF THE LOOP")
print(selected_ids)

# 2) Perform product lookups to determine what the product's name and price are
#selected_ids = ["1","2","3","2","1"]
for selected_id in selected_ids:
    print(selected_id)
    # lookup the corresponding product!
    # or maybe display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    print(matching_product["name"], matching_product["price"])