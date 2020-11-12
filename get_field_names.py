import json
import csv 

form_name = 'standardrutter'
with open(form_name + '.json') as f:
    form = json.load(f)

field_names = []
for field in form['dataModel']:
    field_names.append([field['name']])

print(type(field_names))

with open(form_name + '_fields', '+a') as f: 
	
	# using csv.writer method from CSV package 
	write = csv.writer(f) 
	write.writerows(field_names) 
