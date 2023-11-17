"""Part 2 of workshop 7"""

from flask import Flask, request, render_template
import pyttsx3 as tts

app = Flask(__name__)

@app.route('/')
def main_func():
    """Runs on the main page startup when no route is added"""
    return '<form action="/setalarm" method="get"> \
            <input type="datetime-local" name="alarm"> \
            <input name="two"> \
            <input type="submit"> \
            </form>'


@app.route('/print_to_console')
def print_to_console():
    """Prints string to console"""
    print("print to console test")
    return "Hello print to console"


@app.route('/announcement')
def tts_request(announcement = "Hello text-to-speech example"):
    """Announces a string"""
    engine = tts.init()
    engine.say(announcement)
    engine.runAndWait()
    return "Hello text-to-speech example"


@app.route('/setalarm')
def setalarm():
    """Announces the alarm details after retrieveing them from the page"""
    alarm = request.args.get('alarm')
    tts_request(alarm)
    return main_func()


@app.route('/index')
def index():
    """Creates an index for the website"""
    notifications = ['Joe Biden pick Ron Klain as White House chief of staff - BBC News',
                     '146 cases per 100,000 people in exeter up 27 from last week - PHE Covid stats',
                     'ECM1400 Deadline reminder 4th December']
    return render_template('index.html', title='Daily Update', notifications=notifications)


if __name__ == '__main__':
    app.run()
