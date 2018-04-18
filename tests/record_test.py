import unittest
from csvParse import CSVRecord

class RecordTest(unittest.TestCase):
    def test_create_Record(self):
        col_names = ["name", "city", "address", "age", "city", "zipCode"]
        line = ["jay", "los angeles", "West 30 St.", "20", "los angeles", "90007"]

        record = CSVRecord(line, col_names)

        expected_data = line
        expected_mapping = {"name":0, "city":1, "address":2, "age":3, "city_duplicate":4, "zipCode":5}

        self.assertEquals(record._CSVRecord__data, expected_data)
        self.assertEquals(record._CSVRecord__mapping, expected_mapping)

    def test_get_record(self):
        col_names = ["name", "city", "address", "age", "city", "zipCode"]
        line = ["jay", "los angeles", "West 30 St.", "20", "los angeles", "90007"]

        record = CSVRecord(line, col_names)

        self.assertEquals(record.get(1), "los angeles")
        self.assertEquals(record.get("age"), "20")
    
    def test_json(self):
        col_names = ["name", "city", "address", "age", "city", "zipCode"]
        line = ["jay", "los angeles", "West 30 St.", "20", "los angeles", "90007"]

        record = CSVRecord(line, col_names)

        expected_json = '["jay", "los angeles", "West 30 St.", "20", "los angeles", "90007"]'
        self.assertEquals(record.toJSON(), expected_json)

if __name__ == '__main__':
    unittest.main()
