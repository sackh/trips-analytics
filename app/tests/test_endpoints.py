def test_total_trips(test_app):
    start = "2020-04-03"
    end = "2020-04-19"
    response = test_app.get(f"/api/v1/total_trips?start={start}&end={end}")
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {"date": "2020-04-03", "total_trips": 2558},
            {"date": "2020-04-04", "total_trips": 1745},
            {"date": "2020-04-05", "total_trips": 1270},
            {"date": "2020-04-06", "total_trips": 2169},
            {"date": "2020-04-07", "total_trips": 2009},
            {"date": "2020-04-08", "total_trips": 2070},
            {"date": "2020-04-09", "total_trips": 2087},
            {"date": "2020-04-10", "total_trips": 1972},
            {"date": "2020-04-11", "total_trips": 1596},
            {"date": "2020-04-12", "total_trips": 1025},
            {"date": "2020-04-13", "total_trips": 1966},
            {"date": "2020-04-14", "total_trips": 1857},
            {"date": "2020-04-15", "total_trips": 1793},
            {"date": "2020-04-16", "total_trips": 2030},
            {"date": "2020-04-17", "total_trips": 1848},
            {"date": "2020-04-18", "total_trips": 1479},
            {"date": "2020-04-19", "total_trips": 1049},
        ]
    }


def test_average_fare_heatmap(test_app):
    date = "2020-08-17"
    response = test_app.get(f"/api/v1/average_fare_heatmap?date={date}")
    assert response.status_code == 200
    data = response.json()["data"]
    result = [
        {"s2id": "baad369d3", "fare": 45.46},
        {"s2id": "baad36a03", "fare": 33.76},
        {"s2id": "baad49689", "fare": 12.25},
        {"s2id": "baad49701", "fare": 17.44},
        {"s2id": "baad49707", "fare": 12.69},
        {"s2id": "baad49781", "fare": 6.0},
        {"s2id": "baad4e151", "fare": 19.72},
        {"s2id": "baad4e15b", "fare": 3.25},
        {"s2id": "baad4e15d", "fare": 13.95},
        {"s2id": "baad4e165", "fare": 24.47},
        {"s2id": "baad4e179", "fare": 20.69},
        {"s2id": "baad4e1f7", "fare": 16.43},
        {"s2id": "baad4e1ff", "fare": 22.69},
        {"s2id": "baad4e61f", "fare": 11.5},
        {"s2id": "baad4e663", "fare": 21.62},
        {"s2id": "baad4e665", "fare": 33.67},
        {"s2id": "baad4e66d", "fare": 9.94},
        {"s2id": "baad4e689", "fare": 26.25},
        {"s2id": "baad4e68f", "fare": 11.73},
        {"s2id": "baad4e697", "fare": 14.97},
        {"s2id": "baad4e6b1", "fare": 23.12},
        {"s2id": "baad4e8bd", "fare": 3.25},
        {"s2id": "baad4e96b", "fare": 39.97},
        {"s2id": "baad4eb09", "fare": 15.88},
        {"s2id": "baad4eb17", "fare": 28.95},
        {"s2id": "baad4eb3b", "fare": 17.69},
        {"s2id": "baad4eba5", "fare": 12.76},
        {"s2id": "baad4ebc3", "fare": 15.45},
        {"s2id": "baad4ebdf", "fare": 21.96},
        {"s2id": "baad510a7", "fare": 12.39},
        {"s2id": "baad510b9", "fare": 8.42},
        {"s2id": "baad510c5", "fare": 14.34},
        {"s2id": "baad5113d", "fare": 8.64},
        {"s2id": "baad5113f", "fare": 16.04},
        {"s2id": "baad51141", "fare": 7.25},
        {"s2id": "baad5130b", "fare": 5.99},
        {"s2id": "baad5130d", "fare": 11.79},
        {"s2id": "baad51313", "fare": 21.29},
        {"s2id": "baad51315", "fare": 6.12},
        {"s2id": "baad51335", "fare": 8.12},
        {"s2id": "baad51337", "fare": 16.27},
        {"s2id": "baad51339", "fare": 8.7},
        {"s2id": "baad5133f", "fare": 11.97},
        {"s2id": "baad51395", "fare": 7.45},
        {"s2id": "baad513a1", "fare": 7.95},
        {"s2id": "baad513a3", "fare": 6.25},
        {"s2id": "baad513bd", "fare": 8.25},
        {"s2id": "baad513e1", "fare": 24.78},
        {"s2id": "baad513e7", "fare": 28.88},
        {"s2id": "baad513e9", "fare": 11.17},
        {"s2id": "baad513eb", "fare": 12.92},
        {"s2id": "baad51a09", "fare": 23.99},
        {"s2id": "baad51a1b", "fare": 33.72},
        {"s2id": "baad51a25", "fare": 13.84},
        {"s2id": "baad51bd1", "fare": 15.87},
        {"s2id": "baad51bd3", "fare": 18.54},
        {"s2id": "baad51bdb", "fare": 22.75},
        {"s2id": "baad51bdd", "fare": 13.82},
        {"s2id": "baad51be5", "fare": 7.75},
        {"s2id": "baad51bff", "fare": 12.15},
        {"s2id": "baad51c01", "fare": 15.86},
        {"s2id": "baad51c29", "fare": 12.67},
        {"s2id": "baad51e01", "fare": 15.98},
        {"s2id": "baad51e79", "fare": 14.16},
        {"s2id": "baad56291", "fare": 31.0},
        {"s2id": "baad5630d", "fare": 10.54},
        {"s2id": "baad56509", "fare": 23.75},
        {"s2id": "baad56575", "fare": 20.32},
        {"s2id": "baad56c2f", "fare": 21.31},
        {"s2id": "baad56c47", "fare": 18.55},
        {"s2id": "baad56cc5", "fare": 7.75},
        {"s2id": "baad56ccd", "fare": 21.72},
        {"s2id": "baad56e83", "fare": 19.6},
        {"s2id": "baad56e85", "fare": 20.23},
        {"s2id": "baad56e8d", "fare": 18.64},
        {"s2id": "baad56f01", "fare": 20.57},
        {"s2id": "bab2a9d65", "fare": 26.81},
    ]
    assert set([tuple(di.items()) for di in data]) == set([tuple(d.items()) for d in result])


def test_average_speed_24hrs(test_app):
    date = "2020-09-25"
    response = test_app.get(f"/api/v1/average_speed_24hrs?date={date}")
    assert response.status_code == 200
    assert response.json() == {"data": [{"average_speed": 17.29}]}


def test_exceptions(test_app):
    start = "2020-04-33"
    end = "2020-04-19"
    response = test_app.get(f"/api/v1/total_trips?start={start}&end={end}")
    assert response.status_code == 400
    response = test_app.get(f"/api/v1/average_fare_heatmap?date={start}")
    assert response.status_code == 400
    response = test_app.get(f"/api/v1/average_speed_24hrs?date={start}")
    assert response.status_code == 400
