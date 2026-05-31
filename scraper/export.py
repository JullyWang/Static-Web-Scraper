import csv
import pandas as pd 

def export_csv(data, filename):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
        ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=data[0].keys()
        )

        writer.writeheader()
        writer.writerows(data)

    print(f"[INFO] Exported {len(data)} rows to {filename}")

def export_excel(data, filename):
    df = pd.DataFrame(data)

    df.to_excel(filename, index=False)

    print(f"[INFO] Exported {len(data)} rows to {filename}")

