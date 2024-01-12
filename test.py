# from bardapi import Bard
# import os 
# os.environ['_BARD_API_KEY']="ZAg5sP8BYFYcPLP3_Xp1lNZ_FLh4db9m_K8d1QRKYubXwqMmuCzefso1al-aqcC7xz6sDw."
# import json
# import pandas as pd

# # df = pd.read_csv(r"C:\Users\HP\Desktop\HackRx\data_enrichment_1.csv")
# # df['highlights'] = ''

# # for index, row in df.iterrows():
# #     if index == 0 and index == 1:
# #         continue
# #     row_string = ','.join(row.astype(str))
# #     input_text = "Summarise the input text I will give you into the following points: 1.Job Description 2.Geography and where does he/she live 3.Interesting characteristics about his profile 4.For what profile would he be a good match"

# #     input_text += f"input text: {row_string}. {input_text}"

# #     bard_output = Bard().get_answer(input_text)['content']
# #     print(bard_output)

# import time

# import pandas as pd

# df = pd.read_csv(r"C:\Users\HP\Desktop\HackRx\data_enrichment_1.csv")
# df['highlights'] = ''

# for index, row in df.iterrows():
#     if index == 0 and index == 1:
#         continue
#     row_string = ','.join(row.astype(str))
#     input_text = "Summarize the input text I will give you into the following points: 1.Job Description 2.Geography and where does he/she live 3.Interesting characteristics about his profile 4.For what profile would he be a good match"

#     input_text += f"input text: {row_string}. {input_text}"

#     bard_output = Bard().get_answer(input_text)['content']
#     time.sleep(4)
#     df.loc[index, 'highlights'] = str(bard_output)

# df.to_csv(r"C:\Users\HP\Desktop\HackRx\data_output_1.csv")

    