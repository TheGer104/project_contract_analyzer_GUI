# Proyecto de Análisis de Contratos Inteligentes

Este repositorio contiene dos enfoques principales para analizar contratos inteligentes escritos en Solidity:
1. **Interfaz Gráfica**: Una aplicación de escritorio que permite a los usuarios cargar y analizar contratos de manera intuitiva.
2. **GitHub CI/CD**: Un workflow en GitHub Actions que permite realizar análisis automático de contratos inteligentes al hacer un push al repositorio.

## Descripción General

Este proyecto está diseñado para analizar contratos inteligentes y detectar posibles vulnerabilidades y problemas comunes de seguridad en contratos escritos en Solidity. Utiliza [Mythril](https://github.com/ConsenSys/mythril), una herramienta de análisis estático y simbólico para detectar fallos en contratos inteligentes.

El proyecto cuenta con dos modos de uso:
1. **Interfaz Gráfica**: Ideal para usuarios que prefieren una interacción visual.
2. **GitHub CI/CD**: Ideal para desarrolladores que deseen integrar el análisis de contratos en sus flujos de trabajo de GitHub.

---

## Interfaz Gráfica

### Requisitos

- Python 3.10 o superior
- `tkinter` para la interfaz gráfica
- Dependencias listadas en `requirements.txt` (instalarlas con `pip install -r requirements.txt`)
- Mythril (instalar con `pip install mythril`)

### Instrucciones de Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/TuUsuario/TuRepositorio.git
   cd TuRepositorio
  ```bash

2. **Instalar las dependencias:**
    ```bash
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  ```bash

3. **Ejecutar la interfaz gráfica:**
    ```bash
    python src/main.py
  ```bash

3. **Usar la interfaz:**
- **Paso 1**: Al abrir la aplicación, verás la pantalla de inicio.
- **Paso 2**: Selecciona los contratos que deseas analizar en la sección de selección de contratos.
- **Paso 3**: Selecciona el formato de reporte en el cual deseas obtener los resultados (actualmente solo JSON).
- **Paso 4:** Haz clic en "Iniciar Análisis" para comenzar el proceso. El programa ejecutará el análisis en cada contrato seleccionado y generará un reporte para cada uno en la carpeta   reports.
  
**Funcionalidades**
- Selección de contratos: Permite al usuario seleccionar archivos de contrato en Solidity para analizar.
- Elección del formato de reporte: Actualmente soporta JSON.
- Ejecución del análisis: Analiza el contrato usando Mythril y otros métodos de análisis.
- Generación de reportes: Los reportes se guardan en la carpeta reports y tienen nombres únicos basados en el nombre del contrato y la fecha de análisis.

**Configuración y Personalización**
- El archivo config/config.json permite modificar ciertas opciones de análisis y reportes. Aquí puedes ajustar configuraciones como el directorio de salida de los reportes y otros parámetros relevantes al análisis.
- Si deseas cambiar el formato de salida, edita el archivo config/config.json para seleccionar entre las opciones disponibles (actualmente soporta JSON).