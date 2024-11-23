import random
import datetime
import csv

max_capacity = 50
current_cars = 0
events = []
start_date = datetime.datetime(2020, 1, 1, 0, 0)
end_date = datetime.datetime(2024, 11, 22, 23, 59)
current_time = start_date

def is_holiday(date):
    return date.weekday() >= 5  # 5 = Saturday, 6 = Sunday

while current_time <= end_date:
    hour = current_time.hour
    is_peak_morning = 8 <= hour < 10
    is_peak_evening = 17 <= hour < 19
    is_night = hour >= 22 or hour < 7
    holiday = is_holiday(current_time)

    if is_night:
        event_prob = 0.005  # 0.5% chance per minute during the night
    elif is_peak_morning or is_peak_evening:
        event_prob = 0.15   # 15% chance per minute during peak hours
    else:
        event_prob = 0.05   # 5% chance per minute during regular hours

    if holiday:
        event_prob *= 1.5  # Increase by 50% on holidays


    if random.random() < event_prob:
        if current_cars == 0:
            event = 'Entry'
            current_cars += 1
        elif current_cars == max_capacity:
            event = 'Exit'
            current_cars -= 1
        else:
            if is_peak_morning:
                event_weights = [0.7, 0.3] 
            elif is_peak_evening:
                event_weights = [0.3, 0.7]
            else:
                event_weights = [0.5, 0.5]

            event = random.choices(['Entry', 'Exit'], weights=event_weights)[0]
            if event == 'Entry':
                current_cars += 1
            else:
                current_cars -= 1

        events.append([current_time.strftime('%Y-%m-%d %H:%M'), event])

    current_time += datetime.timedelta(minutes=1)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['DateTime', 'Event'])
    writer.writerows(events)

print(f"Dataset generated")
