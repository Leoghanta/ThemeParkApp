## Theme Park Example
#  SDLC Exercise
#  JWILSON 


def get_valid_input(prompt):
    """
    Repeatedly ask the user for an integer visitor count.

    Rules:
    - Must be a whole number (int)
    - Must not be negative
    """
    while True:
        rawdata = input(prompt).strip()
        try:
            number = int(rawdata)
        except ValueError:
            print("INVALID INPUT")
            continue

        if number < 0:
            print("NUMBER MUST NOT BE NEGATIVE")
            continue

        return number


def get_weekday_by_index(index):
    """Return weekday name for a given 0-based index (0=Mon ... 6=Sun)."""
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    return weekdays[index]


def get_daily_totals():
    """Collect 7 days of visitor totals from the user, one per weekday."""
    day_figures = []

    for weekday in range(7):
        value = get_valid_input(f"ENTER VALUE FOR {get_weekday_by_index(weekday)}: ")
        day_figures.append(value)

    return day_figures


def calculate_average_guests(day_figures):
    """Return the average visitors across 7 days."""
    total_guests = 0
    for value in day_figures:
        total_guests += value

    return total_guests / 7


def find_busiest_day(day_figures):
    """
    Return the weekday with the highest visitor count.
    If there is a tie, returns the first day with that max (matches list.index behaviour).
    """
    max_value = max(day_figures)
    index = day_figures.index(max_value)
    return get_weekday_by_index(index)


def find_quietest_day(day_figures):
    """
    Return the weekday with the lowest visitor count.
    If there is a tie, returns the first day with that min (matches list.index behaviour).
    """
    min_value = min(day_figures)
    index = day_figures.index(min_value)
    return get_weekday_by_index(index)


def display_busiest_day(day_figures):
    """Print the busiest day."""
    print(f"BUSIEST DAY: {find_busiest_day(day_figures)}")


def display_quietest_day(day_figures):
    """Print the quietest day."""
    print(f"QUIETEST DAY: {find_quietest_day(day_figures)}")


def display_average_guests(day_figures):
    """Print the average number of guests."""
    average = calculate_average_guests(day_figures)
    print(f"AVERAGE GUESTS: {average:.2f}")


def main():
    day_figures = get_daily_totals()
    display_busiest_day(day_figures)
    display_quietest_day(day_figures)
    display_average_guests(day_figures)


if __name__ == "__main__":
    main()
