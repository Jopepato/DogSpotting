# DogSpotting
API created using Flask. It will allow the user to send an url of a dog image and will return the number and positions of the dogs within the image. Built with imageai.

## Install
Download the weights for the neural network [here](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5).
And place them in this project folder.
Run the docker compose file to install all the dependencies and create the build.
```
docker-compose up --build -d
```
It will install all the dependencies for python and start the service in the port 80. With the `-d`flag we will indicate it to run in the background.

## Usage
Send the url of a dog image in a json request with the method POST. It will return the number an array of the dogs within the image.
It will have to be requested in the `/predict`route.

### Example
Using the following image:
![dogs](/images/dogs.jpg)

We will just send the following json to our api (using the url of the image)
![jsonToSend](/images/exampleJSON.png)

And will return us the response with the dogs within the image.
![responseJSON](/images/returnJSON.png)

## Example in jupyter notebook and questions answered
An example for several images of dogs can be seen in a Jupyter notebook in the folder `jupyterExample`. As well as the answers to the questions asked.

## Credits
Implemented with the detection library imageai.