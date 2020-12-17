from flask import Blueprint, jsonify, json, request, abort
from Models.advertisements import Advertisements
from flask_cors import CORS, cross_origin

advertisements = Blueprint("advertisement", __name__)
CORS(advertisements)

@advertisements.route("/")
def getall():
    """ Get all element from advertisement """
    elements = Advertisements().get_all_elements()
    data = jsonify(elements)
    data.statut_code = 200
    return data


@advertisements.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from advertisements by id """
    elements = Advertisements().get_one_element(id)
    data = jsonify(elements)
    if data is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        data.statut_code = 200
        return data


@advertisements.route("/", methods=['POST'])
def post():
    """ get methode post from front to insert element into the database """

    title = request.form["title"]
    description = request.form["description"]
    is_valid = request.form["is_valid"]
    company_id = request.form["company_id"]
    city_id = request.form["city_id"]
    start_date = request.form["start_date"]
    add_date = request.form["add_date"]
    sector = request.form["sector"]
    contract_type_id = request.form["contract_type_id"]
    experience = request.form["experience"]
    formation = request.form["formation"]
    try:
        elements = Advertisements().post( title, description, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation)
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(500, identifier)



@advertisements.route("/", methods=['PUT'])
def put():
    """ get methode put from front to update element into the database """
    title = request.form["title"]
    description = request.form["description"]
    is_valid = request.form["is_valid"]
    company_id = request.form["company_id"]
    city_id = request.form["city_id"]
    start_date = request.form["start_date"]
    add_date = request.form["add_date"]
    sector = request.form["sector"]
    contract_type_id = request.form["contract_type_id"]
    experience = request.form["experience"]
    formation = request.form["formation"]
    advertisement_id = request.form["advertisement_id"]
    elementFromDB = Advertisements().get_one_element(request.form["advertisement_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Advertisements().patch( title, description, is_valid, company_id, city_id, start_date, add_date, sector, contract_type_id, experience, formation, advertisement_id )
            return elements
        except Exception as identifier:
            return abort(500, identifier)


@advertisements.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from advertisements by id """
    elementFromDB = Advertisements().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Advertisements().delete_element(id)
            result = jsonify(elements)
            result.statut_code = 200
            return result
        except Exception as identifier:
            return abort(500, identifier)

