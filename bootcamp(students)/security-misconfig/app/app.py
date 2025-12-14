from flask import Flask, jsonify, request, send_from_directory
import os

from config import DEBUG_MODE
from utils import get_user_data
from secrets import ADMIN_KEY

app = Flask(__name__)

# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return "Security Misconfiguration Lab – Running"

# -------------------------
# QUESTION 1 – DEBUG CONFIG LEAK
# -------------------------
@app.route("/debug/config")
def debug_config():
    if DEBUG_MODE and request.headers.get("X-Debug") == "true":
        return jsonify({
            "environment": "production",
            "backup_location": "/internal/backup.env"
        })
    return "Forbidden", 403

# -------------------------
# QUESTION 2 – ROLE TRUST
# -------------------------
@app.route("/api/userinfo")
def userinfo():
    role = request.args.get("role", "user")
    return jsonify(get_user_data(role))

# -------------------------
# QUESTION 3 – PATH TRAVERSAL
# -------------------------
@app.route("/download")
def download():
    filename = request.args.get("file")
    # ❌ No validation
    return send_from_directory("/internal", filename)

# -------------------------
# QUESTION 4 – ADMIN PANEL
# -------------------------
@app.route("/admin/data")
def admin_data():
    key = request.args.get("key")
    if key == ADMIN_KEY:
        return jsonify({
            "status": "success",
            "flag": "SMC{h4rdc0d3d_s3cr3t_zz71}"
        })
    return "Unauthorized", 401

# -------------------------
# STATIC UI
# -------------------------
@app.route("/ui")
def ui():
    return send_from_directory("/static", "index.html")

@app.route("/admin")
def admin_ui():
    return send_from_directory("/static", "admin.html")

# -------------------------
# START SERVER
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
