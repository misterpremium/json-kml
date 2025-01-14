# json-kml
Script to conver json to kml
Remove "semanticSgmets" lavel and the "rawSginals" to the end of file:
FROM:
```
{
  "semanticSegments": [
    {
      "startTime": "1996-10-09T15:00:00.000+02:00",
      "endTime": "1996-10-10T02:00:00.000+02:00",
      "startTimeTimezoneUtcOffsetMinutes": 120,
      "endTimeTimezoneUtcOffsetMinutes": 120,
      "visit": {
        "hierarchyLevel": 0,
        "probability": 1.0,
        "topCandidate": {
          "placeId": "ChIJt-ItlvxLQg0RQmIE9K7_MoY",
          "semanticType": "UNKNOWN",
          "probability": 1.0,
          "placeLocation": {
            "latLng": "40.5102852°, -3.3477139°"
          }
        }
      }
    },
```
To:
```
[
  {
      "startTime": "1996-10-09T15:00:00.000+02:00",
      "endTime": "1996-10-10T02:00:00.000+02:00",
      "startTimeTimezoneUtcOffsetMinutes": 120,
      "endTimeTimezoneUtcOffsetMinutes": 120,
      "visit": {
        "hierarchyLevel": 0,
        "probability": 1.0,
        "topCandidate": {
          "placeId": "ChIJt-ItlvxLQg0RQmIE9K7_MoY",
          "semanticType": "UNKNOWN",
          "probability": 1.0,
          "placeLocation": {
            "latLng": "40.5102852°, -3.3477139°"
          }
        }
      }
    },
```
execute ./covert.sh
