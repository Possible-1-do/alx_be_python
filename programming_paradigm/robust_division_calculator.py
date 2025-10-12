def safe_divide(numerator, denominator):
    """Performs safe division with error handling."""

    try:
        # Try converting inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        # If conversion to float fails
        return "Error: Please enter numeric values only."
