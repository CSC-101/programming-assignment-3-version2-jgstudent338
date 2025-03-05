import data
import build_data
import unittest


         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')]
class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total1(self):
        result = hw3.population_total(reduced_data)
        expected = 655813
        self.assertEqual(result, expected)

    def test_population_total2(self):
        result = hw3.population_total(full_data)
        expected = 318857056
        self.assertEqual(result, expected)
dd
    # Part 2
    # test filter_by_state
    def test_filter_by_state1(self):
        result = hw3.filter_by_state(reduced_data, 'AL')
        desired = data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL')
        expected = [desired]
        self.assertEqual(result, expected)

    def test_filter_by_state2(self):
        result = hw3.filter_by_state(reduced_data, 'WY')
        expected = [data.CountyDemographics(
            {'Percent 65 and Older': 18.1,
             'Percent Under 18 Years': 21.6,
             'Percent Under 5 Years': 6.5},
            'Weston County',
            {"Bachelor's Degree or Higher": 17.2,
             'High School or Higher': 90.2},
            {'American Indian and Alaska Native Alone': 1.7,
             'Asian Alone': 0.4,
             'Black Alone': 0.7,
             'Hispanic or Latino': 4.2,
             'Native Hawaiian and Other Pacific Islander Alone': 0.0,
             'Two or More Races': 2.2,
             'White Alone': 95.0,
             'White Alone, not Hispanic or Latino': 91.5},
            {'Per Capita Income': 28764,
             'Persons Below Poverty Level': 11.2,
             'Median Household Income': 55461},
            {'2010 Population': 7208,
             '2014 Population': 7201,
             'Population Percent Change': -0.1,
             'Population per Square Mile': 3.0},
            'WY')]
        self.assertEqual(result, expected)

    def test_filter_by_state3(self):
        result = hw3.filter_by_state(reduced_data, 'xyz')
        expected = []
        self.assertEqual(result, expected)

    # Part 3
    # test population_by_education
    def test_population_by_education1(self):
        result = hw3.population_by_education(reduced_data, 'High School or Higher')
        expected = 85.6/100*55395+82.2/100*61697+89.6/100*279083+84.3/100*207590+89.2/100*2622 + 81.8/100*42225 + 90.2/100*7201
        self.assertEqual(result, expected)

    def test_population_by_education2(self):
        result = hw3.population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected =  20.9/100 * 55395 + 14.3/100 * 61697 + 31.5/100 * 279083+ 37.9/100 * 207590 + 17.9/100*2622 + 15.2/100 * 42225 + 17.2/100 * 7201
        self.assertEqual(result, expected)

    # test population_by_ethnicity
    def test_population_by_ethnicity1(self):
        result = hw3.population_by_ethnicity(reduced_data, 'White Alone')
        expected = 77.9/100 * 55395 + 91.5/100 * 61697 + 89/100 * 279083+ 75.9/100 * 207590 + 96.1/100*2622 + 92.9/100 * 42225 + 95/100 * 7201
        self.assertEqual(result, expected)

    def test_population_by_ethnicity2(self):
        result = hw3.population_by_ethnicity(reduced_data, 'Hispanic or Latino')
        expected =  2.7/100 * 55395 + 6.7/100 * 61697 + 22/100 * 279083+ 31.5/100 * 207590 + 5.8/100*2622 + 8.3/100 * 42225 + 4.2/100 * 7201
        self.assertEqual(result, expected)

    # test population_below_poverty_level

    def test_population_below_poverty_level(self):
        result = hw3.population_below_poverty_level(reduced_data)
        expected = 12.1/100 * 55395 + 20.2/100 * 61697 + 14.3/100 * 279083+ 19.1/100 * 207590 + 15.7/100*2622 + 18.4/100 * 42225 + 11.2/100 * 7201
        self.assertEqual(result, expected)

    def test_population_below_poverty_level2(self):
        result = hw3.population_below_poverty_level([data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR')])
        expected = (55395 * 12.1/100) + (61697 * 20.2/100)
        self.assertEqual(result, expected)

    # Part 4

    # test percent_by_education
    def test_percent_by_education1(self):
        result = hw3.percent_by_education([data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR')], 'High School or Higher')
        expected = ((61697 * (82.2/100) + 55395 * (85.6/100))/ (61697 + 55395))*100
        self.assertEqual(result, expected)

    def test_percent_by_education2(self):
        result = hw3.percent_by_education([data.CountyDemographics(
                {'Percent 65 and Older': 13.8,
                 'Percent Under 18 Years': 25.2,
                 'Percent Under 5 Years': 6.0},
                'Autauga County',
                {"Bachelor's Degree or Higher": 20.9,
                 'High School or Higher': 85.6},
                {'American Indian and Alaska Native Alone': 0.5,
                 'Asian Alone': 1.1,
                 'Black Alone': 18.7,
                 'Hispanic or Latino': 2.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 1.8,
                 'White Alone': 77.9,
                 'White Alone, not Hispanic or Latino': 75.6},
                {'Per Capita Income': 24571,
                 'Persons Below Poverty Level': 12.1,
                 'Median Household Income': 53682},
                {'2010 Population': 54571,
                 '2014 Population': 55395,
                 'Population Percent Change': 1.5,
                 'Population per Square Mile': 91.8},
                'AL'),
                data.CountyDemographics(
                    {'Percent 65 and Older': 15.3,
                     'Percent Under 18 Years': 25.1,
                     'Percent Under 5 Years': 6.0},
                    'Crawford County',
                    {"Bachelor's Degree or Higher": 14.3,
                     'High School or Higher': 82.2},
                    {'American Indian and Alaska Native Alone': 2.5,
                     'Asian Alone': 1.6,
                     'Black Alone': 1.6,
                     'Hispanic or Latino': 6.7,
                     'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                     'Two or More Races': 2.8,
                     'White Alone': 91.5,
                     'White Alone, not Hispanic or Latino': 85.6},
                    {'Per Capita Income': 19477,
                     'Persons Below Poverty Level': 20.2,
                     'Median Household Income': 39479},
                    {'2010 Population': 61948,
                     '2014 Population': 61697,
                     'Population Percent Change': -0.4,
                     'Population per Square Mile': 104.4},
                    'AR')], "Bachelor's Degree or Higher")
        expected = ((61697 * (14.3 / 100) + 55395 * (20.9 / 100)) / (61697 + 55395)) * 100
        self.assertEqual(result, expected)


    # test percent_by_ethnicity
    def test_percent_by_ethnicity1(self):
        result = hw3.percent_by_ethnicity([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], 'White Alone')
        expected = ((61697 * (91.5 / 100) + 55395 * (77.9 / 100)) / (61697 + 55395)) * 100
        self.assertEqual(result, expected)

    def test_percent_by_ethnicity2(self):
        result = hw3.percent_by_ethnicity([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], "Hispanic or Latino")
        expected = ((61697 * (6.7/ 100) + 55395 * (2.7 / 100)) / (61697 + 55395)) * 100
        self.assertEqual(result, expected)
    # test percent_below_poverty_level

    def test_percent_below_poverty_level1(self):
        result = hw3.percent_below_poverty_level([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')])
        expected = ((61697 * (20.2/ 100) + 55395 * (12.1 / 100)) / (61697 + 55395)) * 100
        self.assertEqual(result, expected)

    def test_percent_below_poverty_level2(self):
        result = hw3.percent_below_poverty_level([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL')])

        expected = (55395 * (12.1 / 100)) / ((55395)) * 100
        self.assertEqual(result, expected)

    # Part 5
    # test education_greater_than
    def test_education_greater_than1(self):
        result = hw3.education_greater_than([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], 'High School or Higher', 83)
        expected =  [data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL')]
        self.assertEqual(result, expected)

    def test_education_greater_than2(self):
        result = hw3.education_greater_than([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], 'High School or Higher', 80)
        expected =  [data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')]
        self.assertEqual(result, expected)
    # test education_less_than
    def test_education_less_than2(self):
        result = hw3.education_less_than([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], 'High School or Higher', 83)
        expected =  [data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')]
        self.assertEqual(result, expected)

    def test_education_less_than1(self):
        result = hw3.education_less_than([data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')], 'High School or Higher', 88)
        expected =  [data.CountyDemographics(
            {'Percent 65 and Older': 13.8,
             'Percent Under 18 Years': 25.2,
             'Percent Under 5 Years': 6.0},
            'Autauga County',
            {"Bachelor's Degree or Higher": 20.9,
             'High School or Higher': 85.6},
            {'American Indian and Alaska Native Alone': 0.5,
             'Asian Alone': 1.1,
             'Black Alone': 18.7,
             'Hispanic or Latino': 2.7,
             'Native Hawaiian and Other Pacific Islander Alone': 0.1,
             'Two or More Races': 1.8,
             'White Alone': 77.9,
             'White Alone, not Hispanic or Latino': 75.6},
            {'Per Capita Income': 24571,
             'Persons Below Poverty Level': 12.1,
             'Median Household Income': 53682},
            {'2010 Population': 54571,
             '2014 Population': 55395,
             'Population Percent Change': 1.5,
             'Population per Square Mile': 91.8},
            'AL'),
            data.CountyDemographics(
                {'Percent 65 and Older': 15.3,
                 'Percent Under 18 Years': 25.1,
                 'Percent Under 5 Years': 6.0},
                'Crawford County',
                {"Bachelor's Degree or Higher": 14.3,
                 'High School or Higher': 82.2},
                {'American Indian and Alaska Native Alone': 2.5,
                 'Asian Alone': 1.6,
                 'Black Alone': 1.6,
                 'Hispanic or Latino': 6.7,
                 'Native Hawaiian and Other Pacific Islander Alone': 0.1,
                 'Two or More Races': 2.8,
                 'White Alone': 91.5,
                 'White Alone, not Hispanic or Latino': 85.6},
                {'Per Capita Income': 19477,
                 'Persons Below Poverty Level': 20.2,
                 'Median Household Income': 39479},
                {'2010 Population': 61948,
                 '2014 Population': 61697,
                 'Population Percent Change': -0.4,
                 'Population per Square Mile': 104.4},
                'AR')]
        self.assertEqual(result, expected)

    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        result = hw3.ethnicity_greater_than(reduced_data, 'Black Alone', 18)
        expected = [data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL')]
        self.assertEqual(result, expected)

    def test_ethnicity_greater_than2(self):
        result = hw3.ethnicity_greater_than(reduced_data, 'Black Alone', 0)
        expected = reduced_data
        self.assertEqual(result, expected)

    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Black Alone', 80)
        expected = reduced_data
        self.assertEqual(result, expected)

    def test_ethnicity_less_than2(self):
        result = hw3.ethnicity_less_than(reduced_data, 'Black Alone', 0)
        expected = []
        self.assertEqual(result, expected)

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        result = hw3.below_poverty_level_greater_than(reduced_data,  80)
        expected = []
        self.assertEqual(result, expected)

    def test_below_poverty_level_greater_than2(self):
        result = hw3.below_poverty_level_greater_than(reduced_data,  0)
        expected = reduced_data
        self.assertEqual(result, expected)

    # test below_poverty_level_less_than

    def test_below_poverty_level_less_than(self):
        result = hw3.below_poverty_level_less_than(reduced_data,  80)
        expected = reduced_data
        self.assertEqual(result, expected)

    def test_below_poverty_level_less_than2(self):
        result = hw3.below_poverty_level_less_than(reduced_data,  0)
        expected = []
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
sd