import webbrowser
import time
import random
import os
import pyautogui

#holy shit this is hot garbage jank
def mobileSearches():
	items = len(mobileSearchTerms) - 1
	mobileCount = 0
	tab = 16

	webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(searchURL + searchTerms[1].lower())
	time.sleep(3)
	pyautogui.press('f12')
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'shift', 'm')
	time.sleep(1)
	pyautogui.press('f5')
	time.sleep(3)
	while tab > 0:
		pyautogui.press('tab')
		tab = tab - 1
	while mobileCount < 1:
		index = random.randint(0,items)
		cooldown = random.randint(6, 19)
		pyautogui.hotkey('ctrl','a')
		pyautogui.press('delete')
		pyautogui.press(mobileSearchTerms[index])
		pyautogui.press('enter')
		time.sleep(1)
		pyautogui.press('tab')
		mobileCount += 1
		print("Mobile search " + str(mobileCount) + " of 30 completed.")
		time.sleep(cooldown)
	print("Mobile searches done. Reseting Chrome settings...")
	time.sleep(1)
	pyautogui.hotkey('ctrl', 'shift', 'm')
	time.sleep(1)
	pyautogui.press('f5')
	time.sleep(2)
	pyautogui.press('f12')
	time.sleep(1)
def pcSearches():
	items = len(searchTerms) - 1
	googleCount = 0
	edgeCount = 0

	clear = lambda: os.system('cls')

	print('Opening browsers...')
	webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://www.bing.com')
	webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open('https://www.bing.com')
	time.sleep(3)

	while googleCount < 35:
		index = random.randint(0,items)
		cooldown = random.randint(6, 19)
		webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(searchURL + searchTerms[index].lower())
		googleCount += 1
		print('Chrome search ' + str(googleCount) + ' of 35 completed.')
		time.sleep(cooldown)

	print('Chrome searches completed. Closing all Chrome tabs and starting Edge searches...')
	time.sleep(3)
	os.system('taskkill /im chrome.exe /f')
	clear()

	while edgeCount < 7:
		index = random.randint(0,items)
		cooldown = random.randint(6,19)
		webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open(searchURL + searchTerms[index].lower())
		edgeCount += 1
		print('Edge search ' + str(edgeCount) + ' of 7 completed.')
		time.sleep(cooldown)

	print('Edge searches completed. Closing all Edge tabs and redirecting to Microsoft Rewards page.')
	time.sleep(3)
	os.system('taskkill /im msedge.exe /f')
	clear()
	webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open('https://account.microsoft.com/rewards/pointsbreakdown')
	
mobileSearchTerms=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

searchURL = 'https://www.bing.com/search?q='
searchTerms=['San Francisco 49ers',
'Chicago Bears',
'Cincinnati Bengals',
'Buffalo Bills',
'Denver Broncos',
'Cleveland Browns',
'Tampa Bay Buccaneers',
'Arizona Cardinals',
'San Diego Chargers',
'Kansas City Chiefs',
'Indianapolis Colts',
'Dallas Cowboys',
'Miami Dolphins',
'Philadelphia Eagles',
'Atlanta Falcons',
'New York Giants',
'Jacksonville Jaguars',
'New York Jets',
'Detroit Lions',
'Green Bay Packers',
'Carolina Panthers',
'New England Patriots',
'Oakland Raiders',
'Los Angeles Rams',
'Baltimore Ravens',
'Washington Redskins',
'New Orleans Saints',
'Seattle Seahawks',
'Pittsburgh Steelers',
'Tennessee Titans',
'Minnesota Vikings',
'Atlanta Hawks',
'Boston Celtics',
'Charlotte Hornets',
'Chicago Bulls',
'Cleveland Cavaliers',
'Dallas Mavericks',
'Denver Nuggets',
'Detroit Pistons',
'Golden State Warriors',
'Houston Rockets',
'Indiana Pacers',
'Los Angeles Clippers',
'Los Angeles Lakers',
'Miami Heat',
'Milwaukee Bucks',
'Minnesota Timberwolves',
'New Jersey Nets',
'New York Knicks',
'Orlando Magic',
'Philadelphia 76ers',
'Phoenix Suns',
'Portland Trail Blazers',
'Sacramento Kings',
'San Antonio Spurs',
'Seattle Supersonics',
'Toronto Raptors',
'Utah Jazz',
'Vancouver Grizzlies',
'Washington Wizards',
'Washington Bullets',
'Anaheim Angels',
'Arizona Diamondbacks',
'Atlanta Braves',
'Baltimore Orioles',
'Boston Red Sox',
'Chicago Cubs',
'Chicago White Sox',
'Cincinnati Reds',
'Cleveland Indians',
'Colorado Rockies',
'Detroit Tigers',
'Florida Marlins',
'Houston Astros',
'Kansas City Royals',
'Los Angeles Dodgers',
'Milwaukee Brewers',
'Minnesota Twins',
'Montreal Expos',
'New York Mets',
'New York Yankees',
'Oakland Athletics',
'Philadelphia Phillies',
'Pittsburgh Pirates',
'San Diego Padres',
'San Francisco Giants',
'Seattle Mariners',
'St Louis Cardinals',
'Tampa Bay Devil Rays',
'Texas Rangers',
'Toronto Blue Jays',
'Anaheim Mighty Ducks',
'Boston Bruins',
'Buffalo Sabres',
'Calgary Flames',
'Carolina Hurricanes',
'Chicago Blackhawks',
'Colorado Avalanche',
'Dallas Stars',
'Detroit Red Wings',
'Edmonton Oilers',
'Florida Panthers',
'Hartford Whalers',
'Los Angeles Kings',
'Montreal Canadiens',
'Nashville Predators',
'New Jersey Devils',
'New York Islanders',
'New York Rangers',
'Ottawa Senators',
'Philadelphia Flyers',
'Phoenix Coyotes',
'Pittsburgh Penguins',
'Quebec Nordiques',
'San Jose Sharks',
'St Louis Blues',
'Tampa Bay Lightning',
'Toronto Maple Leafs',
'Vancouver Canucks',
'Washington Capitals',
'Winnipeg Jets',
'Afghanistan',
'Aland Islands',
'Albania',
'Algeria',
'American Samoa',
'Andorra',
'Angola',
'Anguilla',
'Antarctica',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Aruba',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bermuda',
'Bhutan',
'Bolivia',
'Bonaire, Sint Eustatius and Saba',
'Bosnia and Herzegovina',
'Botswana',
'Bouvet Island',
'Brazil',
'British Indian Ocean Territory',
'Brunei Darussalam',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cabo Verde',
'Cambodia',
'Cameroon',
'Canada',
'Cayman Islands',
'Central',
'Chad',
'Chile',
'China',
'Christmas Island',
'Cocos Islands',
'Colombia',
'Comoros',
'Congo',
'Cook Islands',
'Costa Rica',
'Cote dIvoire',
'Croatia',
'Cuba',
'Curacao',
'Cyprus',
'Czechia',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Eswatini',
'Ethiopia',
'Falkland Islands',
'Faroe Islands',
'Fiji',
'Finland',
'France',
'French Guiana',
'French Polynesia',
'French Southern Territories',
'Gabon',
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Gibraltar',
'Greece',
'Greenland',
'Grenada',
'Guadeloupe',
'Guam',
'Guatemala',
'Guernsey',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Heard Island and McDonald Islands',
'Holy See',
'Honduras',
'Hong Kong',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland',
'Isle of Man',
'Israel',
'Italy',
'Jamaica',
'Japan',
'Jersey',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea',
'Kuwait',
'Kyrgyzstan',
'Lao',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macao',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Martinique',
'Mauritania',
'Mauritius',
'Mayotte',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Montserrat',
'Morocco',
'Mozambique',
'Myanmar',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Caledonia',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Niue',
'Norfolk Island',
'North Macedonia',
'Northern Mariana Islands',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Palestine',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Pitcairn',
'Poland',
'Portugal',
'Puerto Rico',
'Qatar',
'Reunion',
'Romania',
'Russian Federation',
'Rwanda',
'Saint Barthelemy',
'Saint Helena',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Martin',
'Saint Pierre and Miquelon',
'Saint Vincent and the Grenadines',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Sint Maarten',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Georgia and the South Sandwich Islands',
'South Sudan',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Svalbard and Jan Mayen',
'Sweden',
'Switzerland',
'Syrian Arab Republic',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Timor-Leste',
'Togo',
'Tokelau',
'Tonga',
'Trinidad and Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Turks and Caicos Islands',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom of Great Britain and Northern Ireland',
'United States of America',
'United States Minor Outlying Islands',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Venezuela',
'Vietnam',
'Virgin Islands',
'Wallis and Futuna',
'Western Sahara',
'Yemen',
'Zambia',
'Zimbabwe']

mobileSearches()
pcSearches()

print('Bing searching done bruh!')
