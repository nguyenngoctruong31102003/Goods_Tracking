# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Item Tracking Addon',
    'version': '1.0',
    'sequence': 0,
    'category': 'Item Tracking',
    'summary': 'Tutorial addon for learning purposes',
    'description': """
        This is a tutorial addon that inherits res.partner model
        with completely new views and menu items.
    """,
    'depends': ['base', 'contacts','product'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_inherit.xml',
        'views/res_partner_inherit.xml',
        'views/menu_items.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
