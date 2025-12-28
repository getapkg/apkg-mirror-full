from flask import Flask, jsonify, send_from_directory, abort, render_template, request
from pathlib import Path
import json

app = Flask(__name__)

RELEASES_DIR = Path(__file__).parent / "releases"
RELEASES_DIR.mkdir(parents=True, exist_ok=True)

PKG_JSON_PATH = Path(__file__).parent / "packages.json"

@app.route("/")
def index():
    query = request.args.get("q", "")
    if not PKG_JSON_PATH.exists():
        packages = {}
    else:
        with open(PKG_JSON_PATH, "r") as f:
            data = json.load(f)
            packages = data.get("packages", {})
    return render_template("index.html", packages=packages, query=query)

@app.route("/releases/0.1/packages.json")
def packages_json():
    if not PKG_JSON_PATH.exists():
        return jsonify({"packages": {}})
    try:
        with open(PKG_JSON_PATH, "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Failed to read packages.json: {e}"}), 500

@app.route("/releases/0.1/<zipfile>")
def serve_zip(zipfile):
    zip_path = RELEASES_DIR / zipfile
    return send_from_directory(RELEASES_DIR, zipfile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
