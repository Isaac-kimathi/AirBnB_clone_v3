#!/usr/bin/python3
"""index"""

from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    """status of API"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def count():
    """
    Retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})

@app.errorhandler(404)
def not_found(error):
    """404 error handling"""
    return make_response(jsonify({'error': "Not found"}), 404)
