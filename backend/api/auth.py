from flask import Flask, Blueprint, request, jsonify, abort
from flask_cors import CORS, cross_origin
from flask_bcrypt import *
from Models.auth import Auth
from flask_login import LoginManager

auth = Blueprint("auth", __name__)
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(auth)
login_manager = LoginManager()
login_manager.init_app(app)


@auth.route("/login", methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def login():
    """ get post from front to insert element into the database """
    username = request.form["username"]
    password = request.form["password"]
    user = Auth().findbyname(username)
    if len(user) == 0:
        return abort(400, "Utilisateur inconnu")
    else:
        verif = bcrypt.check_password_hash(user[0]["password"], password)  # returns True
        if verif is True:
            login_user(user)
            # je dois faire la connexion
            data = jsonify("login_user")
            data.statut_code = 200
            return data
        else:
            return abort(400, "Mot de passe incorrect")


@auth.route("/register", methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def register():
    """ get post from front to insert element into the database """
    elements = Auth().findbyname(request.form["username"])
    if len(elements) != 0:
        return abort(400, "Il existe déjà un utilisateur avec ce nom d'utilisateur")
    else:
        try:
            elements = Auth().register( request.form["username"], request.form["email"], request.form["password"])
            result = jsonify(elements)
            result.statut_code = 201
            return result
        except Exception as identifier:
            return abort(500, identifier)
        