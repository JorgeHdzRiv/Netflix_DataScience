import pandas as pd

def load_data(data_path,processed_data_path):
    """
    Carga los datos desde la ruta especificada, muestra información básica
    y guarda los datos procesados en la ruta de salida.

    Parameters:
    data_path (str): Ruta del archivo CSV de entrada.
    processed_data_path (str): Ruta del archivo CSV de salida.

    Returns:
    pd.DataFrame: DataFrame con los datos cargados.
    """
    # Cargar los datos iniciales en un DataFrame
    netflix_data = pd.read_csv(data_path)

    # Mostrar las primeras filas del DataFrame
    print("Primeras filas del DataFrame:")
    print(netflix_data.head())

    # Información general del DataFrame
    print("\nInformación del DataFrame:")
    print(netflix_data.info())

    # Guardar el DataFrame en la carpeta de datos procesados
    netflix_data.to_csv(processed_data_path, index=False)

    # Mostrar la ruta donde se guardaron los datos procesados
    print(f'\nDatos procesados guardados en: {processed_data_path}')

    return netflix_data

# Definir la ruta del archivo de datos y la ruta de salida para los datos procesados
data_path = '../data/raw/netflix_dataset.csv'
processed_data_path = '../data/processed/netflix_titles_processed.csv'

# Llamar a la función de carga de datos
load_data(data_path, processed_data_path)