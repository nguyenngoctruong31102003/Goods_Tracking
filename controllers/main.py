import odoo
import logging
import json
from urllib.parse import urlparse, parse_qs

import requests
from werkzeug import urls
from werkzeug.exceptions import Forbidden
from werkzeug.utils import redirect

from odoo import _, http
from odoo.http import request
from odoo.exceptions import ValidationError
from odoo.tools import html_escape
