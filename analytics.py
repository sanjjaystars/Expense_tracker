import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_NAME = "expenses.db"

def get_dataframe():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df


def monthly_summary():
    df = get_dataframe()
    if df.empty:
        print("No data available.")
        return

    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    summary = df.groupby("month")["amount"].sum()
    print("\nMonthly Summary:")
    print(summary)


def category_summary():
    df = get_dataframe()
    if df.empty:
        print("No data available.")
        return

    summary = df.groupby("category")["amount"].sum()
    print("\nCategory Summary:")
    print(summary)


def show_bar_chart():
    df = get_dataframe()
    if df.empty:
        print("No data available.")
        return

    summary = df.groupby("category")["amount"].sum()
    summary.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.show()


def show_pie_chart():
    df = get_dataframe()
    if df.empty:
        print("No data available.")
        return

    summary = df.groupby("category")["amount"].sum()
    summary.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.ylabel("")
    plt.show()
