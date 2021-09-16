import unittest
import assessment as ass

class UnitTestAssessmentMethods(unittest.TestCase):
    # Test valid and invalid file names
    def test_givenInvalidFile_getWeatherData_returnEmptyData(self):
        data = ass.get_weather_data('invalid.csv')
        self.assertEqual(data, [])

    def test_givenValidFile_getWeatherData_returnData(self):
        data = ass.get_weather_data('test.csv')
        self.assertEqual(data[0]['station_id'], '1')
        self.assertEqual(data[0]['date'], 2000.375)
        self.assertEqual(data[0]['temperature_c'], 10.000)
        self.assertEqual(data[13]['station_id'], '2')
        self.assertEqual(data[13]['date'], 2001.958)
        self.assertEqual(data[13]['temperature_c'], 21.000)

    def test_getLowestTempOccurrence_returnsStationIdAndDate(self):
        data = ass.get_weather_data('test.csv')
        station_id, date = ass.get_lowest_temp_occurrence(data)
        self.assertEqual(station_id, '1')
        self.assertEqual(date, 2000.542)
    
    def test_getStationWithHighestTempFluctuation_returnsStationId(self):
        data = ass.get_weather_data('test.csv')
        station_id = ass.get_station_with_highest_temp_fluctuation(data)
        self.assertEqual(station_id, '2')

    def test_getStationWithHighestTempFluctuationInRange_returnsStationId(self):
        data = ass.get_weather_data('test.csv')
        station_id = ass.get_station_with_highest_temp_fluctuation_in_range(data, 2000.542, 2001.292)
        self.assertEqual(station_id, '2')

    def test_calculateTotalFluctuation_returnsTotalFluctuation(self):
        data = [{'temperature_c': 5}, {'temperature_c': 0}, {'temperature_c': 8}]
        total = ass.calculate_total_fluctuation(data)
        self.assertEqual(total, 13)

if __name__ == '__main__':
    unittest.main()
