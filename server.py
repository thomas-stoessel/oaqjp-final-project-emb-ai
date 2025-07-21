from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emot_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    resulting_emotions = emotion_detector(text_to_analyze)
    anger = resulting_emotions['anger']
    disgust = resulting_emotions['disgust']
    fear = resulting_emotions['fear']
    joy = resulting_emotions['joy']
    sadness = resulting_emotions['sadness']
    dominant_emotion = resulting_emotions['dominant_emotion']

    return (f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}.")

@app.route('/')
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
