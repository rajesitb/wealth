import pandas as pd
import datetime


def create_data_frame():
    df = pd.DataFrame({'stock_number': 0, "stock_name": "", "stock_identity": "", "stock_id": "", "action_type": "",
                       "action_date": datetime.datetime.today(), "company_event": "",
                       "date_updated": datetime.datetime.today(), "comment": "",
                       "recommendation": ""}, index=[0])

    return df


