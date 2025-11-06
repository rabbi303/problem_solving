A .txt file will be given. You need to find out how many INFO, ERROR, WARNING there are in total.

def file_analyze(file_path):

#keep log count in Dictionary 
	count = {
			"ERROR" : 0, 
 			"INFO": 0,
			"WARNING": 0 
	} 


	#file read

	with open(file_path, "r") as file:
		for line in file:
			# test every line
			if "INFO" in line:
				count["INFO"] += 1
			elif "ERROR" in line:
				count["ERROR"] += 1
			elif "WARNING" in line:
				count["WARNING"] += 1

		#print all the result
		for key , value in count.items():
			print(f"{key} : {value}")
			
		'''		
		#print only selected result
		selected = "ERROR"
		if selected in count:
			print(f'{selected} : {count[selected]}')
		else:
			print("Invalid selection")
		'''


if __name__ == "__main__":
    file_name = "/media/rabbi/83afe739-1cf3-417b-8249-ba6841296dca/rabbi/python_study/problem_solving/file.txt"
    file_analyze(file_name)
	

