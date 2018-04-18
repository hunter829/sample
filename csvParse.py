import string
import json

class CSVDataWarehouse(object):
	def __init__(self, file_path):
		self.records = []
		#parse csv file
		with open(file_path, "r") as f:
			col_names = map(string.strip, f.readline().split(","))
			#interating over file
			for line in f:
				data = map(string.strip, line.split(","))
				if len(data) != len(col_names):
					raise Exception("format error in csv file")
				self.records.append(CSVRecord(data, col_names))

	def getYoungestDozenFromAZipCode(self, zipCode):
		result = []
		for record in self.records:
			if record.get("zipCode") == zipCode:
				result.append(record)
		result.sort(key=lambda r: r.get("age"))
		return [record.toJSON() for record in result[:12]]

class CSVRecord(object):
	def __init__(self, data, cols):
		self.__data = list(data)
		self.__mapping = {}
		for idx, col_name in enumerate(cols):
			while col_name in self.__mapping:
				col_name += "_duplicate"
			self.__mapping[col_name] = idx

	def get(self, para):
		if isinstance(para, basestring):
			return self.__data[self.__mapping[para]];
		elif isinstance(para, int):
			return self.__data[para]
		else:
			raise Exception("parameter type wrong")

	def size(self):
		return len(self.__data)

	def toJSON(self):
		return json.dumps(self.__data)

