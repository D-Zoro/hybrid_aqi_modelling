"""Generate synthetic air quality dataset for local testing."""

from __future__ import annotations

import csv
from datetime import datetime, timedelta
from pathlib import Path
from random import gauss, random

OUTPUT_PATH = Path(__file__).resolve().parents[2] / "data/mock" / "synthetic_dataset.csv"


def main() -> None:
    start = datetime(2025, 1, 1)
    rows = []
    for hour in range(48):
        ts = start + timedelta(hours=hour)
        base_pm25 = 60 + gauss(0, 10)
        rows.append(
            {
                "station_code": "DL001",
                "timestamp_local": (ts).isoformat(),
                "aqi": base_pm25 * 1.5,
                "pm25_ug_m3": max(5, base_pm25),
                "pm10_ug_m3": max(10, base_pm25 * 1.6),
                "no2_ug_m3": max(5, base_pm25 * 0.6),
                "wind_speed_ms": abs(gauss(3, 1)),
                "humidity_pct": min(95, max(30, 60 + gauss(0, 5))),
                "temperature_c": 25 + gauss(0, 2) - 0.1 * hour,
                "rain_mm": max(0, gauss(0.5, 0.8) - 0.5),
                "is_holiday": int(random() > 0.9),
            }
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote synthetic dataset to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
