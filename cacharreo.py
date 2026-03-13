import tkinter as tk
from tkinter import messagebox

class InventoryApp:
    def __init__(self, root):
        """Initialize the main window and the data storage."""
        self.root = root
        self.root.title("Inventory System Pro")
        self.root.geometry("400x500")
        self.root.config(padx=20, pady=20)

        # DATA STORAGE: List of dictionaries
        self.products = []

        self.create_widgets()

    def create_widgets(self):
        """Build the user interface (Labels, Entries, and Buttons)."""
        tk.Label(self.root, text="INVENTORY MANAGEMENT", font=("Arial", 14, "bold")).pack(pady=10)

        # Input Fields
        self.entries = {}
        for field in ["Name", "Price", "Quantity"]:
            tk.Label(self.root, text=f"{field}:").pack(anchor="w")
            entry = tk.Entry(self.root)
            entry.pack(fill="x", pady=5)
            self.entries[field] = entry

        # Action Buttons
        tk.Button(self.root, text="Add Product", command=self.add_product, bg="#3498db", fg="white", font=("Arial", 10, "bold")).pack(fill="x", pady=10)
        tk.Button(self.root, text="Show Summary", command=self.show_summary, bg="#9b59b6", fg="white").pack(fill="x", pady=5)
        tk.Button(self.root, text="Clear Form", command=self.clear_fields).pack(fill="x", pady=5)

        # Status Label
        self.status_label = tk.Label(self.root, text="No products registered", fg="gray", pady=20)
        self.status_label.pack()

    def add_product(self):
        """Validate inputs and save the product into the list."""
        try:
            # Extract data from entries
            name = self.entries["Name"].get().strip()
            price = float(self.entries["Price"].get())
            qty = int(self.entries["Quantity"].get())

            if not name or price < 0 or qty < 0:
                raise ValueError("Invalid values")

            # Create product dictionary and add to list
            new_product = {
                "name": name,
                "price": price,
                "qty": qty,
                "total": price * qty
            }
            self.products.append(new_product)

            # Update UI and notify user
            self.status_label.config(text=f"Last added: {name} (${new_product['total']:,.2f})", fg="green")
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
            self.clear_fields()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid Name, Price, and Quantity.")

    def show_summary(self):
        """Generate a summary of all products and the grand total."""
        if not self.products:
            return messagebox.showwarning("Empty", "No products registered yet.")

        total_value = sum(p['total'] for p in self.products)
        report = "INVENTORY REPORT\n" + "-"*30 + "\n"
        
        for p in self.products:
            report += f"• {p['name']}: {p['qty']} x ${p['price']} = ${p['total']:,.2f}\n"

        report += "-"*30 + f"\nGRAND TOTAL: ${total_value:,.2f}"
        messagebox.showinfo("Summary", report)

    def clear_fields(self):
        """Clear all input fields."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

