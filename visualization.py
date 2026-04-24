import matplotlib.pyplot as plt

def plot_graph(results):
    names = list(results.keys())
    values = list(results.values())

    plt.bar(names, values)
    plt.title("Page Fault Comparison")
    plt.xlabel("Algorithms")
    plt.ylabel("Page Faults")
    plt.show()