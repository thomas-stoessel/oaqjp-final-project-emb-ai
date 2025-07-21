"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-provided text.

Author(Learner): [thomas-stoessel]
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emot_detector():
    """
    This function receives the text from the HTML interface and runs emotion analysis over it.
    The output returned shows the confidence score across all emotions and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    resulting_emotions = emotion_detector(text_to_analyze)
    anger = resulting_emotions['anger']
    disgust = resulting_emotions['disgust']
    fear = resulting_emotions['fear']
    joy = resulting_emotions['joy']
    sadness = resulting_emotions['sadness']
    dominant_emotion = resulting_emotions['dominant_emotion']

    if anger is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
        )


@app.route('/')
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
