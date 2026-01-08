class BoutiqueAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_statistics(self):
        return self.df[['original_price', 'current_price',
                        'markdown_percentage', 'stock_quantity',
                        'customer_rating']].describe()

    def average_discount(self):
        return self.df['markdown_percentage'].mean()

    def stock_by_category(self):
        return self.df.groupby('category')['stock_quantity'].sum()

    def top_brands_by_stock(self, n=5):
        return self.df.groupby('brand')['stock_quantity'].sum().sort_values(ascending=False).head(n)

    def return_rate(self):
        return (self.df['is_returned'].sum() / len(self.df)) * 100

    def average_rating_by_category(self):
        return self.df.groupby('category')['customer_rating'].mean()
