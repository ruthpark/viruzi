import os



def read_file():
	str = ""
	with open("../mapping.txt") as genes:
		lines = [line.rstrip('\n') for line in genes]
		for line in lines:
			genes = line.split("\t")
			str += genes[0] + ","
	return str



cmd = "./api_dgidb.py --genes='%s' >> output.txt" %(read_file())



os.system(cmd)
