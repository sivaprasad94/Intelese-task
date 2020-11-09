import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
# Libraries for Classification and building Models
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPool2D, Dropout
from tensorflow.keras.utils import to_categorical 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import librosa
def load_cnn_model():
    model = tf.keras.models.load_model('./saved_model/my_model')
    return model

def get_features_detected_peaks(surge_peaks):
    test_features = []
    for i in surge_peaks:
        X, sample_rate = librosa.load('./detected_peaks/' + i, res_type='kaiser_fast') 
        # We extract mfcc feature from data
        mels = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T,axis=0)        
        test_features.append(mels)
    return np.array(test_features)
	
def get_predicted_label(model, test_Data, seperated_peaks):
    df = pd.read_csv("./dataset/UrbanSound8K.csv")
    test_Data = test_Data.reshape(len(test_Data),16, 8, 1 )
    classes = {}
    try:
        preds = model.predict(test_Data)
        preds = preds.argmax(axis=-1)
        
        print(preds)
        print(seperated_peaks)
        for i, j in zip(seperated_peaks , preds):
            label = (df[df.classID==j]['class'].unique()[0])
            classes[i]=label
    except:
        classes['Error:200']='No Peaks Found'
    return classes
    
    
    