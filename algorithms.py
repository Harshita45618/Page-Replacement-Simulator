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


def optimal(pages, capacity):
    frames = []
    faults = 0
    history = []

    for i in range(len(pages)):
        current_page = pages[i]

        if current_page not in frames:
            if len(frames) < capacity:
                frames.append(current_page)
            else:
                future = pages[i+1:]
                index_to_replace = -1
                farthest = -1

                for j in range(len(frames)):
                    if frames[j] not in future:
                        index_to_replace = j
                        break
                    else:
                        next_use = future.index(frames[j])
                        if next_use > farthest:
                            farthest = next_use
                            index_to_replace = j

                frames[index_to_replace] = current_page

            faults += 1
            status = "Fault"
        else:
            status = "Hit"

        history.append((current_page, frames.copy(), status))

    return faults, history
