import pandas as pd
import numpy as np
import random

"""
title: housing data sample
author: jacob murray
description: sample to illustrate a few key python concepts learners ask about
    - list comprehension
    - zip
    - melt
    - plotnine // geom_line + colors
    - ols
"""

# -----------------
# data sample generation
# -----------------

sample_size = 20
sizes = [random.randint(1200, 4800) for _ in range(sample_size)]
bedrooms = [random.randint(1, 4) for _ in range(sample_size)]
effeciency_choices = ['low', 'medium', 'high']
efficiency = [random.choices(effeciency_choices)[0] for _ in range(sample_size)]
eff_mult   = {"high": 0.70, "medium": 0.90, "low": 1.15}
 # seasonal factors per month (Jan–Jun):
seasonal   = {"jan": 1.30, "feb": 1.20, "mar": 1.00, "apr": 0.85, "may": 0.90, "jun": 1.05}
 
def usage(size, beds, eff, month):
    base = size * 0.20 + beds * 50 ## normalizing to hit roughly mean usage of us household
    val  = base * eff_mult[eff] * seasonal[month] ## attempting to account for seasonality
    noise = np.random.normal(0, 44) ## adding random noise to point
    return max(200, round(val + noise)) ## puts 200kwh baseline

untidy_df = pd.DataFrame({
    "id": range(1, sample_size + 1),
    "sqft": sizes,
    "bedrooms": bedrooms,
    "efficiency": efficiency,
    "jan_kwh": [usage(s, b, e, "jan") for s, b, e in zip(sizes, bedrooms, efficiency)],
    "feb_kwh": [usage(s, b, e, "feb") for s, b, e in zip(sizes, bedrooms, efficiency)],
    "mar_kwh": [usage(s, b, e, "mar") for s, b, e in zip(sizes, bedrooms, efficiency)],
    "apr_kwh": [usage(s, b, e, "apr") for s, b, e in zip(sizes, bedrooms, efficiency)],
    "may_kwh": [usage(s, b, e, "may") for s, b, e in zip(sizes, bedrooms, efficiency)],
    "jun_kwh": [usage(s, b, e, "jun") for s, b, e in zip(sizes, bedrooms, efficiency)],
})

### ZIP SAMPLE ()
a = [1, 2, 3]
b = ['a', 'b', 'c']

# No iterable are passed
res = zip()
print(list(res))

# single iterable is passed
res = zip(a)
print(list(res))

# two iterables are passed
res = zip(a, b)
print(list(res))

# verify that caluclation roughly ~800kwh (national avg)
(
    (untidy_df['jan_kwh'].mean() 
    + untidy_df['feb_kwh'].mean()
    + untidy_df['mar_kwh'].mean()) 
    / 3
)

# -------------
# melting 
# -------------
id_vars = ["id", "sqft", "bedrooms", "efficiency"]
 
tidy_df = untidy_df.melt(
    id_vars=id_vars,
    value_vars=[col for col in untidy_df.columns if col.endswith("kwh")],
    var_name="month",
    value_name="electricity_kwh",
)

tidy_df['electricity_kwh'].mean()

# cleaning month variable
tidy_df["month"] = tidy_df["month"].str.replace("_kwh", "")
tidy_df = tidy_df.sort_values(["id", "month"]).reset_index(drop=True)

# --------------
# plotting 
# --------------

from plotnine import ggplot, aes, geom_point, geom_smooth, theme_minimal

housing_plot = (
  ggplot(tidy_df, aes(x = tidy_df['sqft'], y = 'electricity_kwh')) +
    geom_point(aes(color='efficiency'), alpha=.2) +
    geom_smooth(method='lm', se=False, color='blue') +
    theme_minimal()
)

ggplot.show(housing_plot)

housing_plot_2 = (
  ggplot(tidy_df, aes(x = tidy_df['sqft'], y = 'electricity_kwh')) +
    geom_point(aes(color='efficiency'), alpha=.2) +
    geom_smooth(aes(color='efficiency'), method='lm', se=False) +
    theme_minimal()
)
ggplot.show(housing_plot_2)

# --------------
# models 
# --------------

import statsmodels.formula.api as smf

res_e = smf.ols('electricity_kwh ~ sqft + efficiency', data = tidy_df).fit()
print(res_e.summary())

res_e.summary()
