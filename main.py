import tkinter as tk
from tkinter import ttk, messagebox

from algorithms import fifo, lru, optimal, mru
from visualization import plot_graph
from utils import calculate_metrics


def run_simulation():
    try:
        pages = list(map(int, entry_pages.get().split()))
        capacity = int(entry_frames.get())
        algo = algo_var.get()
    except:
        messagebox.showerror("Error", "Invalid Input")
        return

    table.delete(*table.get_children())

    def display(history, title):
        table.insert("", "end", values=("", title, "", ""))
        for i, (page, frames, status) in enumerate(history):
            table.insert("", "end", values=(i+1, page, frames, status))

    if algo == "FIFO":
        faults, history = fifo(pages, capacity)
        display(history, "FIFO")

        hits, ratio = calculate_metrics(faults, len(pages))
        result_label.config(text=f"Faults={faults}, Hits={hits}, Ratio={ratio:.2f}")

    elif algo == "LRU":
        faults, history = lru(pages, capacity)
        display(history, "LRU")

        hits, ratio = calculate_metrics(faults, len(pages))
        result_label.config(text=f"Faults={faults}, Hits={hits}, Ratio={ratio:.2f}")

    elif algo == "MRU":
        faults, history = mru(pages, capacity)
        display(history, "MRU")

        hits, ratio = calculate_metrics(faults, len(pages))
        result_label.config(text=f"Faults={faults}, Hits={hits}, Ratio={ratio:.2f}")

    elif algo == "Optimal":
        faults, history = optimal(pages, capacity)
        display(history, "Optimal")

        hits, ratio = calculate_metrics(faults, len(pages))
        result_label.config(text=f"Faults={faults}, Hits={hits}, Ratio={ratio:.2f}")

    elif algo == "Compare All":
        f1, h1 = fifo(pages, capacity)
        f2, h2 = lru(pages, capacity)
        f3, h3 = mru(pages, capacity)
        f4, h4 = optimal(pages, capacity)

        display(h1, "FIFO")
        display(h2, "LRU")
        display(h3, "MRU")
        display(h4, "Optimal")

        results = {
            "FIFO": f1,
            "LRU": f2,
            "MRU": f3,
            "Optimal": f4
        }

        best = min(results, key=results.get)
        result_label.config(text=f"Best: {best} | {results}")

        plot_graph(results)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Page Replacement Simulator")
root.geometry("850x600")

tk.Label(root, text="Page Reference String").pack()
entry_pages = tk.Entry(root, width=50)
entry_pages.pack()

tk.Label(root, text="Number of Frames").pack()
entry_frames = tk.Entry(root)
entry_frames.pack()

algo_var = tk.StringVar()
algo_dropdown = ttk.Combobox(root, textvariable=algo_var)

algo_dropdown['values'] = ["FIFO", "LRU", "MRU", "Optimal", "Compare All"]
algo_dropdown.pack()
algo_dropdown.current(0)

tk.Button(root, text="Run Simulation", command=run_simulation).pack(pady=10)

columns = ("Step", "Page", "Frames", "Status")
table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    table.heading(col, text=col)

table.pack(expand=True, fill='both')

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()