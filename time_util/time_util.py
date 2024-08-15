from datetime import datetime, timedelta

def date_add(unit: str, amount: int) -> str:
    """
    Adjusts the current date by a specified amount of time and returns the new date as a string.
    
    Parameters:
    unit (str): The unit of time to adjust by. Can be 'day', 'week', or 'month'.
    amount (int): The amount of time to adjust. Positive values move forward in time,
                  while negative values move backward. For weeks and months, negative 
                  values only adjust within the current month.

    Returns:
    str: The adjusted date as a string in 'YYYY-MM-DD' format.
    """
    # Get today's date
    today = datetime.today()
    
    # Calculate the new date based on the unit
    if unit == 'day':
        new_date = today + timedelta(days=amount)
    elif unit == 'week':
        if amount < 0:
            # Calculate the new date, ensuring it doesn't move before the start of the month
            start_of_month = today.replace(day=1)
            if today + timedelta(weeks=amount) < start_of_month:
                new_date = start_of_month
            else:
                new_date = today + timedelta(weeks=amount)
        else:
            new_date = today + timedelta(weeks=amount)
    elif unit == 'month':
        # Simple month adjustment, not handling year overflow
        month = today.month + amount
        year = today.year
        if month > 12:
            month -= 12
            year += 1
        elif month < 1:
            month += 12
            year -= 1
        new_date = today.replace(month=month, year=year)
    else:
        raise ValueError("Unsupported unit. Please use 'day', 'week', or 'month'.")

    # Return the date formatted as a string
    return new_date.strftime("%Y-%m-%d")
