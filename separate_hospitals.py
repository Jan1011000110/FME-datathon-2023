import pandas as pd

def separate_hospitals(data):
    hospitals = {}

    for i in range(len(data)):
        row = data.iloc[i]

        hospital = "-".join(row['ORIGEN'].split("-")[0:2])

        if not hospital in hospitals:
            hospitals[hospital] = [row]
        else:
            hospitals[hospital].append(row)


