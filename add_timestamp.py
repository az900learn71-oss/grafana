import csv
import datetime

with open('website_traffic.csv', 'r') as infile, open('website_traffic_with_time.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write header
    header = next(reader)
    writer.writerow(header + ['Timestamp'])

    # Write data rows
    start_date = datetime.datetime(2023, 1, 1)
    for i, row in enumerate(reader):
        # Adding some hour/minute variation for fun
        timestamp = start_date + datetime.timedelta(days=i, hours=i%24, minutes=i%60)
        writer.writerow(row + [timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')])
