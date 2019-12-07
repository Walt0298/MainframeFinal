import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def sales_genre_date(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    df.groupby(['Genre'], sort=True)['Total'].sum().plot(ax=ax, rot=0)
    plt.show()


def sales_platform_date(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    df.groupby(['Platform'])['Total'].sum().plot.barh(
        ax=ax, rot=0, color=["C{0}".format(i) for i in range(len(df))])
    ax.legend()
    plt.show()


def sales_publisher(df):
    fig, ax = plt.subplots(figsize=(10, 8))
    df.groupby(['Publisher'])['Total'].sum().plot(ax=ax)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("venta_juegos/input/3-Games.csv")
    df = df[(df["NA_Sales"] > 0) & (df["EU_Sales"] > 0) &
            (df["JP_Sales"] > 0) & (df["Other_Sales"] > 0)]
    df["Total"] = df['NA_Sales'] + df['EU_Sales'] + \
        df['JP_Sales'] + df['Other_Sales']
    sales_genre_date(df)
    sales_platform_date(df)
    sales_publisher(df)
