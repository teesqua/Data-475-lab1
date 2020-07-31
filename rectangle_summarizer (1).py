import csv
from statistics import mean

with open("DATA475_lab_rectangles_data.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)

    areas = [float(line[1]) * float(line[2]) for line in reader]


    # for line in reader:
    #     #print(line)
    #     w = float(line[1])
    #     l = float(line[2])
    #     area = w*l
    #     areas.append (areas)


    # print(len(areas))
    # print(sum(areas))
    # print(mean(areas))
    # print(max(areas))
    # print(min(areas))
    

    column_names = {
        "Total Count": len(areas),
        "Total Area": sum(areas),
        "Average Area": mean(areas),
        "Max Area": max(areas),
        "Min Area": min(areas),
    }

    for key, value in column_names.items():
        print(f"{key}: {value}")

    with open("summary.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(column_names.keys())
        writer.writerow(column_names.values())





    
    