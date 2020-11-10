# Intelese-task
1. Build an tensorflow  or keras model that can identify high peak in an audio by separating it from a video data that is caused by a surge, example gunshot accident scream etc

2. Build a flask api where the API can receive the video url or audio url to be passed as an argument

3. The program should be able to provide the output via response or stored locally as a file 

4. Also Dockerize the model such that the API is exposed to the port number 0.0.0.0:8080 or localhost:5000 as per the arguments passed.

Implemented Solution:

Step.1: Get Video or Audio URL as argument from Flask API. 

Step.2: Download Video or Audio using requests.

Step.3: If video, convert it to audio

Step.4: Split audio based on scilence 

Step.5: Identify surge peaks using scipy audio signal processing and extracting the peak signal duration.  

Step.6: Keras model trained on Urbansound8K dataset to classify audios belinging to 1. Air Conditioner 2. Car Horn 3. Dog Bark 4.Drilling
        5. Gun Shots 6. Drilling 7. Jack Hammer 8. Engine Idiling 9. Siren 10. Street Music
        
Step.7: Posting the response through Flask API

Step.8: Dockerize the model to the port number localhost:5000

Steps to setup setup and run the reopository:

1. Colne the repository

2. Build the docker using "docker build -t dockerfile ."

3. Run the docker using 'docker run -p 5000:5000 dockerfile:latest'

4. open link http://localhost:5000/form to enter the url of video or audio
        
        
        
Approach 2: To identify high peaks (Not yet Implemented)

Step.1: Collecting data related to gunshot, acident, scream (Open source dataset Urbansound8k can be used)

Step.2: Converting the audiofile as Spectrogram images

Step.3: Labeling the Spectrogram images using LabelImg or Labelme tools (Identifying the peak patterns in Spectrogram manually and generating the labels)

Step.4: Training object detection models to identity peaks in spectrograms 

Step.5: Extracting the detected part of the image as peak

Step.6: Convert back the detected part as Audio



