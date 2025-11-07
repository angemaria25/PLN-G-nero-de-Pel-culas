import pandas as pd
import re

# Ruta del archivo original
file_path = "../data/film_reviews_result.csv"

# Leer el archivo en bruto y limpiarlo línea por línea
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_rows = []
for line in lines:
    # Saltar líneas vacías o incorrectas
    if not line.strip() or line.startswith("film_name"):
        continue
    
    # Dividir correctamente usando '||' como separador
    #parts = re.split(r"\|\|", line.strip())
    
    # Dividir correctamente usando '|' como separador
    parts = re.split(r"\|", line.strip())
    
    # Verificar que haya 6 columnas (las esperadas)
    if len(parts) == 6:
        clean_rows.append(parts)
    else:
        # Si hay menos columnas, intentar reparar uniendo fragmentos
        while len(parts) > 6:
            parts[5] = " ".join(parts[5:])
            parts = parts[:6]
        if len(parts) == 6:
            clean_rows.append(parts)

# Crear DataFrame
df_clean = pd.DataFrame(clean_rows, columns=[
    "film_name", "gender", "film_avg_rate", "review_rate", "review_title", "review_text"
])

# Limpiar valores y tipos
df_clean["film_avg_rate"] = (
    df_clean["film_avg_rate"].str.replace(",", ".").str.replace("\t", "").astype(float)
)
df_clean["review_rate"] = pd.to_numeric(df_clean["review_rate"], errors="coerce")
df_clean["review_text"] = df_clean["review_text"].str.replace("\t", " ").str.strip()

# Eliminar filas vacías o sin texto
df_clean = df_clean.dropna(subset=["review_text", "gender"])

# Mostrar ejemplo limpio
print(df_clean)

# Guardar en archivo CSV
df_clean.to_csv('data/film_reviews_result_clean.csv', index=False, encoding='utf-8')