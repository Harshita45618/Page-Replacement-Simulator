def calculate_metrics(faults, total):
    hits = total - faults
    hit_ratio = hits / total
    return hits, hit_ratio