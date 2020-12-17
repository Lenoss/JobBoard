from flask import Blueprint, jsonify, json, request, abort
from Models.countries import Countries
from flask_cors import CORS, cross_origin

countries = Blueprint("country", __name__)
CORS(countries)

@countries.route("/")
def getall():
    """ Get all element from Countries """
    elements = Countries().get_all_elements()
    data = jsonify(elements)
    data.statut_code = 200
    return data

@countries.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from cities by id """
    elements = Countries().get_one_element(id)
    data = jsonify(elements)
    if data is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        data.statut_code = 200
        return data

@countries.route("/", methods=['POST'])
def post():
    """ get post from front to insert element into the database """
    try:
        elements = Countries().post( request.form["name"])
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(500, identifier)



@countries.route("/", methods=['PUT'])
def put():
    """ get put from front to update element into the database """
    elementFromDB = Countries().get_one_element(request.form["country_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Countries().patch(request.form["name"])
            data = jsonify(elements)
            data.statut_code = 200
            return data
        except Exception as identifier:
            return abort(500, identifier)


@countries.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from cities by id """
    elementFromDB = Countries().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Countries().delete_element(id)
            data = jsonify(elements)
            data.statut_code = 200
            return data
        except Exception as identifier:
            return abort(500, identifier)
