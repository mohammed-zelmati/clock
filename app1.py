import time

def alarm(new_tuple, h_alarm, m_alarm):
    """Check if the current time matches the alarm time."""
    if h_alarm == new_tuple[0] and m_alarm == new_tuple[1]:
        print("ALARM! Time reached.")
        return True  # Indicate the alarm should stop the loop
    return False

def impression(new_tuple):
    """Display the current time."""
    print(f"{new_tuple[0]:02d} : {new_tuple[1]:02d} : {new_tuple[2]:02d}")

def clock():
    """Main clock loop with alarm functionality."""
    h_alarm = int(input("Set alarm hour (0-23): "))
    m_alarm = int(input("Set alarm minutes (0-59): "))

    # Initialize time values
    h, m, s = 0, 0, 0

    try:
        while True:
            s += 1

            # Increment time
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
            if h == 24:
                h = 0

            # Create the current time tuple
            new_tuple = (h, m, s)

            # Display the current time
            impression(new_tuple)

            # Check the alarm
            if alarm(new_tuple, h_alarm, m_alarm):
                break  # Exit the loop if alarm triggers

            time.sleep(1)

    except KeyboardInterrupt:
        # Handle manual interruption
        print("\nClock stopped.")
        impression(new_tuple)

clock()