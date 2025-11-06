import matplotlib.pyplot as plt

def plot_top_keywords(df_trends, n=10, save_path=None):
    top = df_trends.sort_values('count', ascending=False).head(n)
    plt.figure(figsize=(10,6))
    plt.bar(top['keyword'], top['count'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_sentiment_distribution(df, save_path=None):
    counts = df['sentiment_label'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
