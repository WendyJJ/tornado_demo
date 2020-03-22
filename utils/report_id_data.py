"""
@project: test_interface
@author: aiyunxia
@file: report_id_data
@ide: PyCharm
@time: 2019/12/18 17:29
"""
import pandas as pd
from openpyxl.workbook import Workbook


data_list = []
aa = {}
data= {
    "aadhaar_no": "980059944167",
    "body": {
        "aadhaar_bind_pan_verified": {
            "aadhaar_no": "980059944167",
            "full_name": "Ranji Sharma",
            "pan_code": "FWDPS9695R",
            "verified_result": "Pan and aadhaar matched successfully"
        },
        "aadhaar_info_verification": {
            "aadhaar_no": "980059944167",
            "verified_age_band": "20-30",
            "verified_gender": "MALE",
            "verified_phone": "xxxxxxx408",
            "verified_province": "Assam",
            "verified_result": "Aadhaar Number 980059944167 Exists"
        },
        "multi_head_lending": {
            "cnt_cc_loan_info": {
                "cnt_cc_application_last_1d": 0,
                "cnt_cc_application_last_1m": 0,
                "cnt_cc_application_last_3d": 0,
                "cnt_cc_application_last_3m": 0,
                "cnt_cc_application_last_6m": 0,
                "cnt_cc_application_last_7d": 0
            },
            "cnt_cf_loan_info": {
                "cnt_cf_application_last_1d": 0,
                "cnt_cf_application_last_1m": 0,
                "cnt_cf_application_last_3d": 0,
                "cnt_cf_application_last_3m": 0,
                "cnt_cf_application_last_6m": 0,
                "cnt_cf_application_last_7d": 0
            },
            "cnt_el_loan_info": {
                "cnt_el_application_last_1d": 0,
                "cnt_el_application_last_1m": 0,
                "cnt_el_application_last_3d": 0,
                "cnt_el_application_last_3m": 0,
                "cnt_el_application_last_6m": 0,
                "cnt_el_application_last_7d": 0
            },
            "cnt_loan_application_last_1d": 0,
            "cnt_loan_application_last_1m": 9,
            "cnt_loan_application_last_3d": 0,
            "cnt_loan_application_last_3m": 15,
            "cnt_loan_application_last_6m": 15,
            "cnt_loan_application_last_7d": 0,
            "cnt_pl_loan_info": {
                "cnt_pl_application_last_1d": 0,
                "cnt_pl_application_last_1m": 0,
                "cnt_pl_application_last_3d": 0,
                "cnt_pl_application_last_3m": 0,
                "cnt_pl_application_last_6m": 0,
                "cnt_pl_application_last_7d": 0
            }
        },
        "pan_info_verification": {}
    },
    "clients_uid": "1604",
    "comment": "success",
    "content": "multi_head",
    "pan_code": "FWDPS9695R",
    "phone_number": "xxxxxxx408",
    "report_id": "201912170705179810003850274",
    "score": 50,
    "status": 200
}
body_data = data["body"]
data3 = data_list.append(data.pop("body"))
aa["aadhaar_bind_pan_verified"] = body_data["aadhaar_bind_pan_verified"]
data_list.append(aa)
pd.DataFrame(data_list).to_excel("data.xlsx")