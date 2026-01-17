def calculate_average_order_value(orders):
    """
    Calculate average value of non-cancelled orders.
    Returns 0.0 if there are no valid non-cancelled orders.
    """
    if not isinstance(orders, (list, tuple)):
        return 0.0

    total = 0.0
    valid_count = 0

    for order in orders:
        if not isinstance(order, dict):
            continue

        if order.get("status") == "cancelled":
            continue

        try:
            amount = float(order["amount"])
            total += amount
            valid_count += 1
        except (KeyError, TypeError, ValueError):
            continue

    return total / valid_count if valid_count > 0 else 0.0