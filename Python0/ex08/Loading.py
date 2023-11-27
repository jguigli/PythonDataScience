import time
import os


def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size(0)
        return columns, rows
    except OSError:
        print(OSError)
        return None

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()
    terminal_size = get_terminal_size()
    row_size = terminal_size[0]

    for i, item in enumerate(lst):
        progress = min(1.0, (i + 1) / total)
        percentage = int(progress * 100)
        bar_length = 100 
        bar_step = int(progress * 100)
        bar = "█" * percentage * 2
        counter = f"{i + 1}/{total}"
        gap_size = terminal_size[0] - len(str(percentage)) - len(counter) - 10

        print(f"\r{percentage}%|{bar:<{gap_size}}| {i + 1}/{total}", end="", flush=True)
        yield item
    print()
