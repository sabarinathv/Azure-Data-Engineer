# Stream Analytics related example queries

## To read data from json file - Input.json
```
SELECT City,
    Coordinates.Latitude,
    Coordinates.Longitude
INTO streamoutput
FROM streaminput
```

## IOT Simulator
https://azure-samples.github.io/raspberry-pi-web-simulator/

## Windowing Function examples

### Tumbling Window
SELECT *
INTO outputiot1
FROM inputiothub
HAVING Temperature > 27

```
SELECT deviceid, AVG(humidity) as avg_humidity, AVG(temperature) as avg_temperature
INTO outputiot1
FROM inputiothub
GROUP BY deviceid, TumblingWindow(second, 20)
```

### Hopping Window
```
SELECT deviceid, AVG(humidity) as avg_humidity, AVG(temperature) as avg_temperature
INTO outputiot1
FROM inputiothub
GROUP BY deviceid, HoppingWindow(second, 20, 2)
```

### Sliding Window
```
SELECT deviceid, AVG(humidity) as avg_humidity, AVG(temperature) as avg_temperature
INTO outputiot1
FROM inputiothub
GROUP BY deviceid, SlidingWindow(second, 20)
```

### The Session Window
```
SELECT deviceid, AVG(humidity) as avg_humidity, AVG(temperature) as avg_temperature
INTO outputiot1
FROM inputiothub
GROUP BY deviceid, SessionWindow(second, 5, 20);
```

### Snapshot Window
```
SELECT deviceid, AVG(humidity) as avg_humidity, AVG(temperature) as avg_temperature
INTO outputiot1
FROM inputiothub
GROUP BY deviceid, System. Timestamp();
```