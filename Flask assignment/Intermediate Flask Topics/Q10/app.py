from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run()
