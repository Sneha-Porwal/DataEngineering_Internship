from app.file_handler import load_data
from app.analysis import BoutiqueAnalyzer
from app.visualization import plot_stock_by_category, plot_average_price_by_brand

def main():
    print("Fashion Boutique Inventory Analysis")

    df = load_data("data/fashion_boutique_dataset.csv")
    analyzer = BoutiqueAnalyzer(df)

    print("\nBasic Statistics:")
    print(analyzer.basic_statistics())

    print("\nAverage Discount Percentage:")
    print(f"{analyzer.average_discount():.2f}%")

    print("\nStock by Category:")
    stock_category = analyzer.stock_by_category()
    print(stock_category)

    print("\nTop Brands by Stock:")
    print(analyzer.top_brands_by_stock())

    print("\nReturn Rate:")
    print(f"{analyzer.return_rate():.2f}%")

    print("\nAverage Rating by Category:")
    print(analyzer.average_rating_by_category())

    plot_stock_by_category(stock_category)
    plot_average_price_by_brand(df)

if __name__ == "__main__":
    main()
