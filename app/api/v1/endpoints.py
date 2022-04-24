from datetime import datetime
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd
from fastapi import APIRouter, Depends, HTTPException

from app.api.v1.dependencies import convert_miles_to_km, convert_seconds_to_hours, get_s2_id

router = APIRouter()


async def read_trips_data() -> pd.DataFrame:
    """Return trips data as pandas dataframe.

    :return: class:`pd.DataFrame`
    """
    file_path = Path(__file__).parent.parent.parent.parent / Path(
        "data/chicago_taxi_trips_2020.parquet"
    )
    return pd.read_parquet(file_path)


@router.get("/total_trips")
async def total_trips(
    start: str, end: str, trips_df: pd.DataFrame = Depends(read_trips_data)
) -> Dict:
    """Retrun total number of trips per day between `start` and `end`, based on the pickup
    time of the trip.
    """
    try:
        sdate = datetime.strptime(start, "%Y-%m-%d").date()
        edate = datetime.strptime(end, "%Y-%m-%d").date()
    except ValueError as err:
        raise HTTPException(status_code=400, detail=f"Invalid start or end date, Error: {err}")

    trips_df["pickup_date"] = trips_df["trip_start_timestamp"].dt.date
    df = trips_df[(trips_df.pickup_date >= sdate) & (trips_df.pickup_date <= edate)]
    trips_per_date = df["pickup_date"].value_counts()
    trips_dict = trips_per_date.to_dict()
    trip_tuples = list(sorted(trips_dict.items(), key=lambda x: x[0]))
    return {"data": [{"date": k.strftime("%Y-%m-%d"), "total_trips": v} for k, v in trip_tuples]}


@router.get("/average_fare_heatmap")
async def average_fare_heatmap(
    date: str, trips_df: pd.DataFrame = Depends(read_trips_data)
) -> Dict:
    """Return The average fare per pick up location S2 ID at level 16 for the given date,
    based on the pickup time of the trip.
    """
    try:
        inp_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as err:
        raise HTTPException(status_code=400, detail=f"Invalid start or end date, Error: {err}")

    trips_df["pickup_date"] = trips_df["trip_start_timestamp"].dt.date
    df = trips_df[trips_df.pickup_date == inp_date]
    df = df[(df["pickup_longitude"].notna()) & (df["pickup_longitude"].notna())]
    df["s2id"] = df.apply(
        lambda row: get_s2_id(row.pickup_longitude, row.pickup_longitude), axis=1
    )
    df = df[["s2id", "fare"]]
    df = df.groupby(["s2id"]).mean()
    df = df.round(2)
    trips_dict = df.to_dict("split")
    return {
        "data": [
            {"s2id": k, "fare": v[0]} for k, v in zip(trips_dict["index"], trips_dict["data"])
        ]
    }


@router.get("/average_speed_24hrs")
def average_speed_24hrs(date: str, trips_df: pd.DataFrame = Depends(read_trips_data)) -> Dict:
    """Average speed of trips that ended in the past 24 hours from the provided date."""
    try:
        inp_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as err:
        raise HTTPException(status_code=400, detail=f"Invalid start or end date, Error: {err}")
    trips_df["end_date"] = trips_df["trip_end_timestamp"].dt.date
    df = trips_df[trips_df.end_date == inp_date]
    df = df[(df["trip_miles"].notna()) & (df["trip_seconds"].notna())]
    df["trip_time_hours"] = df["trip_seconds"].apply(lambda x: convert_seconds_to_hours(x))
    df["trip_distance_km"] = df["trip_miles"].apply(lambda x: convert_miles_to_km(x))
    df["trip_speed"] = df.trip_distance_km / df.trip_time_hours
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    avg_speed = round(df["trip_speed"].mean(), 2)
    return {"data": [{"average_speed": avg_speed}]}
