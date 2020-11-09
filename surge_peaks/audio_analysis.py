import librosa
from scipy.signal import chirp, find_peaks, peak_widths
import matplotlib.pyplot as plt
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from playsound import playsound
from os import listdir
from os.path import isfile, join
from scipy.io import wavfile
import librosa
import moviepy
import ntpath
import glob
import requests
import moviepy.editor as mp 


def download_video_file(url):
    
    if str(url).endswith('mp4'):
        file_name = 'sample_video.mp4'
        local_video_filepath = './input_video/' + file_name
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(local_video_filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
    else:
        file_name = url.split('/')[-1]
        files = glob.glob('./temp/*')
        for f in files:
            os.remove(f)
        files = glob.glob('./detected_peaks/*')
        for f in files:
            os.remove(f)
        files = glob.glob('./extracted_peaks/*')
        for f in files:
            os.remove(f)
        local_video_filepath = './input_audio/' + file_name
        response = requests.get(url, stream=True)
        with open(local_video_filepath, "wb") as handle:
            for data in response.iter_content():
                handle.write(data)
    return local_video_filepath, file_name

def convet_to_audio(video_filepath, file_name):
    file_name = file_name
    video_filepath = video_filepath
    # Insert Local Video File Path  
    clip = mp.VideoFileClip(video_filepath) 
    filename = ntpath.basename(video_filepath).split('.')[0]
    # Insert Local Audio File Path 
    audio_filepath ='./extracted_audio/' +  filename + '.wav'
    print(audio_filepath)
    clip.audio.write_audiofile(audio_filepath) 
    return audio_filepath, file_name


def split_audio(audio_filepath, f):
    file_name = f.replace('.wav', '')
    print('split to======',audio_filepath)
    sound = AudioSegment.from_mp3(audio_filepath)
    chunks = split_on_silence(sound,min_silence_len=280,silence_thresh=-33,keep_silence=150)
    files = glob.glob('./temp/*')
    for f in files:
        os.remove(f)
    for i, chunk in enumerate(chunks):
            chunk.export('./temp/' + file_name + "{}.wav".format(i), format="wav")
    audio_chunks = [f for f in listdir('./temp') if isfile(join('./temp', f))]
    return audio_chunks, file_name


def identify_peaks(audio_chunks, file_name):
    for i, chunk in enumerate(audio_chunks):
        y, sr = librosa.load('./temp/' + chunk, sr=None)
        peaks, _ = find_peaks(y)
        results_full = peak_widths(y, peaks)
        list1 =list(map(int,list(results_full[2])))
        list2 = list(map(int,list(results_full[3])))
        try:
            audio = y[min(list1): max(list2)]
            wavfile.write('./detected_peaks/' + 'peak{}'.format(i)+ '_{}'.format(chunk),sr, audio)
        except:
            pass
    surge_peaks = [f for f in listdir('./detected_peaks/') if isfile(join('./detected_peaks/', f))]
    return surge_peaks