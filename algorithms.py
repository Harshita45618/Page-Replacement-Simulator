def fifo(pages, capacity):
    frames, faults = [], 0
    history = []

    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            faults += 1
            status = "Fault"
        else:
            status = "Hit"

        history.append((page, frames.copy(), status))

    return faults, history

def lru(pages, capacity):
    frames, faults = [], 0
    history = []

    for page in pages:
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            faults += 1
            status = "Fault"
        else:
            frames.remove(page)
            frames.append(page)
            status = "Hit"

        history.append((page, frames.copy(), status))

    return faults, history


