# %%

# Séries são listas que podem ajudar bastante em alguns métodos estatísticos

import pandas as pd

idades = [22, 50, 27, 55, 78, 48, 74, 19, 70, 34, 26, 24, 51, 23, 22, 70, 78, 40, 33, 28]

# Sempre tenha uma série com tipos de dados iguais
series_idades = pd.Series(idades)
series_idades.describe()