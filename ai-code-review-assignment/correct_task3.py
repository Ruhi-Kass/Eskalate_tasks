def average_valid_measurements(values):
    """
    Calculate average of numeric values, ignoring None and invalid entries.
    Returns 0.0 if no valid numeric values could be processed.
    """
    if not isinstance(values, (list, tuple)):
        return 0.0

    total = 0.0
    valid_count = 0

    for v in values:
        if v is None:
            continue

        try:
            num = float(v)
            total += num
            valid_count += 1
        except (TypeError, ValueError):
            continue

    return total / valid_count if valid_count > 0 else 0.0