import pandas as pd

file_path = str(input())

with open(file_path, 'r') as file:
    lines = file.readlines()

time_values = []
angular_velocity_values = []

for line in lines:
    values = line.strip().split()
    time_values.append(float(values[0]))
    angular_velocity_values.append(float(values[1]))

data = pd.DataFrame({'time': time_values, 'angular_velocity': angular_velocity_values})

extrema = [] 
last_angular_velocity = data['angular_velocity'].iloc[0]

for index, row in data.iterrows():
    current_angular_velocity = row['angular_velocity']
    if (current_angular_velocity > last_angular_velocity and 
        last_angular_velocity < data['angular_velocity'].iloc[index + 1]) or \
       (current_angular_velocity < last_angular_velocity and 
        last_angular_velocity > data['angular_velocity'].iloc[index + 1]):
        extrema.append(index)

    last_angular_velocity = current_angular_velocity

slope_sum = 0
count = 0

for i in range(1, len(extrema)):
    start_index = extrema[i - 1]
    end_index = extrema[i]

    slope_sum += (data['angular_velocity'].iloc[end_index] - data['angular_velocity'].iloc[start_index]) / \
                 (data['time'].iloc[end_index] - data['time'].iloc[start_index])
    count += 1

average_slope = slope_sum / count if count > 0 else 0

print("Средний угловой коэффициент между экстремумами:", average_slope)
