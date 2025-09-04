import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Sample monthly sales dataset
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [150, 200, 170, 240, 300, 260]
    }
    df = pd.DataFrame(data)

    # Basic KPIs
    avg_sales = df['Sales'].mean()
    max_sales = df['Sales'].max()
    max_month = df.loc[df['Sales'].idxmax(), 'Month']

    print("Average sales:", round(avg_sales, 2))
    print("Max sales:", max_sales, "in", max_month)

    # Plot
    plt.figure()
    plt.plot(df['Month'], df['Sales'], marker='o')
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sales_chart.png", dpi=150)

if __name__ == "__main__":
    main()
