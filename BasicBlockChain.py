import hashlib
import json
from time import time
from uuid import uuid4
import tkinter as tk
from tkinter import messagebox

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash='1', proof=100)  
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

class BlockchainApp:
    def __init__(self, root):
        self.blockchain = Blockchain()
        self.root = root
        self.root.title("Blockchain Application")

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Mine Button
        self.mine_button = tk.Button(self.root, text="Mine Block", command=self.mine_block)
        self.mine_button.grid(row=0, column=0, padx=10, pady=10)

        # Transaction Form
        self.sender_label = tk.Label(self.root, text="Sender")
        self.sender_label.grid(row=1, column=0, padx=10, pady=5)
        self.sender_entry = tk.Entry(self.root)
        self.sender_entry.grid(row=1, column=1, padx=10, pady=5)

        self.recipient_label = tk.Label(self.root, text="Recipient")
        self.recipient_label.grid(row=2, column=0, padx=10, pady=5)
        self.recipient_entry = tk.Entry(self.root)
        self.recipient_entry.grid(row=2, column=1, padx=10, pady=5)

        self.amount_label = tk.Label(self.root, text="Amount")
        self.amount_label.grid(row=3, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_transaction_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.grid(row=4, column=0, columnspan=2, pady=10)

    
        self.chain_text = tk.Text(self.root, height=20, width=50)
        self.chain_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.display_chain()

    def mine_block(self):
        last_block = self.blockchain.last_block
        last_proof = last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        
        self.blockchain.new_transaction(
            sender="0",
            recipient=str(uuid4()).replace('-', ''),
            amount=1,
        )

        previous_hash = self.blockchain.hash(last_block)
        block = self.blockchain.new_block(proof, previous_hash)

        messagebox.showinfo("Block Mined", f"New Block Forged: {block['index']}")
        self.display_chain()

    def add_transaction(self):
        sender = self.sender_entry.get()
        recipient = self.recipient_entry.get()
        amount = self.amount_entry.get()
        
        if not sender or not recipient or not amount:
            messagebox.showwarning("Input Error", "Please fill out all fields")
            return
        
        index = self.blockchain.new_transaction(sender, recipient, float(amount))
        messagebox.showinfo("Transaction Added", f"Transaction will be added to Block {index}")
        
        self.sender_entry.delete(0, tk.END)
        self.recipient_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.display_chain()

    def display_chain(self):
        self.chain_text.delete(1.0, tk.END)
        chain_data = json.dumps(self.blockchain.chain, indent=4)
        self.chain_text.insert(tk.END, chain_data)

if __name__ == '__main__':
    root = tk.Tk()
    app = BlockchainApp(root)
    root.mainloop()
