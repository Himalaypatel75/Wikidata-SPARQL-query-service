import tkinter as tk
from tkinter import ttk

class ShortStraddleAlgoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Short Straddle Algo Robo")
        
        header_label = ttk.Label(root, text="Short Straddle Algo Robo 🤖", font=("Helvetica", 20))
        header_label.pack(pady=20)
        
        broker_frame = ttk.LabelFrame(root, text="Broker Details", padding=(20, 10))
        broker_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Broker details inputs
        user_id_label = ttk.Label(broker_frame, text="Zerodha User ID 💼:")
        user_id_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.user_id_entry = ttk.Entry(broker_frame)
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        access_token_label = ttk.Label(broker_frame, text="Access Token 🔑:")
        access_token_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.access_token_entry = ttk.Entry(broker_frame, show="*")
        self.access_token_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        secret_token_label = ttk.Label(broker_frame, text="Secret Token 🤫:")
        secret_token_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.secret_token_entry = ttk.Entry(broker_frame, show="*")
        self.secret_token_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        totp_label = ttk.Label(broker_frame, text="TOTP 📱:")
        totp_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.totp_entry = ttk.Entry(broker_frame)
        self.totp_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        option_frame = ttk.LabelFrame(root, text="Option Selection", padding=(20, 10))
        option_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        # Option selection dropdown
        option_label = ttk.Label(option_frame, text="Select Option 🛠️:")
        option_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.option_var = tk.StringVar()
        self.option_dropdown = ttk.Combobox(option_frame, textvariable=self.option_var, values=["Nifty", "BankNifty", "Finnifty"])
        self.option_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.option_dropdown.current(0)
        
        # Other input fields
        max_qty_label = ttk.Label(option_frame, text="Max Quantity 💰:")
        max_qty_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.max_qty_entry = ttk.Entry(option_frame)
        self.max_qty_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        lot_qty_label = ttk.Label(option_frame, text="Lot Quantity 📦:")
        lot_qty_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.lot_qty_entry = ttk.Entry(option_frame)
        self.lot_qty_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        # Buttons
        start_button = ttk.Button(root, text="Start", command=self.start_algo)
        start_button.pack(pady=10)
        
        profit_booking_button = ttk.Button(root, text="Profit Booking")
        profit_booking_button.pack(pady=5)
        
        stop_loss_button = ttk.Button(root, text="Stop Loss")
        stop_loss_button.pack(pady=5)
        
        square_off_all_button = ttk.Button(root, text="Square Off All")
        square_off_all_button.pack(pady=5)
        
    def start_algo(self):
        user_id = self.user_id_entry.get()
        access_token = self.access_token_entry.get()
        secret_token = self.secret_token_entry.get()
        totp = self.totp_entry.get()
        option = self.option_var.get()
        max_qty = self.max_qty_entry.get()
        lot_qty = self.lot_qty_entry.get()
        
        # Perform action with the input data (e.g., start the algorithm)
        print("Starting algorithm with the following inputs:")
        print("User ID:", user_id)
        print("Access Token:", access_token)
        print("Secret Token:", secret_token)
        print("TOTP:", totp)
        print("Option:", option)
        print("Max Quantity:", max_qty)
        print("Lot Quantity:", lot_qty)

def main():
    root = tk.Tk()
    app = ShortStraddleAlgoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
