import pandas as pd
import math

filePath = './angles_UCI_CS.csv'


def process(path):
    data = pd.read_csv(path, skipinitialspace=True)
    angles = data.loc[:, "angle_degrees"].tolist()
    cosine = []
    for s in angles:
        cosine.append(round(math.cos(math.radians(s)), 4))
    cos = pd.Series(cosine)
    data['cos'] = cos.values
    print(data)
    return data

def returnCSV(data):
	data.to_csv('output.csv')

ouputData = process(filePath)
returnCSV(outputData)
	

