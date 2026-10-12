from flask import Flask

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.service_routes import service_bp
from routes.catalog_routes import catalog_bp
from routes.hairpiece_order_routes import (
    hairpiece_order_bp,
    admin_hairpiece_order_bp
)
from routes.appointment_routes import (
    appointment_bp,
    admin_appointment_bp
)
from routes.payment_routes import (
    payment_bp,
    stripe_webhook_bp
)
from routes.admin_routes import admin_user_bp
from routes.inventory_routes import inventory_bp
from routes.item_category_routes import item_category_bp
from routes.tracking_routes import purchasing_bp
from routes.report_routes import report_bp
from routes.contact_routes import contact_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(catalog_bp)

    app.register_blueprint(hairpiece_order_bp)
    app.register_blueprint(admin_hairpiece_order_bp)

    app.register_blueprint(appointment_bp)
    app.register_blueprint(admin_appointment_bp)

    app.register_blueprint(payment_bp)
    app.register_blueprint(stripe_webhook_bp)

    app.register_blueprint(admin_user_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(item_category_bp)
    app.register_blueprint(purchasing_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(contact_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)