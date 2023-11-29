def count_in_list(lst: list, word) -> int:
    result = 0
    try:
        result = lst.count(word)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return result
