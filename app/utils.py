def clean_data(flights_data):
    keys_to_remove = ["is_best", "arrival_time_ahead", "delay"]
    cleaned = []

    for flight in flights_data:
        # convert to dict if it's an class instance
        if hasattr(flight, "__dict__"):
            flight_dict = flight.__dict__
        else:
            flight_dict = flight

        cleaned_flight = {}
        for key, value in flight_dict.items():
            if key not in keys_to_remove:
                cleaned_flight[key] = value
        cleaned.append(cleaned_flight)

    return cleaned
