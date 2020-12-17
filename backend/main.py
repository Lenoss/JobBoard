from flask import Flask, jsonify
from api.advertisements import advertisements
from api.companies import companies
from api.cities import cities
from api.countries import countries
from api.contract_types import contract_types
from api.roles import roles
from api.auth import auth
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


app.register_blueprint(advertisements, url_prefix="/api/advertisements")
app.register_blueprint(companies, url_prefix="/api/companies")
app.register_blueprint(cities, url_prefix="/api/cities")
app.register_blueprint(countries, url_prefix="/api/countries")
app.register_blueprint(contract_types, url_prefix="/api/contract_types")
app.register_blueprint(roles, url_prefix="/api/roles")
app.register_blueprint(auth, url_prefix="/api/auth")

@app.route("/index")
@app.route("/")
def index():
    return 'Hello from home page'

if __name__ == "__main__":
    app.run(debug=True)