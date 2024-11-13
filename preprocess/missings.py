import pandas as pd

def num_missings_col(df: pd.DataFrame) -> pd.Series:
    """Devuelve el numero de missings por columna

    Args:
        df (pd.DataFrame): df que analizar

    Returns:
        pd.Series: Numero de missings por columna
    """
    return df.isna().sum()