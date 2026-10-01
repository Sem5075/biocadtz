import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    hostname = os.environ.get("HOSTNAME", "unknown")
    node_name = os.environ.get("NODE_NAME", "unknown")
    pod_name = os.environ.get("POD_NAME", hostname)
    namespace = os.environ.get("POD_NAMESPACE", "unknown")
    image_tag = os.environ.get("IMAGE_TAG", "unknown")

    return f"""
<html>
<head><title>testapp</title></head>
<body>
  <h1>testapp</h1>
  <ul>
    <li><b>Pod / Container:</b> {pod_name}</li>
    <li><b>Node:</b> {node_name}</li>
    <li><b>Namespace:</b> {namespace}</li>
    <li><b>Hostname:</b> {hostname}</li>
    <li><b>Image Tag:</b> {image_tag}</li>
    <li><b>здесь могла быть ваша реклама</b></li>
  </ul>
</body>
</html>
""", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=32777)
