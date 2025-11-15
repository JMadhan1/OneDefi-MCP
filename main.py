import os
import logging
from flask import request
from app import app

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import routes after app is created
try:
    import routes_simple  # noqa: F401
    logger.info("Routes imported successfully")
except Exception as e:
    logger.error(f"Error importing routes: {e}", exc_info=True)

# Register error handlers
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return "Page not found. Please check the URL.", 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}", exc_info=True)
    return "Internal server error. Please check the logs.", 500

# Get port from environment variable (for Render deployment)
port = int(os.environ.get("PORT", 5000))
debug = os.environ.get("FLASK_ENV") != "production"

if __name__ == "__main__":
    logger.info(f"Starting Flask app on port {port}")
    logger.info(f"Available routes: {[str(rule) for rule in app.url_map.iter_rules()]}")
    app.run(host="0.0.0.0", port=port, debug=debug)
