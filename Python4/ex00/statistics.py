def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculates statistical measures (mean, median, quartile, std, var)
     based on the provided values."""
    try:
        if not args:
            raise ValueError("At least one value must be provided.")

        mean = sum(args) / len(args)
        median = sorted(args)[len(args) // 2]
        quartile25 = sorted(args)[int(len(args) * 0.25)]
        quartile75 = sorted(args)[int(len(args) * 0.75)]
        s_diff = [(element - mean) ** 2 for element in args]
        var = sum(s_diff) / len(args)
        std = var ** 0.5

        if 'mean' in kwargs.values():
            print(f"mean : {mean}")

        if 'median' in kwargs.values():
            print(f"median : {median}")

        if 'quartile' in kwargs.values():
            print(f"quartile : [{float(quartile25)}, {float(quartile75)}]")

        if 'std' in kwargs.values():
            print(f"std : {std}")

        if 'var' in kwargs.values():
            print(f"var : {var}")

    except Exception as e:
        print(f"Error handling: {e}")
