import csv

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
