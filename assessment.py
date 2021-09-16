import csv

# Reads data from csv file and stores it in data rows
def get_weather_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            csvreader = csv.DictReader(file, delimiter=',')
            data = list(csvreader)
            for row in data:
                row['date'] = float(row['date'])
                row['temperature_c'] = float(row['temperature_c'])
        print type(data[0]['station_id']), type(data[0]['date']), type(data[0]['temperature_c'])
    except IOError:
        print "Could not read file", filename
    return data

# Returns station_id and date of lowest temperature occurrence
def get_lowest_temp_occurrence(data):
    min_station_id = data[0]['station_id']
    min_date = data[0]['date']
    min_temp = data[0]['temperature_c']
    for pt in data:
        if pt['temperature_c'] < min_temp:
            min_temp = pt['temperature_c']
            min_date = pt['date']
            min_station_id = pt['station_id']
    return min_station_id, min_date

# Returns station_id with the highest temperature fluctuation
def get_station_with_highest_temp_fluctuation(data):
    station_dict = get_sorted_station_dict(data)
    max_fluctuation = 0
    station_id = ''
    for key in station_dict:
        curr_fluctuation = calculate_total_fluctuation(station_dict[key])
        if (curr_fluctuation > max_fluctuation):
            max_fluctuation = curr_fluctuation
            station_id = key
    return station_id

# Returns station_id with the highest temperature fluctuation in range
def get_station_with_highest_temp_fluctuation_in_range(data, start_date, end_date):
    station_dict = get_sorted_station_dict(data)
    max_fluctuation = 0
    station_id = ''
    for key in station_dict:
        start_i = get_date_location(station_dict[key], start_date)
        end_i = get_date_location(station_dict[key], end_date)
        curr_fluctuation = calculate_total_fluctuation(station_dict[key][start_i:end_i])
        max_fluctuation = curr_fluctuation
        station_id = key
    return station_id

# Find index of date using binary search
def get_date_location(data, target_date):
    left_i = 0
    right_i = len(data)
    mid_i = left_i + int((right_i - left_i) / 2.0)
    while (data[mid_i]['date'] != target_date):
        if (target_date > data[mid_i]['date']):
            left_i = mid_i
        else:
            right_i = mid_i
        mid_i = left_i + int((right_i - left_i) / 2)
    return mid_i 

# Port data into a dictionary where station data is sorted by date per station
def get_sorted_station_dict(data):
    station_dict = {}
    for row in data:
        if row['station_id'] not in station_dict:
            station_dict[row['station_id']] = []
        station_dict[row['station_id']].append(row)
    for key in station_dict:
        station_dict[key].sort(key=get_date)
    return station_dict

# Gets the date value
def get_date(data):
    return data.get('date')

# Calculates total fluctuation of weather temp from array of data
def calculate_total_fluctuation(data):
    total = 0
    for i in range(0, len(data)-1):
        total += abs(data[i]['temperature_c'] - data[i+1]['temperature_c'])
    return total
