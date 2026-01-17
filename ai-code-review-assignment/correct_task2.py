def count_valid_emails(emails):
    """
    Counts strings that appear to be very basic email addresses.
    Requires: non-empty local part + @ + domain with at least one dot.
    Very permissive validation — not RFC 5322 compliant.
    """
    if not isinstance(emails, (list, tuple)):
        return 0

    count = 0

    for item in emails:
        if not isinstance(item, str):
            continue

        email = item.strip()
        if not email:
            continue

        if "@" not in email:
            continue

        try:
            local, domain = email.rsplit("@", 1)
            if not local or not domain:
                continue
            if "." not in domain:
                continue
            if " " in email or len(domain) < 3:
                continue
            count += 1
        except ValueError:
            continue

    return count