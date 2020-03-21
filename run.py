from flask import Flask 

app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route('/')
def main():
    return f'Hello, world from hostname: { app.config.get("HOSTNAME") }<br>Running in namespace: { app.config.get("NAMESPACE")' 

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
