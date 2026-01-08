import matplotlib.pyplot as plt

def plot_stock_by_category(stock_data):
    stock_data.plot(kind='bar')
    plt.title("Stock Quantity by Category")
    plt.xlabel("Category")
    plt.ylabel("Stock Quantity")
    plt.tight_layout()
    plt.show()


def plot_average_price_by_brand(df):
    avg_price = df.groupby('brand')['current_price'].mean()
    avg_price.plot(kind='bar', figsize=(10, 5))
    plt.title("Average Current Price by Brand")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()
