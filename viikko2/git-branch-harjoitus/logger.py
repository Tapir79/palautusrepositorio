from datetime import datetime

def logger(viesti):
    """Log the given message with a timestamp."""
    print(f"{datetime.now()}: {viesti}")
