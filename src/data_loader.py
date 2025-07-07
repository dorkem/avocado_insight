import pandas as pd
import os

def load_avocado_data():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'avocado.csv'))
    df = pd.read_csv(csv_path, parse_dates=['Date'])
    return df
