import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Read Datasheet csv and return a Data Frame"""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return