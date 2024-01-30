def format_date(date):
    """
    Format the give date string
    """
    return date.strftime("%d %b, %Y")


def format_time(date):
    """
    Format the give date string
    """
    return date.strftime("%H:%M %p")


context = {
    "format_date": format_date,
    "format_time": format_time,
}