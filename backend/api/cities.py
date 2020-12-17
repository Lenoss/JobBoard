from flask import Blueprint, jsonify, json, request, abort
from Models.cities import Cities
from flask_cors import CORS, cross_origin

cities = Blueprint("city", __name__)
CORS(cities)

@cities.route("/")
def getall():
    """ Get all element from cities """
    elements = Cities().get_all_elements()
    data = jsonify(elements)
    data.statut_code = 200
    return data

@cities.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from cities by id """
    elements = Cities().get_one_element(id)
    if elements is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        data = jsonify(elements)
        data.statut_code = 200
        return data

@cities.route("/", methods=['POST'])
def post():
    """ get post from front to insert element into the database """
    try:
        elements = Cities().post( request.form["city_name"], request.form["country_id"],  request.form["zipcode"])
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(500, identifier)


@cities.route("/", methods=['PUT'])
def put():
    """ get put from front to update element into the database """
    elementFromDB = Cities().get_one_element(request.form["city_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Cities().patch(request.form["city_name"], request.form["country_id"], request.form["zipcode"], request.form["city_id"])
            return elements
        except Exception as identifier:
            return abort(500, identifier)


@cities.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from cities by id """
    elementFromDB = Cities().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Cities().delete_element(id)
            result = jsonify(elements)
            result.statut_code = 200
            return result
        except Exception as identifier:
            return abort(500, identifier)
