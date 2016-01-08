# -*- encoding: utf-8 -*-
{
    'name': 'NH eObs',
    'version': '0.1',
    'category': 'Clinical',
    'license': 'AGPL-3',
    'summary': '',
    'description': """     """,
    'author': 'Neova Health',
    'website': 'http://www.neovahealth.co.uk/',
    'depends': ['nh_clinical', 'nh_ews', 'nh_gcs', 'nh_pbp', 'nh_stools', 'nh_graphs',
                'nh_shift_management'],
    'data': ['eobs_data.xml',
             'observation_report.xml',
             'wizard/cancel_notifications_view.xml',
             'wizard/print_observation_report_view.xml',
             'views/wardboard_view.xml',
             'views/workload_view.xml',
             'views/placement_view.xml',
             'views/overdue_view.xml',
             'views/views.xml',
             'views/kamishibai_view.xml',
             'views/spell_management_views.xml',
             'views/ward_dashboard_view.xml',
             'views/locations_view.xml',
             'views/menuitem.xml',
             'views/observation_report.xml',
             'security/ir.model.access.csv'],
    'qweb': ['static/src/xml/nh_eobs.xml'],
    'application': True,
    'installable': True,
    'active': False,
}
