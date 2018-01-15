# Part of Open eObs. See LICENSE file for full copyright and licensing details.
from . import test_api_get_activities_settings
from . import test_eobs_settings
from . import test_helpers
from . import test_sql_statements
from . import test_workload
from .nh_clinical_frequencies_ews import *
from .nh_clinical_observation_report_wizard import *
from .nh_clinical_patient_monitoring_exception import *
from .nh_clinical_patient_observation_ews import *
from .nh_clinical_patient_transfer import *
from .nh_clinical_wardboard import *
from .nh_eobs_api import *
from .nh_eobs_ward_dashboard import *
from .report_nh_clinical_observation_report import *
from .nh_clinical_patient_placement import *

# Disabled tests
# from . import test_api_demo
# from openeobs.nh_eobs.tests.wardboard import test_wardboard
# from . import test_palliative_status_tour
# from . import test_staff_allocation_tours
# from . import test_stand_in_api
