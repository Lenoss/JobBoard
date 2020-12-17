from flask import Blueprint, jsonify, json, request, abort
from Models.roles import Roles
roles = Blueprint("role", __name__)


@roles.route("/")
def getall():
    """ Get all element from role """
    try:
        elements = Roles().get_all_elements()
    except Exception as identifier:
        return abort(400, identifier)
    data = jsonify(elements)
    data.statut_code = 200
    return data


@roles.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from roles by id """
    try:
       elements = Roles().get_one_element(id)
    except Exception as identifier:
        return abort(400, identifier)
    if elements is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        data = jsonify(elements)
        data.statut_code = 200
        return data


@roles.route("/", methods=['POST'])
def post():
    """ get post from front to insert element into the database """
    try:
        elements = Roles().post(request.form["title"])
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(400, identifier)


@roles.route("/", methods=['PUT'])
def put():
    """ get put from front to update element into the database """
    elementFromDB = Roles().get_one_element(request.form["role_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")  
    else:
        try:
            elements = Roles().put(request.form["title"], request.form["role_id"])
            return elements
        except Exception as identifier:
            return abort(400, identifier)


@roles.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from roles by id """
    elementFromDB = Roles().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.") 
    else:
        try:
            elements = Roles().delete_element(id)
            result = jsonify(elements)
            result.statut_code = 200
            return result
        except Exception as identifier:
            return abort(500, identifier) 