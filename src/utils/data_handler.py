import json
import csv
import os

class DataHandler:
    def __init__(self, config):
        # Configura la ruta de contratos basada en la configuración
        self.contracts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../tests/contracts'))
        if not os.path.exists(self.contracts_dir):
            os.makedirs(self.contracts_dir)

    def load_config(self, filepath):
        """Load configuration for analysis."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        
        with open(filepath, 'r') as file:
            config = json.load(file)
        
        return config

    def load_contract(self, filepath):
        """Load a smart contract from a file."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Contract file not found: {filepath}")
        
        with open(filepath, 'r') as file:
            contract_code = file.read()
        
        return contract_code
    
    def list_contracts(self):
        # Lista los archivos de contrato dentro de la ruta configurada
        return [f for f in os.listdir(self.contracts_dir) if f.endswith('.sol')]


    def select_contract(self, contracts):
        """Allow the user to select a contract from the list."""
        print("Available contracts:")
        for idx, contract in enumerate(contracts, start=1):
            print(f"{idx}. {contract}")
        
        choice = int(input("Select a contract by number: ")) - 1
        if 0 <= choice < len(contracts):
            return contracts[choice]
        else:
            print("Invalid choice.")
            return None
