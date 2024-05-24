# Basic-BlockChain

This is a Python application implementing a basic blockchain and a graphical user interface (GUI) to interact with it. The application uses the Tkinter library for the GUI and follows the blockchain principles to manage transactions and mine blocks. Here's a breakdown of its components:

Blockchain Class
The Blockchain class is responsible for handling the core functionalities of the blockchain:

Initialization (__init__ method): Sets up the blockchain with an empty chain and current transactions, and creates the genesis block.
New Block (new_block method): Adds a new block to the blockchain after mining (proof of work) and resets the current transactions.
New Transaction (new_transaction method): Adds a new transaction to the list of current transactions.
Hash (hash method): Generates a SHA-256 hash of a block.
Proof of Work (proof_of_work method): Simple proof-of-work algorithm that finds a proof that, when hashed with the last proof, produces a hash starting with four leading zeros.
Valid Proof (valid_proof method): Checks if a hash of the last proof and the current proof has four leading zeros.
Last Block (last_block property): Returns the last block in the chain.
BlockchainApp Class
The BlockchainApp class handles the GUI using Tkinter and interacts with the Blockchain class:

Initialization (__init__ method): Initializes the blockchain, sets up the root window, and creates the GUI components.
Create Widgets (create_widgets method): Creates and arranges the widgets in the GUI, including buttons for mining blocks and adding transactions, text entries for transaction details, and a text widget to display the blockchain.
Mine Block (mine_block method): Mines a new block by solving the proof-of-work puzzle, adds a reward transaction, and displays a message box with the new block information.
Add Transaction (add_transaction method): Adds a new transaction to the blockchain, shows a confirmation message, and updates the display.
Display Chain (display_chain method): Updates the text widget to show the current state of the blockchain.
GUI Components
The GUI includes:

Buttons: For mining blocks and adding transactions.
Labels and Entry Widgets: For entering transaction details (sender, recipient, amount).
Text Widget: For displaying the blockchain data.
How It Works
Mining a Block: When the "Mine Block" button is clicked, a new block is mined by solving a proof-of-work puzzle. A reward transaction is created and added to the block.
Adding a Transaction: Users can enter transaction details and click "Add Transaction" to add a new transaction to the blockchain. The transaction is then included in the next mined block.
Displaying the Blockchain: The current state of the blockchain is displayed in a text widget, formatted as JSON.
This application serves as a simple example of how blockchain technology works, including transaction management and block mining, all wrapped in a user-friendly interface.
