import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
<html>
<head><title>tzapp</title></head>
<body>
  <h1>tzapp</h1>
<b>Hello world</b>
</body>
</html>
""", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=32777)
