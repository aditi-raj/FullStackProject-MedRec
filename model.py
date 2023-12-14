import pandas as pd


data = pd.read_csv('drug.csv')
data = data.dropna()
data['condition'] = data['condition'].str.lower()

def recommend_drug(medical_condition):
   if data['condition'].str.contains(medical_condition).any():
      filtered_data=data[data['condition']==medical_condition]
      # print(filtered_data)
      sorted_data = filtered_data.sort_values(by=['usefulCount', 'rating'], ascending=False)
      # print(sorted_data)
   return sorted_data.iloc[0]['drugName']



