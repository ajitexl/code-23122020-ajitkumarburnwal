import ijson
from pprint import pprint
import json
import tabulate

data = {}



def bmi_range(bmi):
    if bmi <=18.4:
        data['BMICategory'] = "Underweight"
        data["Healthrisk"] = "Malnutrition risk"
        return data
    if bmi >=18.5 and bmi<=24.9:
        data['BMICategory'] = "Normal weight"
        data["Healthrisk"] = "Low risk"
        return data
    if bmi >=25 and bmi<=29.9:
        data['BMICategory'] = "Overweight"
        data["Healthrisk"] = "Enhanced risk"
        return data
    if bmi >=30 and bmi<=34.9:
        data['BMICategory'] = "Moderately obese"
        data["Healthrisk"] = "Medium risk"
        return data
    if bmi >=35 and bmi<=39.9:
        data['BMICategory'] = "Severely obese"
        data["Healthrisk"] = "High risk"
        return data
    if bmi >=40:
        data['BMICategory'] = "Very severely obese"
        data["Healthrisk"] = "Very high risk"
        return data




def process_an_object(columns):
    data_list= []
    for data in columns:
    #The BMI (Body Mass Index) in (kg/m2) is equal to the weight in kilograms (kg)divided by your height in meters squared (m)2.
        data["BMI"] = round(data["WeightKg"]/(data["HeightCm"]/100)**2,2)
        bmi_analysis = bmi_range(data["BMI"])
        data.update(bmi_analysis)
        data_list.append(data)
    return data_list
        

def parse_json(json_filename):
    res = 0
    with open(json_filename, 'rb') as file:
        objects = ijson.items(file, 'item') 
        columns = list(objects) #Convert generator to list
        data_list  = process_an_object(columns)
        for i in data_list: 
            if i['BMICategory'] == "Overweight": 
                res = res + 1
        #pprint(data_list)

        with open('result.json', 'w') as f:
            json.dump(data_list , f)
        
        header = data_list[0].keys()
        rows =  [x.values() for x in data_list]
        print (tabulate.tabulate(rows, header))
        
        
        
        print(f"total number of Overweight paticent : {res}")
        

if __name__ == '__main__':
    parse_json('input.json')

