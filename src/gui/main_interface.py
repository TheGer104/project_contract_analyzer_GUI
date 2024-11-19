import tkinter as tk
import os
from src.gui.screens.start_screen import StartScreen
from src.gui.screens.contract_selection_screen import ContractSelectionScreen
from src.gui.screens.report_format_screen import ReportFormatScreen
from src.gui.screens.progress_screen import ProgressScreen
from src.gui.screens.results_screen import ResultsScreen
from src.analysis.contract_analyzer import ContractAnalyzer
from src.utils.data_handler import DataHandler
from src.config.config_loader import load_config
from src.reports.report_generator import ReportGenerator

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contract Analyzer")
        self.geometry("800x600")

        # Configuración de la ruta de contratos
        self.contracts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../tests/contracts'))
        if not os.path.exists(self.contracts_dir):
            os.makedirs(self.contracts_dir)

        # Inicializa el resto de componentes necesarios aquí, como data_handler, contract_analyzer, etc.
        self.config = load_config()
        self.data_handler = DataHandler(self.config) 
        self.contract_analyzer = ContractAnalyzer(self.config)
        self.report_generator = ReportGenerator(output_dir="reports")

        # Variables para almacenar selección de contrato, modo de análisis y formato de reporte
        self.selected_contract = None
        self.analysis_mode = None
        self.report_format = None
        self.analysis_results = None

        # Carga la lista de contratos disponibles
        self.contracts = self.data_handler.list_contracts()

        # Llama al método de inicio de pantalla
        self.show_start_screen()

    def show_start_screen(self):
        self.clear_window()
        StartScreen(self).pack(fill="both", expand=True)

    def show_contract_selection_screen(self):
        self.clear_window()
        # Pasar la lista de contratos directamente a ContractSelectionScreen
        ContractSelectionScreen(self, self, self.contracts).pack(fill="both", expand=True)

    def show_report_format_screen(self):
        self.clear_window()
        ReportFormatScreen(self, self).pack(fill="both", expand=True)

    def show_progress_screen(self):
        self.clear_window()
        ProgressScreen(self, self).pack(fill="both", expand=True)

    def show_results_screen(self):
        self.clear_window()
        ResultsScreen(self).pack(fill="both", expand=True)

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()  # Destruye todos los widgets en la ventana principal
