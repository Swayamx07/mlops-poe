import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset


REFERENCE_FILE = "monitoring/data/reference.csv"
CURRENT_FILE = "monitoring/data/current.csv"
REPORT_FILE = "reports/evidently_report.html"


def main():
    print("Loading reference data...")
    reference_data = pd.read_csv(REFERENCE_FILE)

    print("Loading current data...")
    current_data = pd.read_csv(CURRENT_FILE)

    print("Running Evidently data drift analysis...")

    report = Report([
        DataDriftPreset()
    ])

    result = report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    result.save_html(REPORT_FILE)

    print("Evidently report generated successfully.")
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()