# DataFrame 
# Reading data from different Sources
# Reading data from JSON

import pandas as pd
# from io import StringIO
# Data = '{"Employee_name":"james","email":"sample@gmail.com","job_profile":[{"title1":"team lead","title2":"sales"}]}'
# df = pd.read_json(StringIO(Data))
# print(df)
# print(df.to_json())

url ="https://www.fdic.gov/bank-failures/failed-bank-list/santa-anna-national-bank"

htm = pd.read_html(url)
print(htm)