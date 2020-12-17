from flask import Blueprint, jsonify, json, request, abort
from Models.contract_types import Contract_Types

contract_types = Blueprint("contract_types", __name__)


@contract_types.route("/")
def getall():
    """ Get all element from contract type """
    elements = Contract_Types().get_all_elements()
    data = jsonify(elements)
    data.statut_code = 200
    return data


@contract_types.route("/<int:id>", methods=['GET'])
def get(id):
    """ Get one element from contract types by id """
    elements = Contract_Types().get_one_element(id)
    if elements is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        elements = jsonify(elements)
        elements.statut_code = 200
        return elements


@contract_types.route("/", methods=['POST'])
def post():
    """ get post from front to insert element into the database """
    try:
        elements = Contract_Types().post(request.form["contract"])
        result = jsonify(elements)
        result.statut_code = 201
        return result
    except Exception as identifier:
        return abort(500, identifier)


@contract_types.route("/", methods=['PUT'])
def put():
    """ get put from front to update element into the database """
    elementFromDB = Contract_Types().get_one_element(request.form["type_id"])
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Contract_Types().put(request.form["contract"], request.form["type_id"])
            return elements
        except Exception as identifier:
            return abort(500, identifier)


@contract_types.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """ delete one element from contract_types by id """
    elementFromDB = Contract_Types().get_one_element(id)
    if elementFromDB is None:
        return abort(500, "L'élément n'existe pas.")
    else:
        try:
            elements = Contract_Types().delete_element(id)
            result = jsonify(elements)
            result.statut_code = 200
            return result
        except Exception as identifier:
            return abort(500, identifier)
