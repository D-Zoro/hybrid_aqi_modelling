# Data Dictionary

## Overview
This document outlines the schemas for raw, processed, and feature datasets within AiroSense. Columns follow ISO naming standards and SI units where applicable.

## Raw Data Schemas
### Sentinel-5P (NO2)
| Column | Type | Description |
| --- | --- | --- |
| `observation_id` | UUID | Unique identifier per GEE tile download |
| `timestamp_utc` | TIMESTAMP | Measurement time (UTC) |
| `latitude` | FLOAT | Tile centroid latitude |
| `longitude` | FLOAT | Tile centroid longitude |
| `value_mol_m2` | FLOAT | NO2 column density |
| `cloud_fraction` | FLOAT | Cloud coverage ratio |
| `qa_value` | INT | Quality assurance score |

### OpenWeather One Call
| Column | Type | Description |
| --- | --- | --- |
| `station_id` | STRING | Synthetic ID generated from lat/lon rounding |
| `timestamp_utc` | TIMESTAMP | Hourly forecast time |
| `temperature_k` | FLOAT | Temperature (Kelvin) |
| `humidity_pct` | FLOAT | Relative humidity (%) |
| `pressure_hpa` | FLOAT | Surface pressure |
| `wind_speed_ms` | FLOAT | Wind speed (m/s) |
| `wind_direction_deg` | FLOAT | Wind direction |
| `pm10_ug_m3` | FLOAT | PM10 estimates (if available) |

### CPCB / OpenAQ Ground Truth
| Column | Type | Description |
| --- | --- | --- |
| `station_code` | STRING | CPCB site identifier |
| `timestamp_local` | TIMESTAMP | Local timestamp |
| `aqi` | FLOAT | Calculated AQI |
| `pm25_ug_m3` | FLOAT | PM2.5 concentration |
| `pm10_ug_m3` | FLOAT | PM10 concentration |
| `no2_ug_m3` | FLOAT | Nitrogen dioxide |
| `so2_ug_m3` | FLOAT | Sulphur dioxide |
| `co_mg_m3` | FLOAT | Carbon monoxide |
| `o3_ug_m3` | FLOAT | Ozone |

## Processed Schema
Stored as partitioned Parquet in `processed/<region>/<yyyy>/<mm>/<dd>/`.

| Column | Type | Notes |
| --- | --- | --- |
| `station_id` | STRING | Hash of nearest CPCB station |
| `timestamp_utc` | TIMESTAMP | Synchronized hourly timestamp |
| `aqi_label` | STRING | Classes (`Good`, `Satisfactory`, ... ) |
| `aqi_value` | FLOAT | Fused AQI estimate |
| `no2_column_density` | FLOAT | Resampled satellite value |
| `weather_temp_c` | FLOAT | Kelvin to Celsius |
| `wind_speed_ms` | FLOAT | Clipped 0-30 range |
| `humidity_pct` | FLOAT | |
| `rain_mm` | FLOAT | Derived from precipitation |
| `missing_flags` | JSON | Column-level missing indicators |

## Feature Store (Feast)
**Primary keys:** `entity_id` (station_id), `event_timestamp`

| Feature | Type | Definition |
| --- | --- | --- |
| `aqi_lag_1h` | FLOAT | Previous hour AQI |
| `aqi_lag_6h` | FLOAT | 6-hour lag |
| `aqi_rolling_mean_24h` | FLOAT | 24-hour mean |
| `no2_trend_6h` | FLOAT | Linear trend slope |
| `wind_u_component` | FLOAT | Derived from speed + direction |
| `dew_point_c` | FLOAT | Computed from humidity/temperature |
| `holiday_flag` | BOOL | Derived from region calendar |
| `industrial_activity_index` | FLOAT | Optional external data |

## Data Retention
- Raw: 180 days (Glacier after 30 days)
- Processed: 365 days (prefix partitioning)
- Feature store offline: 365 days
- ML artifacts: Keep all production models, prune experiments > 180 days
