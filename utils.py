def analyze_message(message: str):
    msg = message.lower()

    # Determine category
    if "payment" in msg or "refund" in msg:
        category = "billing"
    elif "error" in msg or "not working" in msg:
        category = "technical"
    else:
        category = "feedback"

    # Determine urgency
    urgency = "high" if "urgent" in msg or "asap" in msg else "low"

    return {
        "category": category,
        "urgency": urgency
    }