# -*- coding: utf-8 -*-


import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

def welcome():
    return "Welcome All"


def predict_note_authentication(data_in):

    prediction = model.predict(data_in)
    print(prediction)
    return prediction


def main():
    st.title("Data Analyst Salary Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Salary Prediction ML App </h2>
    </div>
    """


    file_name = "model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']

    features = {'rating': 0,
                    'company_age': 0,
                    'size_1 to 50 Employees': 0,
                    'size_10000+ Employees': 0,
                    'size_1001 to 5000 Employees': 0,
                    'size_201 to 500 Employees': 0,
                    'size_5001 to 10000 Employees': 0,
                    'size_501 to 1000 Employees': 0,
                    'size_51 to 200 Employees': 0,
                    'type_of_ownership_College / University': 0,
                    'type_of_ownership_Company - Private': 0,
                    'type_of_ownership_Company - Public': 0,
                    'type_of_ownership_Franchise': 0,
                    'type_of_ownership_Government': 0,
                    'type_of_ownership_Hospital': 0,
                    'type_of_ownership_Nonprofit Organization': 0,
                    'type_of_ownership_Private Practice / Firm': 0,
                    'type_of_ownership_School / School District': 0,
                    'type_of_ownership_Subsidiary or Business Segment': 0,
                    'industry_Accounting': 0,
                    'industry_Advertising & Marketing': 0,
                    'industry_Aerospace & Defense': 0,
                    'industry_Architectural & Engineering Services': 0,
                    'industry_Automotive Parts & Accessories Stores': 0,
                    'industry_Banks & Credit Unions': 0,
                    'industry_Biotech & Pharmaceuticals': 0,
                    'industry_Brokerage Services': 0,
                    'industry_Cable, Internet & Telephone Providers': 0,
                    'industry_Colleges & Universities': 0,
                    'industry_Commercial Equipment Rental': 0,
                    'industry_Computer Hardware & Software': 0,
                    'industry_Consulting': 0,
                    'industry_Consumer Product Rental': 0,
                    'industry_Consumer Products Manufacturing': 0,
                    'industry_Department, Clothing, & Shoe Stores': 0,
                    'industry_Drug & Health Stores': 0,
                    'industry_Electrical & Electronic Manufacturing': 0,
                    'industry_Energy': 0,
                    'industry_Enterprise Software & Network Solutions': 0,
                    'industry_Express Delivery Services': 0,
                    'industry_Farm Support Services': 0,
                    'industry_Federal Agencies': 0,
                    'industry_Financial Analytics & Research': 0,
                    'industry_Financial Transaction Processing': 0,
                    'industry_Food & Beverage Manufacturing': 0,
                    'industry_Gambling': 0,
                    'industry_Gas Stations': 0,
                    'industry_Gift, Novelty & Souvenir Stores': 0,
                    'industry_Health Care Products Manufacturing': 0,
                    'industry_Health Care Services & Hospitals': 0,
                    'industry_Home Centers & Hardware Stores': 0,
                    'industry_Home Furniture & Housewares Stores': 0,
                    'industry_IT Services': 0,
                    'industry_Industrial Manufacturing': 0,
                    'industry_Insurance Agencies & Brokerages': 0,
                    'industry_Insurance Carriers': 0,
                    'industry_Internet': 0,
                    'industry_Investment Banking & Asset Management': 0,
                    'industry_K-12 Education': 0,
                    'industry_Legal': 0,
                    'industry_Lending': 0,
                    'industry_Logistics & Supply Chain': 0,
                    'industry_Membership Organizations': 0,
                    'industry_Miscellaneous Manufacturing': 0,
                    'industry_Municipal Governments': 0,
                    'industry_Preschool & Child Care': 0,
                    'industry_Real Estate': 0,
                    'industry_Religious Organizations': 0,
                    'industry_Research & Development': 0,
                    'industry_Security Services': 0,
                    'industry_Social Assistance': 0,
                    'industry_Staffing & Outsourcing': 0,
                    'industry_State & Regional Agencies': 0,
                    'industry_Telecommunications Manufacturing': 0,
                    'industry_Telecommunications Services': 0,
                    'industry_Transportation Equipment Manufacturing': 0,
                    'industry_Transportation Management': 0,
                    'industry_Wholesale': 0,
                    'sector_Accounting & Legal': 0,
                    'sector_Aerospace & Defense': 0,
                    'sector_Agriculture & Forestry': 0,
                    'sector_Arts, Entertainment & Recreation': 0,
                    'sector_Biotech & Pharmaceuticals': 0,
                    'sector_Business Services': 0,
                    'sector_Consumer Services': 0,
                    'sector_Education': 0,
                    'sector_Finance': 0,
                    'sector_Government': 0,
                    'sector_Health Care': 0,
                    'sector_Information Technology': 0,
                    'sector_Insurance': 0,
                    'sector_Manufacturing': 0,
                    'sector_Non-Profit': 0,
                    'sector_Oil, Gas, Energy & Utilities': 0,
                    'sector_Real Estate': 0,
                    'sector_Retail': 0,
                    'sector_Telecommunications': 0,
                    'sector_Transportation & Logistics': 0,
                    'revenue_1-2b': 0,
                    'revenue_1-5m': 0,
                    'revenue_10-25m': 0,
                    'revenue_100-500m': 0,
                    'revenue_10b': 0,
                    'revenue_2-5b': 0,
                    'revenue_25-50m': 0,
                    'revenue_5-10m': 0,
                    'revenue_50-100m': 0,
                    'revenue_500m-1b': 0,
                    'revenue_<1m': 0,
                    'city_Albany': 0,
                    'city_Altamonte Springs': 0,
                    'city_Anchorage': 0,
                    'city_Ankeny': 0,
                    'city_Ann Arbor': 0,
                    'city_Arlington': 0,
                    'city_Ashburn': 0,
                    'city_Atlanta': 0,
                    'city_Austin': 0,
                    'city_Baltimore': 0,
                    'city_Beaverton': 0,
                    'city_Bellevue': 0,
                    'city_Bethesda': 0,
                    'city_Birmingham': 0,
                    'city_Bloomington': 0,
                    'city_Bonita Springs': 0,
                    'city_Boston': 0,
                    'city_Boulder': 0,
                    'city_Bowie': 0,
                    'city_Brea': 0,
                    'city_Brentwood': 0,
                    'city_Bridgeton': 0,
                    'city_Brooklyn': 0,
                    'city_Brooklyn Heights': 0,
                    'city_Burlingame': 0,
                    'city_Cambridge': 0,
                    'city_Carlsbad': 0,
                    'city_Carson': 0,
                    'city_Center Valley': 0,
                    'city_Charlotte': 0,
                    'city_Chaska': 0,
                    'city_Chicago': 0,
                    'city_Chico': 0,
                    'city_Cincinnati': 0,
                    'city_Clarksburg': 0,
                    'city_Colmar': 0,
                    'city_Colorado Springs': 0,
                    'city_Columbia': 0,
                    'city_Columbus': 0,
                    'city_Culver City': 0,
                    'city_Dallas': 0,
                    'city_Danville': 0,
                    'city_Deerfield': 0,
                    'city_Denver': 0,
                    'city_Detroit': 0,
                    'city_Dublin': 0,
                    'city_Durham': 0,
                    'city_Eden Prairie': 0,
                    'city_Englewood': 0,
                    'city_Eugene': 0,
                    'city_Eureka': 0,
                    'city_Fairport': 0,
                    'city_Falls Church': 0,
                    'city_Flint': 0,
                    'city_Florham Park': 0,
                    'city_Fort Wayne': 0,
                    'city_Fremont': 0,
                    'city_Ft Carson': 0,
                    'city_Garden City': 0,
                    'city_Gilbert': 0,
                    'city_Glendale': 0,
                    'city_Golden': 0,
                    'city_Grand Prairie': 0,
                    'city_Greensboro': 0,
                    'city_Harrisburg': 0,
                    'city_Hartford': 0,
                    'city_Hayward': 0,
                    'city_Herndon': 0,
                    'city_Highland': 0,
                    'city_Houston': 0,
                    'city_Indianapolis': 0,
                    'city_Industry': 0,
                    'city_Irving': 0,
                    'city_Jacksonville': 0,
                    'city_Jersey City': 0,
                    'city_Kansas City': 0,
                    'city_King of Prussia': 0,
                    'city_Ladera Ranch': 0,
                    'city_Lafayette': 0,
                    'city_Lake Mary': 0,
                    'city_Lancaster': 0,
                    'city_Laramie': 0,
                    'city_Las Vegas': 0,
                    'city_Leander': 0,
                    'city_Lenexa': 0,
                    'city_Long Beach': 0,
                    'city_Los Angeles': 0,
                    'city_Loveland': 0,
                    'city_Lowell': 0,
                    'city_Mahwah': 0,
                    'city_Malden': 0,
                    'city_McLean': 0,
                    'city_Medford': 0,
                    'city_Memphis': 0,
                    'city_Miami': 0,
                    'city_Miami Lakes': 0,
                    'city_Minneapolis': 0,
                    'city_Minnetonka': 0,
                    'city_Mount Laurel': 0,
                    'city_Mountain View': 0,
                    'city_Mundelein': 0,
                    'city_Naples': 0,
                    'city_Nashville': 0,
                    'city_New Britain': 0,
                    'city_New Haven': 0,
                    'city_New York': 0,
                    'city_Newark': 0,
                    'city_Newport News': 0,
                    'city_Norfolk': 0,
                    'city_Normal': 0,
                    'city_North Canton': 0,
                    'city_Northbrook': 0,
                    'city_Oakland': 0,
                    'city_Ogden': 0,
                    'city_Oklahoma': 0,
                    'city_Oklahoma City': 0,
                    'city_Orlando': 0,
                    'city_Palm Beach Gardens': 0,
                    'city_Palo Alto': 0,
                    'city_Parsippany': 0,
                    'city_Pasadena': 0,
                    'city_Philadelphia': 0,
                    'city_Phoenix': 0,
                    'city_Pittsburgh': 0,
                    'city_Plano': 0,
                    'city_Pleasanton': 0,
                    'city_Plymouth': 0,
                    'city_Portland': 0,
                    'city_Portsmouth': 0,
                    'city_Provo': 0,
                    'city_Quantico': 0,
                    'city_Raleigh': 0,
                    'city_Reading': 0,
                    'city_Reno': 0,
                    'city_Richardson': 0,
                    'city_Richmond': 0,
                    'city_Riverwoods': 0,
                    'city_Roanoke': 0,
                    'city_Rolling Meadows': 0,
                    'city_Rosemont': 0,
                    'city_Roswell': 0,
                    'city_Roy': 0,
                    'city_Sacramento': 0,
                    'city_Saint Louis': 0,
                    'city_Saint Petersburg': 0,
                    'city_Salt Lake City': 0,
                    'city_San Antonio': 0,
                    'city_San Diego': 0,
                    'city_San Francisco': 0,
                    'city_San Jose': 0,
                    'city_San Marcos': 0,
                    'city_Santa Barbara': 0,
                    'city_Santa Clara': 0,
                    'city_Santa Cruz': 0,
                    'city_Scottsdale': 0,
                    'city_Seattle': 0,
                    'city_Sellersville': 0,
                    'city_Sheldonville': 0,
                    'city_Solon': 0,
                    'city_Somerset': 0,
                    'city_Springfield': 0,
                    'city_St Louis Park': 0,
                    'city_Stamford': 0,
                    'city_Stanford': 0,
                    'city_Stevens Point': 0,
                    'city_Sycamore': 0,
                    'city_Tampa': 0,
                    'city_Tempe': 0,
                    'city_Tigard': 0,
                    'city_Troy': 0,
                    'city_Urbandale': 0,
                    'city_Vienna': 0,
                    'city_Virginia': 0,
                    'city_Waltham': 0,
                    'city_Warrenton': 0,
                    'city_Washington': 0,
                    'city_Waterbury': 0,
                    'city_Wayne': 0,
                    'city_Wellesley': 0,
                    'city_West Palm Beach': 0,
                    'city_Westlake Village': 0,
                    'city_Westminster': 0,
                    'city_Wilmington': 0,
                    'city_Wilton': 0,
                    'city_Winchester': 0,
                    'city_Woodbury': 0,
                    'city_Worthington': 0,
                    'state_AK': 0,
                    'state_AL': 0,
                    'state_AZ': 0,
                    'state_CA': 0,
                    'state_CO': 0,
                    'state_CT': 0,
                    'state_DC': 0,
                    'state_DE': 0,
                    'state_FL': 0,
                    'state_GA': 0,
                    'state_IA': 0,
                    'state_IL': 0,
                    'state_IN': 0,
                    'state_KS': 0,
                    'state_KY': 0,
                    'state_MA': 0,
                    'state_MD': 0,
                    'state_ME': 0,
                    'state_MI': 0,
                    'state_MN': 0,
                    'state_MO': 0,
                    'state_NC': 0,
                    'state_NH': 0,
                    'state_NJ': 0,
                    'state_NV': 0,
                    'state_NY': 0,
                    'state_OH': 0,
                    'state_OK': 0,
                    'state_OR': 0,
                    'state_PA': 0,
                    'state_TN': 0,
                    'state_TX': 0,
                    'state_UT': 0,
                    'state_VA': 0,
                    'state_VT': 0,
                    'state_WA': 0,
                    'state_WI': 0,
                    'state_WV': 0,
                    'state_WY': 0}

                
               
              

    st.markdown(html_temp, unsafe_allow_html=True)

    rating = st.text_input("Rating", "Type Here")
    features['rating'] = rating

    company_age = st.text_input("company_age", "Type Here")
    features['company_age'] = company_age

    # company size
    option = st.selectbox(
        'Choose company size: ',
        ('size_1 to 50 Employees',
                'size_10000+ Employees',
                'size_1001 to 5000 Employees',
                'size_201 to 500 Employees',
                'size_5001 to 10000 Employees',
                'size_501 to 1000 Employees',
                'size_51 to 200 Employees'))

    st.write('You selected:', option)
    features[option] = 1 

    # type of ownership
    option = st.selectbox(
        'Choose type of ownership: ',
        ('type_of_ownership_College / University',
                'type_of_ownership_Company - Private',
                'type_of_ownership_Company - Public',
                'type_of_ownership_Franchise',
                'type_of_ownership_Government',
                'type_of_ownership_Hospital',
                'type_of_ownership_Nonprofit Organization',
                'type_of_ownership_Private Practice / Firm',
                'type_of_ownership_School / School District',
                'type_of_ownership_Subsidiary or Business Segment'))

    st.write('You selected:', option)
    features[option] = 1 


    # type of industry
    option = st.selectbox(
        'Choose industry: ',
        ('industry_Accounting',
                'industry_Advertising & Marketing',
                'industry_Aerospace & Defense',
                'industry_Architectural & Engineering Services',
                'industry_Automotive Parts & Accessories Stores',
                'industry_Banks & Credit Unions',
                'industry_Biotech & Pharmaceuticals',
                'industry_Brokerage Services',
                'industry_Cable, Internet & Telephone Providers',
                'industry_Colleges & Universities',
                'industry_Commercial Equipment Rental',
                'industry_Computer Hardware & Software',
                'industry_Consulting',
                'industry_Consumer Product Rental',
                'industry_Consumer Products Manufacturing',
                'industry_Department, Clothing, & Shoe Stores',
                'industry_Drug & Health Stores',
                'industry_Electrical & Electronic Manufacturing',
                'industry_Energy',
                'industry_Enterprise Software & Network Solutions',
                'industry_Express Delivery Services',
                'industry_Farm Support Services',
                'industry_Federal Agencies',
                'industry_Financial Analytics & Research',
                'industry_Financial Transaction Processing',
                'industry_Food & Beverage Manufacturing',
                'industry_Gambling',
                'industry_Gas Stations',
                'industry_Gift, Novelty & Souvenir Stores',
                'industry_Health Care Products Manufacturing',
                'industry_Health Care Services & Hospitals',
                'industry_Home Centers & Hardware Stores',
                'industry_Home Furniture & Housewares Stores',
                'industry_IT Services',
                'industry_Industrial Manufacturing',
                'industry_Insurance Agencies & Brokerages',
                'industry_Insurance Carriers',
                'industry_Internet',
                'industry_Investment Banking & Asset Management',
                'industry_K-12 Education',
                'industry_Legal',
                'industry_Lending',
                'industry_Logistics & Supply Chain',
                'industry_Membership Organizations',
                'industry_Miscellaneous Manufacturing',
                'industry_Municipal Governments',
                'industry_Preschool & Child Care',
                'industry_Real Estate',
                'industry_Religious Organizations',
                'industry_Research & Development',
                'industry_Security Services',
                'industry_Social Assistance',
                'industry_Staffing & Outsourcing',
                'industry_State & Regional Agencies',
                'industry_Telecommunications Manufacturing',
                'industry_Telecommunications Services',
                'industry_Transportation Equipment Manufacturing',
                'industry_Transportation Management',
                'industry_Wholesale',
))

    st.write('You selected:', option)
    features[option] = 1 

    # sector
    option = st.selectbox(
        'Choose sector: ',
        ('sector_Accounting & Legal',
                'sector_Aerospace & Defense',
                'sector_Agriculture & Forestry',
                'sector_Arts, Entertainment & Recreation',
                'sector_Biotech & Pharmaceuticals',
                'sector_Business Services',
                'sector_Consumer Services',
                'sector_Education',
                'sector_Finance',
                'sector_Government',
                'sector_Health Care',
                'sector_Information Technology',
                'sector_Insurance',
                'sector_Manufacturing',
                'sector_Non-Profit',
                'sector_Oil, Gas, Energy & Utilities',
                'sector_Real Estate',
                'sector_Retail',
                'sector_Telecommunications',
                'sector_Transportation & Logistics'))

    st.write('You selected:', option)
    features[option] = 1 


# revenue
    option = st.selectbox(
        'Choose revenue: ',
        ('revenue_1-2b',
                'revenue_1-5m',
                'revenue_10-25m',
                'revenue_100-500m',
                'revenue_10b',
                'revenue_2-5b',
                'revenue_25-50m',
                'revenue_5-10m',
                'revenue_50-100m',
                'revenue_500m-1b',
                'revenue_<1m'))

    st.write('You selected:', option)
    features[option] = 1     


# city
    option = st.selectbox(
        'Choose revenue: ',
        ('city_Albany',
                'city_Altamonte Springs',
                'city_Anchorage',
                'city_Ankeny',
                'city_Ann Arbor',
                'city_Arlington',
                'city_Ashburn',
                'city_Atlanta',
                'city_Austin',
                'city_Baltimore',
                'city_Beaverton',
                'city_Bellevue',
                'city_Bethesda',
                'city_Birmingham',
                'city_Bloomington',
                'city_Bonita Springs',
                'city_Boston',
                'city_Boulder',
                'city_Bowie',
                'city_Brea',
                'city_Brentwood',
                'city_Bridgeton',
                'city_Brooklyn',
                'city_Brooklyn Heights',
                'city_Burlingame',
                'city_Cambridge',
                'city_Carlsbad',
                'city_Carson',
                'city_Center Valley',
                'city_Charlotte',
                'city_Chaska',
                'city_Chicago',
                'city_Chico',
                'city_Cincinnati',
                'city_Clarksburg',
                'city_Colmar',
                'city_Colorado Springs',
                'city_Columbia',
                'city_Columbus',
                'city_Culver City',
                'city_Dallas',
                'city_Danville',
                'city_Deerfield',
                'city_Denver',
                'city_Detroit',
                'city_Dublin',
                'city_Durham',
                'city_Eden Prairie',
                'city_Englewood',
                'city_Eugene',
                'city_Eureka',
                'city_Fairport',
                'city_Falls Church',
                'city_Flint',
                'city_Florham Park',
                'city_Fort Wayne',
                'city_Fremont',
                'city_Ft Carson',
                'city_Garden City',
                'city_Gilbert',
                'city_Glendale',
                'city_Golden',
                'city_Grand Prairie',
                'city_Greensboro',
                'city_Harrisburg',
                'city_Hartford',
                'city_Hayward',
                'city_Herndon',
                'city_Highland',
                'city_Houston',
                'city_Indianapolis',
                'city_Industry',
                'city_Irving',
                'city_Jacksonville',
                'city_Jersey City',
                'city_Kansas City',
                'city_King of Prussia',
                'city_Ladera Ranch',
                'city_Lafayette',
                'city_Lake Mary',
                'city_Lancaster',
                'city_Laramie',
                'city_Las Vegas',
                'city_Leander',
                'city_Lenexa',
                'city_Long Beach',
                'city_Los Angeles',
                'city_Loveland',
                'city_Lowell',
                'city_Mahwah',
                'city_Malden',
                'city_McLean',
                'city_Medford',
                'city_Memphis',
                'city_Miami',
                'city_Miami Lakes',
                'city_Minneapolis',
                'city_Minnetonka',
                'city_Mount Laurel',
                'city_Mountain View',
                'city_Mundelein',
                'city_Naples',
                'city_Nashville',
                'city_New Britain',
                'city_New Haven',
                'city_New York',
                'city_Newark',
                'city_Newport News',
                'city_Norfolk',
                'city_Normal',
                'city_North Canton',
                'city_Northbrook',
                'city_Oakland',
                'city_Ogden',
                'city_Oklahoma',
                'city_Oklahoma City',
                'city_Orlando',
                'city_Palm Beach Gardens',
                'city_Palo Alto',
                'city_Parsippany',
                'city_Pasadena',
                'city_Philadelphia',
                'city_Phoenix',
                'city_Pittsburgh',
                'city_Plano',
                'city_Pleasanton',
                'city_Plymouth',
                'city_Portland',
                'city_Portsmouth',
                'city_Provo',
                'city_Quantico',
                'city_Raleigh',
                'city_Reading',
                'city_Reno',
                'city_Richardson',
                'city_Richmond',
                'city_Riverwoods',
                'city_Roanoke',
                'city_Rolling Meadows',
                'city_Rosemont',
                'city_Roswell',
                'city_Roy',
                'city_Sacramento',
                'city_Saint Louis',
                'city_Saint Petersburg',
                'city_Salt Lake City',
                'city_San Antonio',
                'city_San Diego',
                'city_San Francisco',
                'city_San Jose',
                'city_San Marcos',
                'city_Santa Barbara',
                'city_Santa Clara',
                'city_Santa Cruz',
                'city_Scottsdale',
                'city_Seattle',
                'city_Sellersville',
                'city_Sheldonville',
                'city_Solon',
                'city_Somerset',
                'city_Springfield',
                'city_St Louis Park',
                'city_Stamford',
                'city_Stanford',
                'city_Stevens Point',
                'city_Sycamore',
                'city_Tampa',
                'city_Tempe',
                'city_Tigard',
                'city_Troy',
                'city_Urbandale',
                'city_Vienna',
                'city_Virginia',
                'city_Waltham',
                'city_Warrenton',
                'city_Washington',
                'city_Waterbury',
                'city_Wayne',
                'city_Wellesley',
                'city_West Palm Beach',
                'city_Westlake Village',
                'city_Westminster',
                'city_Wilmington',
                'city_Wilton',
                'city_Winchester',
                'city_Woodbury',
                'city_Worthington'))

    st.write('You selected:', option)
    features[option] = 1 


# state
    option = st.selectbox(
        'Choose type of ownership: ',
        ('state_AK',
                'state_AL',
                'state_AZ',
                'state_CA',
                'state_CO',
                'state_CT',
                'state_DC',
                'state_DE',
                'state_FL',
                'state_GA',
                'state_IA',
                'state_IL',
                'state_IN',
                'state_KS',
                'state_KY',
                'state_MA',
                'state_MD',
                'state_ME',
                'state_MI',
                'state_MN',
                'state_MO',
                'state_NC',
                'state_NH',
                'state_NJ',
                'state_NV',
                'state_NY',
                'state_OH',
                'state_OK',
                'state_OR',
                'state_PA',
                'state_TN',
                'state_TX',
                'state_UT',
                'state_VA',
                'state_VT',
                'state_WA',
                'state_WI',
                'state_WV',
                'state_WY'))

    st.write('You selected:', option)
    features[option] = 1 



    result = ""



result = ""
if st.button("Predict"):
    result=predict_note_authentication(list(features.values()))
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
