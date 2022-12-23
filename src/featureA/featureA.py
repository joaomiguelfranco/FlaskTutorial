from flask import Blueprint

featureA_bp = Blueprint('featureA', __name__, url_prefix="/featureA/")


@featureA_bp.route('/')
def show():
    return "Feature A"
