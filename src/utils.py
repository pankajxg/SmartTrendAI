import matplotlib.pyplot as plt

def plot_bar(words_counts, title='Top keywords'):
    if not words_counts:
        return None
    words, counts = zip(*words_counts)
    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(words, counts)
    ax.set_title(title)
    ax.set_xticklabels(words, rotation=45, ha='right')
    plt.tight_layout()
    return fig
