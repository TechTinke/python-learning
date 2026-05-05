from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# TEMPLATE INHERITANCE - create one master HTML file that contains the skeleton of what each page will look like