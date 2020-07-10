"""
Created on Tue Jul  7 20:52:05 2020

@author: nachiketkale
"""
def countryByContinent(country):
    Africa=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic' ,'Chad ','Comoros ','Republic of the Congo','Democratic Republic of the Congo' ,'Ivory Coast''Djibouti','Egypt','Equatorial Guinea','Eritrea','Ethiopia','Gabon','Gambia' ,'Ghana' ,'Guinea','Guinea-Bissau','Kenya' ,'Lesotho','Liberia','Libya' ,'Madagascar','Malawi','Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger' ,'Nigeria','Rwanda','Senegal','Seychelles','Sierra Leone','Somalia','South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Western Sahara','Zambia','Zimbabwe' ]
    Antartica=['Antarctica']
    Asia=['Afghanistan','Armenia','Azerbaijan','Bahrain' ,'Bangladesh','Bhutan','Brunei' ,'Cambodia' ,'China' ,'East Timor','Georgia ','India ','Indonesia' ,'Iran ','Iraq ','Israel' ,'Japan ','Jordan' ,'Kazakhstan' ,'Kuwait ','Kyrgyzstan' ,'Laos ','Lebanon','Malaysia' ,'Maldives' ,'Mongolia' ,'Myanmar ','Nepal ','North Korea','Oman ','Pakistan' ,'Philippines' ,'Palestine ','Qatar','Russia','Saudi Arabia' ,'Singapore ','South Korea' ,'Sri Lanka ','Syria ','Tajikistan' ,'Thailand ','Turkey','Turkmenistan','Taiwan','United Arab Emirates' ,'Uzbekistan','Vietnam','Yemen']
    Europe=['Albania', 'Andorra', 'Austria','Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland','France', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Republic of Ireland', 'Italy', 'Kosovo','Latvia', 'Liechtenstein','Lithuania', 'Luxembourg', 'North Macedonia', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia','San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain','Sweden ','Switzerland', 'Ukraine', 'UK', 'Vatican City']
    NorthAmerica=['Antigua and Barbuda','Anguilla', 'Aruba ','The Bahamas','Barbados','Belize','Bermuda','Bonaire','British Virgin Islands','Canada','Cayman Islands','Clipperton Island','Costa Rica','Cuba','Curaçao','Dominica','Dominican Republic','El Salvador','Greenland','Grenada','Guadeloupe','Guatemala','Haiti','Honduras','Jamaica','Martinique','Mexico','Montserrat','Navassa Island','Nicaragua','Panama','Puerto Rico','Saba', 'Saint Barthelemy','Saint Kitts and Nevis','Saint Lucia', 'Saint Martin','Saint Pierre and Miquelon','Saint Vincent and the Grenadines', 'Sint Eustatius','Sint Maarten','Trinidad and Tobago','Turks and Caicos','US','Virgin Islands']
    SouthAmerica=['Argentina','Bolivia','Brazil','Chile','Colombia','Ecuador','Falkland Islands','French Guiana','Guyana','Paraguay','Peru','South Georgia and the South Sandwich Islands', 'Suriname ','Uruguay','Venezuela']
    Australia=['Australia','Micronesia','Fiji','Kiribati', 'Marshall Islands','Nauru','New Zealand','Palau','Papua New Guinea', 'Samoa','Solomon Islands','Tonga', 'Tuvalu','Vanuatu']
    
    if country in Africa :
        return "Africa"
    elif country in Antartica :
        return "Antartica"
    elif country in Asia :
        return "Asia"
    elif country in Europe :
        return "Europe"
    elif country in NorthAmerica :
        return "North America"
    elif country in SouthAmerica :
        return "South America"
    elif country in Australia :
        return "Australia"
    else:
        return None
    

