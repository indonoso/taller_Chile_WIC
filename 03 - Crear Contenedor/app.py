from flask import Flask, render_template
from visualization import create_vis
import os

app = Flask(__name__)


@app.route('/')
def display_super_vis():
    if not ('vis.html' in os.listdir('templates')):
        create_vis()

    return render_template('vis.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
