Countries = ['United States', 'Egypt', 'Equatorial Guinea', 'Costa Rica',
       'Senegal', 'Guyana', 'Malta', 'Bolivia', 'Anguilla',
       'Turks and Caicos Islands', 'Saint Vincent and the Grenadines',
       'Italy', 'Pakistan', 'Iceland', 'Marshall Islands', 'Luxembourg',
       'Honduras', 'The Bahamas', 'El Salvador', 'Samoa', 'Kazakhstan',
       'Switzerland', 'Sint Maarten', 'Hong Kong', 'Trinidad and Tobago',
       'Latvia', 'Slovakia', 'Suriname', 'Mexico', 'Ecuador', 'Colombia',
       'Norway', 'Thailand', 'Venezuela', 'Panama', 'Morocco',
       'Antigua and Barbuda', 'Azerbaijan', 'New Zealand', 'Liberia',
       'Hungary', 'Sweden', 'Israel', 'Ethiopia', 'Martinique',
       'Saint Barthelemy', 'Barbados', 'Germany', 'Kyrgyzstan', 'Ireland',
       'Malaysia', 'Cyprus', 'Qatar', 'Fiji', 'Saint Kitts and Nevis',
       'Taiwan', 'Haiti', 'Kuwait', 'Canada',
       'Federated States of Micronesia', 'Jamaica', 'Dominican Republic',
       'Japan', 'Finland', 'Aruba', 'French Guiana', 'India',
       'British Virgin Islands', 'Brazil', 'French Polynesia',
       'United Arab Emirates', 'Singapore', 'Netherlands', 'China',
       'Denmark', 'Peru', 'Argentina', 'Cayman Islands', 'South Africa',
       'Spain', 'Netherlands Antilles', 'Bermuda', 'Kiribati',
       'Saudi Arabia', 'Czech Republic', 'Belgium', 'Afghanistan',
       'Curacao', 'Georgia', 'Philippines', 'Grenada', 'Cape Verde',
       'Ukraine', 'Russia', 'Guatemala', 'Saint Lucia', 'Paraguay',
       'Turkey', 'United Kingdom', 'Cuba', 'Dominica', 'Portugal',
       'Bahrain', 'Vietnam', 'Belize', 'Nicaragua', 'Austria', 'Jordan',
       'Palau', 'Uganda', 'South Korea', 'Angola', 'Ghana', 'Guadeloupe',
       'France', 'Poland', 'Nigeria', 'Greenland', 'Chile', 'Australia',
       'Uruguay', 'Cook Islands', 'Bulgaria',
       'Bonaire, Sint Eustatius, and Saba', 'Greece', 'Yemen',
       'The Gambia', 'Guinea', 'Croatia', 'Belarus', 'Libya', 'Macau',
       'Togo', 'Romania', 'Mauritania', 'Saint Martin', 'Namibia',
       'Lebanon', 'Oman', 'Cameroon', 'Sierra Leone', 'Tunisia',
       'Solomon Islands', 'New Caledonia', 'Algeria', 'Lithuania',
       'Rwanda', 'Burundi', 'Zimbabwe',
       'Saint Helena, Ascension, and Tristan da Cunha', 'Tanzania',
       'Nepal', 'Niger', 'Papua New Guinea', 'Indonesia', 'Kenya',
       'Brunei', 'Malawi', 'Gibraltar', 'Burkina Faso', 'Chad', 'Moldova',
       'Djibouti', 'Zambia', "Cote d'Ivoire", 'Kosovo', 'Iraq']

headerWritten = False
import random
import csv
col_names =  ['DEST_COUNTRY_NAME', 'ORIGIN_COUNTRY_NAME', 'count', 'Year']
with open('big-data-all.csv','a') as f1:
    writer=csv.writer(f1, delimiter=',',lineterminator='\n',)


    # Only for first time
    if not headerWritten:
      writer.writerow(col_names)
      headerWritten = True

    for i in range(0,50000000):
      intYear = random.randint(1800, 2900)
      intCount = random.randint(0, 100)
      strDEST_COUNTRY_NAME = "'"+random.choice(Countries)+"'"
      strORIGIN_COUNTRY_NAME = "'"+random.choice(Countries)+"'"

      row = [strDEST_COUNTRY_NAME,strORIGIN_COUNTRY_NAME,intCount,intYear]
      writer.writerow(row)

import pandas as pd
df=pd.read_csv("/databricks/driver/big-data-all.csv")
outname = 'big-data-all.csv'
outdir = '/dbfs/mnt/data/data/'
df.to_csv(outdir+outname, index=False, encoding="utf-8")
