import os
import csv
import datetime

folder_path = "idle_res_us"
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"): 
        results = []
        #try:
        with open(folder_path + "/" + filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #if line_count == 0:
                #    results.append(row)
                #    line_count = 1
                #    continue
                #else:
                try:
                    date_time_obj = datetime.datetime.strptime(row[0], '%Y-%m-%d,%H:%M:%S')
                    timestamp = int(datetime.datetime.timestamp(date_time_obj))
                    row[0] = timestamp
                    results.append(row)
                except:
                    pass
        if len(results) > 1:
            with open(folder_path + "_timestamp/" + filename, mode='w') as results_file:
                results_writer = csv.writer(results_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in results:
                    print(row)
                    results_writer.writerow(row)
        #except:
        #    print("Skipping file: " + filename)
    else:
        continue