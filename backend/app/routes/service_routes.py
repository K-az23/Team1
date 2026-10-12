from flask import Blueprint, jsonify

service_bp = Blueprint(
    "services",
    __name__
)



# GET /api/services
@service_bp.route("/api/services", methods=["GET"])
def get_services():
    return jsonify({
        "success": False,
        "message": "Get services endpoint not implemented yet."
    }), 501

# GET /api/services/<service_id>
@service_bp.route("/api/services/<string:service_id>", methods=["GET"])
def get_service(service_id):
    return jsonify({
        "success": False,
        "message": "Get service endpoint not implemented yet."
    }), 501

# POST /api/admin/services
@service_bp.route("/api/admin/services", methods=["POST"])
def create_service():
    return jsonify({
        "success": False,
        "message": "Create service endpoint not implemented yet."
    }), 501

# PATCH /api/admin/services/<service_id>
@service_bp.route("/api/admin/services/<string:service_id>", methods=["PATCH"])
def update_service(service_id):
    return jsonify({
        "success": False,
        "message": "Update service endpoint not implemented yet."
    }), 501

# DELETE /api/admin/services/<service_id>
@service_bp.route("/api/admin/services/<string:service_id>", methods=["DELETE"])
def delete_service(service_id):
    return jsonify({
        "success": False,
        "message": "Delete/deactivate service endpoint not implemented yet."
    }), 501