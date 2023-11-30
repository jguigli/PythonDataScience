def count_in_list(lst: list, value) -> int:
    """Retourne le nombre de value contenu dans lst"""
    result = 0
    try:
        result = lst.count(value)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return result
