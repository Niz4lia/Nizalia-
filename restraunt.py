import tkinter as tk
from tkinter import messagebox
import re  # for regex search

# --- Menu Data ---
menu_items = {
    "Burgers": {
        "Zinger Burger": 450,
        "Beef Burger": 500,
        "Chicken Burger": 400,
    },
    "Pizza": {
        "Small Pizza": 700,
        "Medium Pizza": 950,
        "Large Pizza": 1200,
    },
    "Drinks": {
        "Sprite": 100,
        "Pepsi": 100,
        "7up": 100,
    }
}

# --- Global Order List ---
order = []

# --- Functions ---

def add_to_order(item_name, price):
    """Add selected item to order."""
    try:
        order.append((item_name, price))
        refresh_order_list()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def refresh_order_list():
    """Update order list and total."""
    listbox.delete(0, tk.END)
    total = 0
    for name, price in order:
        listbox.insert(tk.END, f"{name} - Rs {price}")
        total += price
    total_label.config(text=f"Total: Rs {total}")

def clear_order():
    """Clear the entire order."""
    try:
        order.clear()
        refresh_order_list()
    except Exception as e:
        messagebox.showerror("Error", f"Could not clear order: {e}")

def delete_selected():
    """Delete selected item from order."""
    try:
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No Selection", "Please select an item to delete.")
            return
        index = selected_index[0]
        del order[index]
        refresh_order_list()
    except Exception as e:
        messagebox.showerror("Error", f"Could not delete item: {e}")

def print_bill():
    """Print order summary in message box."""
    try:
        if not order:
            messagebox.showwarning("Empty Order", "No items in order to print.")
            return
        bill = "----- Restaurant Bill -----\n\n"
        total = 0
        for name, price in order:
            bill += f"{name} - Rs {price}\n"
            total += price
        bill += f"\n---------------------------\nTotal: Rs {total}\nThank you!"
        messagebox.showinfo("Print Bill", bill)
    except Exception as e:
        messagebox.showerror("Error", f"Could not print bill: {e}")

def search_items():
    """Search menu items using regex."""
    try:
        query = search_entry.get()
        result_box.delete(0, tk.END)
        if not query:
            messagebox.showinfo("Info", "Enter a keyword or regex pattern to search.")
            return

        found = False
        for category, items in menu_items.items():
            for item in items.keys():
                if re.search(query, item, re.IGNORECASE):
                    result_box.insert(tk.END, f"{item} - Rs {items[item]}")
                    found = True
        
        if not found:
            result_box.insert(tk.END, "No match found.")
    except re.error:
        messagebox.showerror("Regex Error", "Invalid regular expression pattern.")
    except Exception as e:
        messagebox.showerror("Error", f"Search failed: {e}")

def add_from_search():
    """Add selected item from search results."""
    try:
        selected = result_box.get(tk.ACTIVE)
        if "Rs" not in selected:
            return
        name, price = selected.split(" - Rs ")
        price = int(price)
        add_to_order(name, price)
    except Exception as e:
        messagebox.showerror("Error", f"Could not add from search: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Restaurant POS System")
root.geometry("1000x1000")
root.config(bg="#a3ffd3")

# --- Menu Frame ---
menu_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
menu_frame.place(x=20, y=20, width=450, height=550)

tk.Label(menu_frame, text="Menu", font=("Arial", 18, "bold"), bg="#ffffff").pack(pady=10)

for category, items in menu_items.items():
    tk.Label(menu_frame, text=category, font=("Arial", 14, "bold"), bg="#eeeeee").pack(fill=tk.X, padx=10, pady=5)
    btn_frame = tk.Frame(menu_frame, bg="#ffffff")
    btn_frame.pack(fill=tk.X, padx=15)
    
    for item, price in items.items():
        btn = tk.Button(btn_frame, text=f"{item}\nRs {price}", width=15, height=2,
                        command=lambda i=item, p=price: add_to_order(i, p))
        btn.pack(side=tk.LEFT, padx=5, pady=5)

# --- Order Frame ---
order_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
order_frame.place(x=500, y=20, width=420, height=400)

tk.Label(order_frame, text="Your Order", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
listbox = tk.Listbox(order_frame, width=45, height=15, font=("Arial", 12))
listbox.pack(padx=10, pady=10)

total_label = tk.Label(order_frame, text="Total: Rs 0", font=("Arial", 14, "bold"), bg="#ffffff")
total_label.pack(pady=5)

# --- Clear Order Button (Very visible) ---
btn_clear = tk.Button(order_frame, text="CLEAR ORDER", bg="#ff1a1a", fg="white",
                      font=("Arial", 16, "bold"), command=clear_order)
btn_clear.pack(pady=10, fill=tk.X, padx=20)

# --- Other Buttons ---
btn_delete = tk.Button(order_frame, text="Delete Selected", bg="#ffa64d", fg="white",
                       font=("Arial", 14, "bold"), command=delete_selected)
btn_delete.pack(pady=5, fill=tk.X, padx=20)

btn_print = tk.Button(order_frame, text="Print Bill", bg="#00cc66", fg="white",
                      font=("Arial", 14, "bold"), command=print_bill)
btn_print.pack(pady=5, fill=tk.X, padx=20)

# --- Search Frame ---
search_frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
search_frame.place(x=500, y=440, width=420, height=250)

tk.Label(search_frame, text="Search (Regex Supported):", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=5)
search_entry = tk.Entry(search_frame, width=30, font=("Arial", 12))
search_entry.pack(pady=5)
tk.Button(search_frame, text="Search", bg="#4da6ff", fg="white", font=("Arial", 12, "bold"), command=search_items).pack(pady=5)

result_box = tk.Listbox(search_frame, width=45, height=600, font=("Arial", 10))
result_box.pack(padx=10, pady=5)
result_box.bind("<Double-1>", lambda e: add_from_search())

# Optional: Bind Enter key for search
search_entry.bind("<Return>", lambda e: search_items())

root.mainloop()
