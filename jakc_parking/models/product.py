import logging
from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError, Warning

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = "product.template"

    iface_parking_membership = fields.Boolean("Parking Membership", default=False)
