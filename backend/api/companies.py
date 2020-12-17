from flask import Blueprint, jsonify, json, request, abort
from flask_cors import CORS, cross_origin
from Models.companies import Companies

companies = Blueprint("companies", __name__)
CORS(companies)

@companies.route("/")
def getall():
    """ Get all element from company """
    elements = Companies().get_all_elements()
    data = jsonify(elements)
    data.statut_code = 200
    return data


@companies.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from company by id """
    elements = Companies().get_one_element(id)
    data = jsonify(elements)
    if data is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        data.statut_code = 200
        return data


@companies.route("/", methods=['POST'])
def post():
    """ get post from front to insert element into the database """
    try:
        elements = Companies().post(request.form["title"], request.form["email"], request.form["phone"], request.form["user_id"], request.form["logo"] )
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(500, identifier)


@companies.route("/", methods=['PUT'])
def put():
    """ get put from front to update element into the database """
    elementFromDB = Companies().get_one_element(request.form["company_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Companies().patch(request.form["title"], request.form["email"], request.form["phone"], request.form["user_id"], request.form["logo"], request.form["company_id"] )
            return elements
        except Exception as identifier:
            return abort(500, identifier)


@companies.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from company by id """
    elementFromDB = Companies().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Companies().delete_element(id)
            result = jsonify(elements)
            result.statut_code = 200
            return result
        except Exception as identifier:
            return abort(500, identifier)

