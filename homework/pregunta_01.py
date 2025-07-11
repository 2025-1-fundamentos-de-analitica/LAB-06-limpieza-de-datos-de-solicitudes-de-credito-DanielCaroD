"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
from pathlib import Path
import pandas as pd

def clean_stringcol(col: pd.Series, strip=True):
    col = col.copy()
    col = col.str.lower()
    col = col.str.replace(" ", "_")
    col = col.str.replace(".", "_")
    col = col.str.replace("-", "_")
    if strip:
        col = col.str.strip()
    return col


def clean_df(df: pd.DataFrame):
    df = df.copy()
    df = df.dropna()
    df["monto_del_credito"] = df["monto_del_credito"].str.removeprefix("$ ").str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)

    df["tipo_de_emprendimiento"] = clean_stringcol(df["tipo_de_emprendimiento"]).astype("category")

    df["sexo"] = df["sexo"].str.lower().astype("category")

    df["estrato"] = df["estrato"].astype("category")
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int).astype("category")

    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True, format="mixed")

    df["barrio"] = clean_stringcol(df["barrio"], strip=False).astype("category")

    df["idea_negocio"] = clean_stringcol(df["idea_negocio"]).astype("category")

    df["línea_credito"] = clean_stringcol(df["línea_credito"]).astype("category")

    df.drop_duplicates(inplace=True)

    return df

from pathlib import Path
import pandas as pd


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", index_col=0, sep=";")
    df = clean_df(df)
    outdir = Path("files/output")
    outdir.mkdir(parents=True, exist_ok=True)
    df.to_csv(outdir / "solicitudes_de_credito.csv", sep=";")
    
pregunta_01()