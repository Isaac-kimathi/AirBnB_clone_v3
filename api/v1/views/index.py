#!/usr/bin/python3
"""index"""

from api.v1.views import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status of API"""
    return jsonify({"status": "OK"})

@app.errorhandler(404)
def not_found(error):
    """404 error handling"""
    return make_response(jsonify({'error': "Not found"}), 404)


