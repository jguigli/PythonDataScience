import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Read a CSV datasheet and return a DataFrame."""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error handling: {str(e)}")
        return
