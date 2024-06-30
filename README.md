# WEATHER API USING FAST API

This is a local API for fetching weather data from 'http://api.weatherapi.com/v1'. The API can be deployed directly on the root OS or through a docker container. 

## USAGE (Docker):


1. Clone the repository to your local PC and change directory to the root of the repository:
```
cd Weather-API-FastAPI 
```
2. Build the docker image:
```
docker build -t weather-app .
```
3. Run the docker image:
>1. Run the docker image without mounting the directory as volume:
>```
>docker run -it --rm -p 8000:8000 weather-app
>```
>2. Run the docker image with mounting the directory as volume. You can make changes directly into the folder and uvicorn will reload upon detecting changes in the files:
>```
>docker run -it --rm -p 8000:8000 -v $(pwd):/Weather-app  weather-app
>```


## USAGE (CLI):


1. Clone the repository to your local PC and change directory to the root of the repository:
```
cd Weather-API-FastAPI 
```
2. Build the docker image:
```
pip3 install -r requirements.txt
```
3. Run the docker image:
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```