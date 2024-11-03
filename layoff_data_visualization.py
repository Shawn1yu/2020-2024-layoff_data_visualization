# -*- coding: utf-8 -*-
"""Layoff_Data_Visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10TbEx2FKxqcXVgnw0JX84Q4eVcaN--0a
"""

pip install basemap

!pip install squarify

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify
from mpl_toolkits.basemap import Basemap
import warnings
warnings.filterwarnings("ignore")

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('layoffs_data.csv')

df.head()

df.tail()

df.shape

df.info()

df.describe()

df.describe(include = "all").T

df.isnull().sum()

df['Laid_Off_Count'] = df['Laid_Off_Count'].replace(np.NAN, 0)
df['Funds_Raised'] = df['Funds_Raised'].replace(np.NAN, 0)
df['Percentage'] = df['Percentage'].replace(np.NAN, 0)
df.isnull().sum()

df.duplicated().sum()

import datetime as dt
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
df['quarter'] = df['Date'].dt.to_period('Q')
df.head()

from wordcloud import WordCloud
company_names = " ".join(df.sort_values('Laid_Off_Count', ascending=False)['Company'].head(10))

wordcloud = WordCloud(max_words=200, background_color="white", colormap="viridis").generate(company_names)

plt.figure(figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Top 10 Companies with Highest Layoffs')
plt.show()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 10))

sns.barplot(
    data=df.groupby('Industry')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index(),
    y='Industry', x='Laid_Off_Count', edgecolor='black', palette='Set3', ax=axs[0]
)
axs[0].set_title('Laid Off Count by Industry')
axs[0].set_xlabel('Laid Off Count')

sns.barplot(
    data=df.groupby('Industry')['Percentage'].sum().sort_values(ascending=False).reset_index(),
    y='Industry', x='Percentage', edgecolor='black', palette='muted', ax=axs[1]
)
axs[1].set_title('Percent Laid Off by Industry')
axs[1].set_xlabel('Percent Laid Off')

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

sns.barplot(
    data=df.groupby('Stage')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index(),
    y='Stage', x='Laid_Off_Count', edgecolor='black', palette='Set2', ax=axs[0]
)
axs[0].set_title('Laid Off Count by Company Stage')
axs[0].set_xlabel('Laid Off Count')

sns.barplot(
    data=df.groupby('Stage')['Percentage'].sum().sort_values(ascending=False).reset_index(),
    y='Stage', x='Percentage', edgecolor='black', palette='Set3', ax=axs[1]
)
axs[1].set_title('Percent Laid Off by Company Stage')
axs[1].set_xlabel('Percent Laid Off')

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(12, 6))

sns.barplot(
    data=df,
    x='Year', y='Laid_Off_Count', hue='Month',
    estimator=sum, edgecolor='black', palette='pastel', ax=ax
)

ax.set_title('Layoffs by Year and Month')
ax.set_ylabel('Laid Off Count')

plt.tight_layout()
plt.show()

fig, axs = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(8, 5))

sns.lineplot(
    data=df.groupby('Year')['Laid_Off_Count'].sum().reset_index(),
    x='Year', y='Laid_Off_Count', marker='o', ax=axs[0]
)
axs[0].set_title('Laid Off Count by Year')
axs[0].set_ylabel('Laid Off Count')

sns.barplot(
    data=df.groupby('Year')['Laid_Off_Count'].sum().reset_index(),
    x='Year', y='Laid_Off_Count', palette='Set3', linewidth=1, edgecolor='black', ax=axs[1]
)
axs[1].set_title('Laid Off Count by Year')
axs[1].set_ylabel('Laid Off Count')

plt.tight_layout()
plt.show()

monthly_data = df.groupby(df['Date'].dt.to_period('M'))['Laid_Off_Count'].sum().reset_index()
monthly_data['Date'] = monthly_data['Date'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(monthly_data['Date'], monthly_data['Laid_Off_Count'], marker='o', linestyle='-')
ax.set_title('Monthly Layoffs Count Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Laid Off Count')

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 4))

sns.barplot(
    data=df.sort_values(by='quarter'),
    x='quarter', y='Laid_Off_Count',
    linewidth=1, edgecolor='black', palette='pastel', ax=ax
)

ax.set_title('Layoffs per quarter')
ax.set_ylabel('Laid Off Count')
ax.set_xlabel('Quarter')

ax.tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.show()

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

df_2023 = df[df['Year'] == 2023]

monthly_data_2023 = df_2023.groupby('Month')['Laid_Off_Count'].sum().reindex(month_order).reset_index()

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 5))

sns.lineplot(data=monthly_data_2023, x='Month', y='Laid_Off_Count', marker='o', ax=axs[0], color='#329da8')
axs[0].set_title('Laid Off Count by Month in 2023')
axs[0].set_ylabel('Laid Off Count')

sns.barplot(data=monthly_data_2023, x='Month', y='Laid_Off_Count', palette='pastel', linewidth=1, edgecolor='black', ax=axs[1])
axs[1].set_ylabel('Laid Off Count')

plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

monthly_data_ex_2023 = df.query("Year != 2023").groupby('Month')['Laid_Off_Count'].sum().reindex(month_order).reset_index()

fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 5))

sns.lineplot(data=monthly_data_ex_2023, x='Month', y='Laid_Off_Count', marker='o', ax=axs[0], color='#ab29cc')
axs[0].set_title('Laid Off Count by Month (Excluding 2023)')
axs[0].set_ylabel('Laid Off Count')

sns.barplot(data=monthly_data_ex_2023, x='Month', y='Laid_Off_Count', palette='bright', linewidth=1, edgecolor='black', ax=axs[1])
axs[1].set_ylabel('Laid Off Count')

plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

top_10_countries = df.groupby('Country')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index().head(10)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=top_10_countries,
    x='Country', y='Laid_Off_Count',
    linewidth=1, edgecolor='black', palette='deep', ax=ax
)

ax.set_title('Layoffs by country (top 10)')
ax.set_ylabel('Laid Off Count')

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()

df_usa = df[df['Country'] == 'United States']

industry_usa = df_usa.groupby('Industry')['Laid_Off_Count'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=industry_usa.sort_values(by='Laid_Off_Count', ascending=False),
    x='Laid_Off_Count', y='Industry',
    linewidth=1, edgecolor='black', palette='deep', ax=ax
)

ax.set_title('Layoffs by Industry in United States')
ax.set_xlabel('Laid Off Count')
ax.set_ylabel('Industry')

plt.xticks(rotation=30)

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 5))

df_usa = df[df['Country'] == 'India']

industry_usa = df_usa.groupby('Industry')['Laid_Off_Count'].sum().reset_index()

ax = sns.barplot(data=industry_usa.sort_values(by='Laid_Off_Count', ascending=False), x='Laid_Off_Count', y='Industry',
                 linewidth=1, edgecolor='black', palette='deep')
ax.set(title='Layoffs by Industry in India', xlabel='Laid Off Count', ylabel='Industry')

plt.tight_layout()
plt.xticks(rotation=30)
plt.show()

fig, ax = plt.subplots(figsize=(10, 5))

df_usa = df[df['Country'] == 'Germany']

industry_usa = df_usa.groupby('Industry')['Laid_Off_Count'].sum().reset_index()

ax = sns.barplot(data=industry_usa.sort_values(by='Laid_Off_Count', ascending=False), x='Laid_Off_Count', y='Industry',
                 linewidth=1, edgecolor='black', palette='deep')
ax.set(title='Layoffs by Industry in Germany', xlabel='Laid Off Count', ylabel='Industry')

plt.tight_layout()
plt.xticks(rotation=30)
plt.show()

top_10_companies = df.groupby('Company')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index().head(10)

fig, ax = plt.subplots(figsize=(12, 4))

sns.barplot(
    data=top_10_companies,
    x='Laid_Off_Count', y='Company',
    linewidth=1, edgecolor='black', palette='Set2', ax=ax
)

ax.set_title('Layoffs by company (top 10)')
ax.set_xlabel('Laid Off Count')
ax.set_ylabel('Company')

plt.tight_layout()
plt.show()

top_10_hq = df.groupby('Location_HQ')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index().head(10)

fig, ax = plt.subplots(figsize=(12, 4))

sns.barplot(
    data=top_10_hq,
    x='Laid_Off_Count', y='Location_HQ',
    linewidth=1, edgecolor='black', palette='pastel', ax=ax
)

ax.set_title('Layoffs by HQ (top 10)')
ax.set_xlabel('Laid Off Count')
ax.set_ylabel('Location HQ')

plt.tight_layout()
plt.show()

import plotly.express as px

world = df.groupby("Country")["Laid_Off_Count"].sum().reset_index()

figure = px.choropleth(
    world,
    locations="Country",
    locationmode="country names",
    color="Laid_Off_Count",
    hover_name="Country",
    range_color=[1, 10000],
    color_continuous_scale="reds",
    title="Countries having LayOffs"
)

figure.show()

sorted_df = df.groupby('Company')['Laid_Off_Count'].sum().sort_values(ascending=False).reset_index().head(10)
Companies = sorted_df["Company"].tolist()
Laid_off_count = sorted_df['Laid_Off_Count'].tolist()

colors = ['#FFC300', '#FF5733', '#C70039', '#900C3F', '#581845', '#DAF7A6', '#33FF57', '#FF33EC', '#3357FF', '#57FF33']
sizes = [count / sum(Laid_off_count) for count in Laid_off_count]
labels = [f'{company}\n{laid_off_count}' for company, laid_off_count in zip(Companies, Laid_off_count)]

plt.figure(figsize=(10, 8))
squarify.plot(sizes=sizes, label=labels, color=colors)
plt.title('Top 10 Companies Laid Off')
plt.axis('off')
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))

sns.scatterplot(
    data=df,
    x='Funds_Raised', y='Laid_Off_Count',
    hue='Industry', palette='coolwarm', edgecolor='w', alpha=0.7, ax=ax
)

ax.set_title('Relationship between Funds Raised and Layoff Count')
ax.set_xlabel('Funds Raised (in dollars)')
ax.set_ylabel('Laid Off Count')

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

plt.tight_layout()
plt.grid(True)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))

sns.scatterplot(
    data=df,
    x='Funds_Raised', y='Laid_Off_Count',
    hue='Industry', palette='coolwarm', edgecolor='w', alpha=0.7, ax=ax
)

ax.set_title('Relationship between Funds Raised and Layoff Count')
ax.set_xlabel('Funds Raised (in dollars)')
ax.set_ylabel('Laid Off Count')

ax.set_xscale('log')
ax.set_yscale('log')

ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1))

plt.tight_layout()
plt.grid(True)
plt.show()

high_funding_threshold = df['Funds_Raised'].quantile(0.75)
high_layoff_threshold = df['Laid_Off_Count'].quantile(0.75)

high_funding_high_layoff = df[(df['Funds_Raised'] >= high_funding_threshold) & (df['Laid_Off_Count'] >= high_layoff_threshold)]

high_funding_high_layoff_info = high_funding_high_layoff[['Company', 'Industry', 'Funds_Raised', 'Laid_Off_Count']]

high_funding_high_layoff_info

fig, ax = plt.subplots(figsize=(12, 8))

sns.scatterplot(
    data=high_funding_high_layoff,
    x='Funds_Raised', y='Laid_Off_Count',
    hue='Industry', palette='coolwarm', edgecolor='w', alpha=0.7, ax=ax
)

ax.set_title('High Funding and High Layoff Companies')
ax.set_xlabel('Funds Raised (in dollars)')
ax.set_ylabel('Laid Off Count')

ax.set_xscale('log')
ax.set_yscale('log')

plt.grid(True)
plt.tight_layout()
plt.show()