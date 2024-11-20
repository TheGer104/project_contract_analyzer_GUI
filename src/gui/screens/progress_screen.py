import tkinter as tk
from tkinter import ttk
import os

class ProgressScreen(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.main_window = main_window
        self.configure(bg="#2E2E2E")
        self.is_analysis_complete = False  # Previene dobles llamadas a `update_progress`

        self.clear_window()  # Limpia cualquier residuo previo

        title_label = tk.Label(self, text="Running Analysis...", font=("Arial", 18), bg="#2E2E2E", fg="white")
        title_label.pack(pady=20)

        self.progress_bar = ttk.Progressbar(self, orient="horizontal", mode="determinate", length=400)
        self.progress_bar.pack(pady=20)
        self.progress_bar["value"] = 0
        self.update_progress()

    def clear_window(self):
        """Elimina cualquier widget que pudiera persistir en la pantalla."""
        for widget in self.winfo_children():
            widget.destroy()

    def update_progress(self):
        if not self.is_analysis_complete:  # Verifica si ya se completó el análisis
            self.progress_bar["value"] += 10
            if self.progress_bar["value"] < 100:
                self.after(500, self.update_progress)
            else:
                self.is_analysis_complete = True  # Marca el análisis como completo
                self.complete_analysis()

    def complete_analysis(self):
        try:
            contract_path = os.path.join(self.main_window.contracts_dir, self.main_window.selected_contract)
            contract_code = self.main_window.data_handler.load_contract(contract_path)

            # Realizar análisis según el modo seleccionado
            if self.main_window.analysis_mode == "basic":
                print("Realizando análisis básico...")
                analysis_results = self.main_window.contract_analyzer.full_analysis(contract_code)
            elif self.main_window.analysis_mode == "complex":
                print("Realizando análisis con Mythril...")
                analysis_results = self.main_window.contract_analyzer.complex_analysis(contract_code, contract_path)

            # Guardar los resultados y generar el reporte
            self.main_window.analysis_results = analysis_results
            self.main_window.report_generator.generate_report(
                analysis_results, contract_name=self.main_window.selected_contract
            )
            self.main_window.show_results_screen()

        except Exception as e:
            print(f"Error durante el análisis: {e}")
            # Muestra un mensaje de error en la interfaz gráfica
            error_label = tk.Label(self, text="An error occurred during the analysis.", fg="red", bg="#2E2E2E")
            error_label.pack(pady=20)
