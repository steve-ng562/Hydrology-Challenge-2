import pandas as pd 

outputPath = './src/output.csv'
testPath = './angles_UCI_CS_out.csv'

def readCSVFile(outPath):
	output = pd.read_csv(outPath, skipinitialspace =True)
	return output
	

def test():
	outputData = readCSVFile(outputPath)
	testData = readCSVFile(testPath)
	assert outputData.loc[:, "angle_degrees"].tolist() == testData.loc[:, "angle_degrees"].tolist()
	assert outputData.loc[:, "station_id"].tolist() == testData.loc[:, "station_id"].tolist()
	assert outPutData.loc[:, "angle_cosine"].tolist() == testData.loc[:, "angle_cosine"].tolist()
