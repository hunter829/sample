import unittest
from csvParse import CSVDataWarehouse


class DataWareHouseTest(unittest.TestCase):
    def test_malformat(self):
        path = "resource/test_malformat.csv"
        try:
            dw = CSVDataWarehouse(path)
        except Exception, e:
            self.assertEquals(str(e), "format error in csv file")

    def test_getYoungestDozenFromAZipCode(self):
        path = "resource/test.csv"
        dw = CSVDataWarehouse(path)

        expect_list = ['["jay2", "los angeles", "West 27 St.", "10", "Los Angeles", "90007"]', 
        '["jay2", "los angeles", "West 27 St.", "12", "Los Angeles", "90007"]', 
        '["jay", "los angeles", "West 27 St.", "20", "Los Angeles", "90007"]', 
        '["jay3", "los angeles", "West 27 St.", "20", "Los Angeles", "90007"]', 
        '["jay8", "los angeles", "West 27 St.", "20", "Los Angeles", "90007"]', 
        '["jay3", "los angeles", "West 27 St.", "23", "Los Angeles", "90007"]', 
        '["jay5", "los angeles", "West 27 St.", "24", "Los Angeles", "90007"]', 
        '["jay5", "los angeles", "West 27 St.", "24", "Los Angeles", "90007"]', 
        '["jay4", "los angeles", "West 27 St.", "30", "Los Angeles", "90007"]', 
        '["jay4", "los angeles", "West 27 St.", "35", "Los Angeles", "90007"]', 
        '["jay6", "los angeles", "West 27 St.", "50", "Los Angeles", "90007"]', 
        '["jay6", "los angeles", "West 27 St.", "50", "Los Angeles", "90007"]']

        self.assertEquals(dw.getYoungestDozenFromAZipCode("90007"), expect_list)

if __name__ == '__main__':
    unittest.main()
