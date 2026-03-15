from flask import Flask, request, jsonify
import os
from printer import send_print_job        # Use the existing function
from validator import file_exists, file_not_empty, get_page_count

app = Flask(__name__)

@app.route("/print", methods=["POST"])
def print_file():
    data = request.get_json()
    filename = data.get("filename")

    if not filename or not os.path.exists(filename):
        return jsonify({"status": "error", "message": "File not found"}), 404

    # Simulate printing
    output_file = send_print_job(filename)

    # Validate printed output
    validation = {
        "exists": file_exists(output_file),
        "not_empty": file_not_empty(output_file),
        "page_count": get_page_count(output_file)
    }

    return jsonify({"status": "success", "output_file": output_file, "validation": validation}), 200

if __name__ == "__main__":
    app.run(debug=True)