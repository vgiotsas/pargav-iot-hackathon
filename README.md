# pargav-iot-hackathon
Privacy Aware Research of Generic Anomalies and Visualisations

RIPE NCC IoT Hackathon Project

## Data format

per device CSV format: 1 minute sampling
```
timestamp (unix epoch), bandwidth up(kbits/s), bandwidth down(kbits/s), connections made, different ports accessed, different IPs accessed
```

Examples

tv.LAN.uncontrolled.csv:
```1570873590, 5, 2000, 10, 1, 1
1570873650, 4, 1900, 8, 1, 1
```

tv.WAN.idle.csv:
```1570873590, 5, 2000, 10, 1, 1
1570873650, 4, 1900, 8, 1, 1
```
roomba.LAN.idle.csv
``1570873590, 1, 1, 1, 12
1570873590, 2, 2, 2, 2
``
roomba.WAN.controlled.csv
```1570873590, 1, 1, 1, 1
1570873590, 2, 2, 2, 2
```
