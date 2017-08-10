# MASSCAN: Mass IP port scanner
This is a fastest Internet port scanner, It can scan the entire Internet in under 6 minutes, transmitting 10 million packets per second

## From
Masscan repository: [https://github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan)

## Usage
```
masscan -p80,8000-8100 10.0.0.0/8
```


## Build From Docker
```
docker build -t masscan .
```

## Run
```
docker run --rm -it image_name -p0-65535 --rate=10000 ip
```
