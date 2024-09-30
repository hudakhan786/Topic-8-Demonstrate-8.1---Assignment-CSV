import csv
import matplotlib.pyplot as plt

# Function to read data from CSV
def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get the indexes for TMIN and TMAX
        tmin_index = header_row.index('TMIN')
        tmax_index = header_row.index('TMAX')
        date_index = header_row.index('DATE')
        station_index = header_row.index('NAME')

        dates, tmin, tmax, station_name = [], [], [], None
        for row in reader:
            dates.append(row[date_index])
            tmin.append(float(row[tmin_index]))
            tmax.append(float(row[tmax_index]))
            if not station_name:
                station_name = row[station_index]

    return dates, tmin, tmax, station_name

# Read data
dates, tmin, tmax, station_name = read_csv('data.csv')

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Plot TMIN
axs[0].plot(dates, tmin, label='TMIN', color='blue')
axs[0].set_title(f'{station_name} - TMIN')
axs[0].set_ylabel('Temperature (C)')

# Plot TMAX
axs[1].plot(dates, tmax, label='TMAX', color='red')
axs[1].set_title(f'{station_name} - TMAX')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Temperature (C)')

# Adjust layout and show plot
plt.tight_layout()
plt.show()
