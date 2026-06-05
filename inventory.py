

# =====================================================================
# 1. Inventory Initialization (Nested Dictionary)
# =====================================================================
inventory = {
    "laptop": {"price": 999.99, "quantity": 5},      # Less than 10 to trigger low stock
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 49.99, "quantity": 8},   # Less than 10 to trigger low stock
    "monitor": {"price": 199.99, "quantity": 20},
}

# =====================================================================
# 2. Display Inventory Function (Formatted Table)
# =====================================================================
def display_inventory():
    print("\n" + "="*45)
    print(f"{'Product':<15}{'Price':<15}{'Quantity':<15}")
    print("="*45)
    
    total_value = 0.0
    low_stock_products = set()  # Using a set to track items needing restock
    
    for product, details in inventory.items():
        price = details["price"]
        qty = details["quantity"]
        
        # Calculate line value and add to total value
        total_value += price * qty
        
        # Check low stock threshold (< 10) and add to the set if true
        if qty < 10:
            low_stock_products.add(product)
            
        print(f"{product.capitalize():<15}${price:<14.2f}{qty:<15}")
        
    print("-"*45)
    print(f"Total Inventory Value: ${total_value:,.2f}")
    
    # Display low stock alerts from our set
    print("-"*45)
    if low_stock_products:
        # Converting set items to a clean comma-separated string
        alert_list = ", ".join([p.capitalize() for p in low_stock_products])
        print(f"⚠️ LOW STOCK ALERT: The following items need restocking:\n   [{alert_list}]")
    else:
        print("✅ All stock levels are healthy.")
    print("="*45 + "\n")

# --- First view of the inventory ---
print("--- INITIAL INVENTORY STATE ---")
display_inventory()


# =====================================================================
# 3. Product Lookup Feature (Safe access using .get)
# =====================================================================
print("--- PRODUCT LOOKUP DEMO ---")
search_query = input("Enter a product name to look up: ").lower().strip()

# Safe retrieval using .get() to prevent crashes
product_data = inventory.get(search_query)

if product_data:
    print(f"🔎 Match Found -> {search_query.capitalize()}: Price: ${product_data['price']:.2f}, Current Qty: {product_data['quantity']}")
else:
    print(f"❌ '{search_query}' does not exist in our inventory system.")
print()


# =====================================================================
# 4. Stock Level Update Feature (Simulating Restock/Sale)
# =====================================================================
print("--- STOCK LEVEL UPDATE DEMO ---")
update_target = input("Enter the product name you wish to update: ").lower().strip()

if update_target in inventory:
    try:
        # Prompting user for update quantity change (can be positive or negative)
        change = int(input(f"Enter quantity change for {update_target.capitalize()} (e.g., +10 for restock, -2 for sale): "))
        
        # Modify the inner dictionary value directly
        inventory[update_target]["quantity"] += change
        
        # Prevent inventory from dropping below zero
        if inventory[update_target]["quantity"] < 0:
            inventory[update_target]["quantity"] = 0
            
        print(f"✅ Successfully updated {update_target.capitalize()} quantity.")
    except ValueError:
        print("❌ Invalid input. Quantity change must be a whole number.")
else:
    print(f"❌ Cannot update. '{update_target}' is not in the system.")


# --- Final view showing calculated changes and dynamically updated set ---
print("\n--- UPDATED INVENTORY STATE ---")
display_inventory()
