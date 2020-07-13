
from scipy.stats import trim_mean
import pandas as pd
import numpy as np
import wquantiles 
# wquantiles import yazdığımızda yüklenmiyorsa pip install wquantiles ile yükleyip sonra burda import edebiliriz)
# dataylı bilgi https://pypi.org/project/wquantiles/#description

state = pd.read_csv("state.csv")
print(state.head(8))

print("Mean: ", state["Population"].mean())
print("Trimmed Mean: ", trim_mean(state["Population"], 0.1))
print("Median: ", state["Population"].median())
## Trimmed mean is close to median because we cut bootm and top 10% data

# numpy for weighted mean
print("Murder Rate Mean: ", state["Murder.Rate"].mean())
print("Weighted mean: ", np.average(state["Murder.Rate"], weights = state["Population"]))
print("Weighted median: ",  wquantiles.median(state['Murder.Rate'], weights=state['Population']))
