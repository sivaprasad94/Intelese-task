from flask import request, Flask, render_template
app = Flask(__name__)
from surge_peaks import audio_analysis
from keras_cnn_model import keras_cnn_model

@app.route("/post_field", methods=["GET", "POST"])
def identify_peaks():
    url = request.form
    video_url = url['Video or Audio URL']
    print(video_url)
    x, f = audio_analysis.download_video_file(video_url)
    if f.endswith('wav'):
        a,f = audio_analysis.split_audio(x, f)
    else:
        a, f = audio_analysis.convet_to_audio(x,f)
        a, f = audio_analysis.split_audio(a, f)
    seperated_peaks = audio_analysis.identify_peaks(a, f)
    model = keras_cnn_model.load_cnn_model()
    test_Data = keras_cnn_model.get_features_detected_peaks(seperated_peaks)
    labels = keras_cnn_model.get_predicted_label(model, test_Data, seperated_peaks)
    return labels

@app.route("/form", methods=["GET"])
def get_form():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')