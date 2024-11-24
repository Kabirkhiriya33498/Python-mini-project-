import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class AuctionEaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AuctionEase")
        self.root.geometry("800x600")
        self.root.configure(bg="#ffffff")

        # Auction Data
        self.auction_items = []
        self.current_item_index = -1
        self.current_bid = tk.DoubleVar(value=0)
        self.highest_bidder = tk.StringVar(value="No bids yet")
        self.auction_history = []

        # Style Configuration
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#ffffff")
        self.style.configure("TLabel", background="#ffffff", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("Header.TLabel", font=("Arial", 18, "bold"), foreground="#333333")
        self.style.configure("Search.TEntry", font=("Arial", 12), padding=5)

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Header Bar
        header_frame = ttk.Frame(self.root, style="TFrame")
        header_frame.pack(fill="x", pady=10, padx=10)

        ttk.Label(header_frame, text="AuctionEase", style="Header.TLabel").pack(side="left", padx=10)
        search_entry = ttk.Entry(header_frame, width=50, style="Search.TEntry")
        search_entry.pack(side="left", padx=10)
        ttk.Button(header_frame, text="Search", command=self.search_item).pack(side="left", padx=5)

        # Tabs
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=1, fill="both", padx=10, pady=10)

        # Home Tab
        self.home_tab = ttk.Frame(tab_control, style="TFrame")
        tab_control.add(self.home_tab, text="Home")
        self.create_home_tab()

        # Auction Tab
        self.auction_tab = ttk.Frame(tab_control, style="TFrame")
        tab_control.add(self.auction_tab, text="Auction")
        self.create_auction_tab()

        # History Tab
        self.history_tab = ttk.Frame(tab_control, style="TFrame")
        tab_control.add(self.history_tab, text="History")
        self.create_history_tab()

    def create_home_tab(self):
        ttk.Label(self.home_tab, text="Auction Items", font=("Arial", 16, "bold")).pack(pady=10)

        self.items_list = ttk.Treeview(
            self.home_tab, columns=("Item", "Starting Bid"), show="headings", height=10
        )
        self.items_list.pack(fill="both", padx=10, pady=10)
        self.items_list.heading("Item", text="Item Name")
        self.items_list.heading("Starting Bid", text="Starting Bid (₹)")
        self.items_list.column("Item", width=300)
        self.items_list.column("Starting Bid", width=150)

        ttk.Button(self.home_tab, text="Add New Item", command=self.add_item).pack(pady=10)

    def create_auction_tab(self):
        ttk.Label(self.auction_tab, text="Active Auction", font=("Arial", 16, "bold")).pack(pady=10)

        ttk.Label(self.auction_tab, text="Current Item:").pack()
        self.item_label = ttk.Label(self.auction_tab, text="N/A", font=("Arial", 14))
        self.item_label.pack()

        ttk.Label(self.auction_tab, text="Current Bid:").pack()
        self.current_bid_label = ttk.Label(self.auction_tab, text="N/A", font=("Arial", 14), foreground="#007700")
        self.current_bid_label.pack()

        ttk.Label(self.auction_tab, text="Highest Bidder:").pack()
        self.highest_bidder_label = ttk.Label(self.auction_tab, text="N/A", font=("Arial", 14), foreground="#0077cc")
        self.highest_bidder_label.pack(pady=10)

        ttk.Label(self.auction_tab, text="Your Name:").pack()
        self.bidder_name_entry = ttk.Entry(self.auction_tab, font=("Arial", 12))
        self.bidder_name_entry.pack(pady=5)

        ttk.Label(self.auction_tab, text="Your Bid:").pack()
        self.bid_amount_entry = ttk.Entry(self.auction_tab, font=("Arial", 12))
        self.bid_amount_entry.pack(pady=5)

        ttk.Button(self.auction_tab, text="Place Bid", command=self.place_bid).pack(pady=10)

        ttk.Button(self.auction_tab, text="Start Next Auction", command=self.start_next_auction).pack(pady=10)

    def create_history_tab(self):
        ttk.Label(self.history_tab, text="Auction History", font=("Arial", 16, "bold")).pack(pady=10)

        self.history_list = ttk.Treeview(
            self.history_tab, columns=("Item", "Winner", "Winning Bid"), show="headings", height=10
        )
        self.history_list.pack(fill="both", padx=10, pady=10)
        self.history_list.heading("Item", text="Item")
        self.history_list.heading("Winner", text="Winner")
        self.history_list.heading("Winning Bid", text="Winning Bid (₹)")
        self.history_list.column("Item", width=200)
        self.history_list.column("Winner", width=150)
        self.history_list.column("Winning Bid", width=100)

    def add_item(self):
        item_name = simpledialog.askstring("Add Item", "Enter item name:")
        starting_bid = simpledialog.askfloat("Add Item", "Enter starting bid:")
        if item_name and starting_bid:
            self.auction_items.append({"name": item_name, "starting_bid": starting_bid})
            self.items_list.insert("", "end", values=(item_name, f"₹{starting_bid:.2f}"))
            messagebox.showinfo("Success", f"Item '{item_name}' added to the auction list!")
        else:
            messagebox.showerror("Error", "Invalid item details!")

    def start_next_auction(self):
        self.current_item_index += 1
        if self.current_item_index < len(self.auction_items):
            current_item = self.auction_items[self.current_item_index]
            self.current_bid.set(current_item["starting_bid"])
            self.highest_bidder.set("No bids yet")

            self.item_label.config(text=current_item["name"])
            self.current_bid_label.config(text=f"₹{current_item['starting_bid']:.2f}")
            self.highest_bidder_label.config(text="No bids yet")
        else:
            messagebox.showinfo("Info", "No more items to auction.")

    def place_bid(self):
        bidder_name = self.bidder_name_entry.get().strip()
        try:
            bid_amount = float(self.bid_amount_entry.get())
            if bidder_name and bid_amount > self.current_bid.get():
                self.current_bid.set(bid_amount)
                self.highest_bidder.set(bidder_name)
                self.current_bid_label.config(text=f"₹{bid_amount:.2f}")
                self.highest_bidder_label.config(text=bidder_name)
                messagebox.showinfo("Success", "Bid placed successfully!")
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Invalid bid. Ensure it's higher than the current bid and your name is entered.")

    def search_item(self):
        messagebox.showinfo("Search", "Search functionality is currently under development!")


if __name__ == "__main__":
    root = tk.Tk()
    app = AuctionEaseApp(root)
    root.mainloop()


