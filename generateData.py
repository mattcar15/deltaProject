import pandas as pd

fileName = 'data/ASRS_DBOnline_2018.csv'
df = pd.read_csv(fileName)


#Synopsis => CR
flightPhase = df['Aircraft 1.9'] # mult! ;
environment = df['Environment.1'] # mult ;
makeModelName = df['Aircraft 1.2'] # a mess
primaryProblem = df['Assessments.1']
light = df['Environment.3']
synopsis = df['Report 1.2']


dataAll =[flightPhase, environment,  makeModelName,primaryProblem, light]



#Flight Phase
#col Y
flightPhaseArr = ['Climb', 'Descent', 'Landing', 'Taxi', 'Parked', 'Cruise', 'Initial Approach', 'Initial Climb', 'Final Approach', 'Takeoff', 'Other Parked pre-departure', 'Other Go Around', 'Other Preflight planning', 'Other Deplaning', 'Other boarding', 'Other Load Planning', 'Other Standing', 'Other All', 'Other Non-Flight', 'Other Push-back', 'Other Gate', 'Other Under Tow into hangar']


#Weather Elements / Visibility
#col K
environmentArr = ['Turbulence', 'Rain', 'Icing', 'Cloudy', 'Fog', 'Thunderstorm', 'Snow', 'Windshear', 'Clear']


#make model
#col R
makeModelNameArr = ['A319','A320','A321','CRJ700','CRJ900','CRJ200','B737','B767','B777']

#Primary Problem
#col CM
primaryProblemArr = ['Aircraft', 'Procedure', 'Equipment / Tooling', 'Human Factors', 'Chart Or Publication', 'Weather', 'Airport', 'Ambiguous', 'Airspace Structure', 'ATC Equipment / Nav Facility / Buildings', 'Company Policy', 'Manuals', 'MEL', 'Incorrect / Not Installed / Unavailable Part', 'Environment - Non Weather Related', 'Staffing', 'Logbook Entry']


#Light
#col M
lightArr = ['Dawn', 'Daylight', 'Dusk', 'Night']



arrAll = [flightPhaseArr,environmentArr,makeModelNameArr, primaryProblemArr,lightArr]


def generate(classA, configA, classB, configB):
    counts = [0] * len(arrAll[classB])
    synp = []
    for num, configADatum in enumerate(dataAll[classA]):
        if(num != 0, configADatum != None):
            try:
                if (float(configADatum)):
                    pass
                    #print("NAN")
            except ValueError:
                #print("mnot NAN boi")
                #print("Config A", num, str(configADatum))
                #print(arrAll[classA][configA] , " =? " ,  str(configADatum))

                if (str(arrAll[classA][configA]) == str(configADatum)):
                    #print(arrAll[classA][configA])
                    try:
                        if (float(dataAll[classB][num])):
                            pass
                            #print("flt", float(dataAll[classB][num]));
                            #print(dataAll[classB][num])
                    except ValueError:
                        #print(str(dataAll[classB][num]), " in " , (str(arrAll[classB])))
                        def capture(input):
                            if (input in (arrAll[classB])):
                                counts[(arrAll[classB]).index(input)] += 1
                            if (str(arrAll[classB][configB]) in input):
                                synp.append(synopsis[num])

                        if (classB == 1 or classB == 2):
                            if (str(dataAll[classB][num]).find(';') > 0):
                                #print(str(dataAll[classB][num]))
                                splitted =  str(dataAll[classB][num]).split(';')
                                #print(splitted)
                                for inp in splitted:
                                    capture(inp)
                            else:
                                capture(str(dataAll[classB][num]))

                        else:
                            capture(str(dataAll[classB][num]))



    return [synp, counts]