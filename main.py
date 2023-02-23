from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import datetime


class Users():
    def __init__(self):
        self.uptime = datetime.datetime.now()
        self.ip_list = []

def create_app(users_instance):
    app = Flask(__name__)
    app.config['Users'] = users_instance
    return app

users = Users()
app = create_app(users)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour", "10 per minute"],
    storage_uri="memory://",
)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route("/api/myip", methods=["GET"])
def get_user_address():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)  
        if ip not in app.config['Users'].ip_list: 
            app.config['Users'].ip_list.append(ip)
        retval = jsonify({'user ip': ip})
    else:
        ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        if ip not in app.config['Users'].ip_list: 
            app.config['Users'].ip_list.append(ip) 
        retval = jsonify({'user ip': ip})

    return retval

@app.route("/api/iplist", methods=["GET"])
def get_addresses_list():
    return jsonify({'users ip list': app.config['Users'].ip_list,
                    'uptime': str(datetime.datetime.now() - app.config['Users'].uptime)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)