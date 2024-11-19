import tkinter as tk
import json
import re

class ResultsScreen(tk.Frame):
    def __init__(self, main_window, **kwargs):
        super().__init__(main_window, **kwargs)
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        # Crear el área de texto para mostrar los resultados
        self.results_text = tk.Text(self, wrap="word", width=100, height=30)
        self.results_text.pack(padx=20, pady=20, fill="both", expand=True)

        # Configurar estilos de palabras clave y secciones
        self.results_text.tag_configure("title", foreground="darkblue", font=("TkDefaultFont", 10, "bold"))
        self.results_text.tag_configure("header", foreground="blue", font=("TkDefaultFont", 10, "bold"))
        self.results_text.tag_configure("body", font=("TkDefaultFont", 9))
        self.results_text.tag_configure("separator", font=("TkDefaultFont", 8, "italic"))

        # Insertar los resultados formateados en el área de texto
        self.format_and_insert_results()

        # Botones de navegación
        menu_button = tk.Button(self, text="Menu", command=self.main_window.show_start_screen, bg="green", fg="white")
        menu_button.pack(side="left", padx=20, pady=20)

        exit_button = tk.Button(self, text="Exit", command=self.main_window.quit, bg="red", fg="white")
        exit_button.pack(side="right", padx=20, pady=20)

    def format_and_insert_results(self):
        if not hasattr(self.main_window, 'analysis_results') or not self.main_window.analysis_results:
            self.results_text.insert(tk.END, "No results available.", "body")
            return

        # Insertar la información de análisis básico
        self.insert_basic_analysis(self.main_window.analysis_results)

        # Insertar el reporte de análisis de Mythril, si está presente
        if "mythril_analysis" in self.main_window.analysis_results and "mythril_analysis_raw" in self.main_window.analysis_results["mythril_analysis"]:
            raw_report = self.main_window.analysis_results["mythril_analysis"]["mythril_analysis_raw"]
            self.insert_mythril_analysis(raw_report)

    def insert_basic_analysis(self, results):
        # Insertar la información de análisis básico
        self.results_text.insert(tk.END, "Basic Analysis:\n", "header")
        for section, details in results.items():
            if section == "mythril_analysis":
                continue  # Omitir el análisis de Mythril aquí, ya que se procesará por separado
            self.results_text.insert(tk.END, f"\n{section.capitalize()}:\n", "title")
            for key, value in details.items():
                self.results_text.insert(tk.END, f"  {key}: {value}\n", "body")
        self.results_text.insert(tk.END, "\n\n", "body")

    def insert_mythril_analysis(self, raw_report):
        # Dividir el reporte por secciones de vulnerabilidad
        sections = re.split(r'(==== .+ ====)', raw_report)
        
        for section in sections:
            if section.startswith("===="):
                # Insertar encabezado de vulnerabilidad
                self.results_text.insert(tk.END, section.strip() + "\n", "header")
            else:
                # Formatear y agregar saltos de línea en el contenido del reporte
                self.insert_section_with_spacing(section)

    def insert_section_with_spacing(self, section_text):
        lines = section_text.split("\n")
        
        for line in lines:
            line = line.strip()
            if line.startswith("SWC ID:") or line.startswith("Severity:") or line.startswith("Contract:"):
                # Encabezados clave
                self.results_text.insert(tk.END, line + "\n", "title")
            elif line.startswith("In file:"):
                self.results_text.insert(tk.END, line + "\n\n", "separator")
            elif line.startswith("Initial State:") or line.startswith("Transaction Sequence:"):
                self.results_text.insert(tk.END, line + "\n\n", "header")
            elif line:
                # Insertar líneas de información detallada
                self.results_text.insert(tk.END, line + "\n", "body")
        
        # Separar secciones con espacios
        self.results_text.insert(tk.END, "\n\n", "body")
