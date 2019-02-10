import csv
import pandas as pd

csvName = 'OneDrive_1_2-9-2019/ASRS_DBOnline_2018.csv'

df = pd.read_csv(csvName)
synopsis = df['Report 1.2']
flightPhase = df['Assessments.1']
environment = df['Environment.1']
makeModelName = df['Aircraft 1.2']
primaryProblem = df['Aircraft 1.9']
light = df['Environment.3']

environmentArr = ['Turbulence', 'Rain', 'Icing', 'Cloudy', 'Fog', 'Thunderstorm', 'Snow', 'Windshear', 'Clear']

flightPhaseArr = ['Climb', 'Descent', 'Landing', 'Taxi', 'Parked', 'Cruise', 'Initial Approach', 'Initial Climb', 'Final Approach', 'Takeoff', 'Other Parked pre-departure', 'Other Go Around', 'Other Preflight planning', 'Other Deplaning', 'Other boarding', 'Other Load Planning', 'Other Standing', 'Other All', 'Other Non-Flight', 'Other Push-back', 'Other Gate', 'Other Under Tow into hangar']

primaryProblemArr = ['Aircraft', 'Procedure', 'Equipment / Tooling', 'Human Factors', 'Chart Or Publication', 'Weather', 'Airport', 'Ambiguous', 'Airspace Structure', 'ATC Equipment / Nav Facility / Buildings', 'Company Policy', 'Manuals', 'MEL', 'Incorrect / Not Installed / Unavailable Part', 'Environment - Non Weather Related', 'Staffing', 'Logbook Entry']

makeModelNameArr = ['A319','A320','A321','CRJ700','CRJ900','CRJ200','B737','B767','B777']

lightArr = ['Dawn', 'Daylight', 'Dusk', 'Night']