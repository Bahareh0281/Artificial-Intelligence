for data in model_info : 
    # #map goal column to 1 or 0 
    # data['satisfaction'] = data['satisfaction'].map({'neutral or dissatisfied' : 0 ,'satisfied' :1} )

    # classify customer type
    data['Customer Type'] = data['Customer Type'].map({'Loyal Customer' : 1 ,'disloyal Customer' :0 } )

    # classify type of travel 
    data['Type of Travel'] = data['Type of Travel'].map({'Business travel' : 0 ,'Personal Travel' :1 } )
    # classify Class 
    data['Class'] = data['Class'].map({'Business' : 0 ,'Eco' :1 ,'Eco Plus' :2 } )

    #classify Gender 
    data['Gender'] = data['Gender'].map({'Male' : 0 ,'Female' :1 } )

    # classify age 
    data.loc[data['Age'] <= 16  , 'Age']                          = 0 
    data.loc[ (data['Age'] > 16 ) & (data['Age'] <= 32 ) , 'Age'] = 1 
    data.loc[ (data['Age'] > 32 ) & (data['Age'] <= 48 ) , 'Age'] = 2 
    data.loc[ (data['Age'] > 48 ) & (data['Age'] <= 64 ) , 'Age'] = 3
    data.loc[ (data['Age'] > 64 ) & (data['Age'] <= 80 ) , 'Age'] = 4
    data.loc[ (data['Age'] > 80 ) , 'Age']                        = 5

    # classify Arrival Delay in Minutes
    data.loc[  data['Arrival Delay in Minutes'] <= 60.0  , 'Arrival Delay in Minutes']                                                 = 0 
    data.loc[ (data['Arrival Delay in Minutes'] > 60.0 ) & (data['Arrival Delay in Minutes'] <= 120.0 ) ,  'Arrival Delay in Minutes']   = 1 
    data.loc[ (data['Arrival Delay in Minutes'] > 120.0 ) & (data['Arrival Delay in Minutes'] <= 180.0 ) , 'Arrival Delay in Minutes']   = 2 
    data.loc[ (data['Arrival Delay in Minutes'] > 180.0 ) & (data['Arrival Delay in Minutes'] <= 240.0 ) , 'Arrival Delay in Minutes']   = 3
    data.loc[ (data['Arrival Delay in Minutes'] > 240.0 ) & (data['Arrival Delay in Minutes'] <= 300.0 ) , 'Arrival Delay in Minutes']   = 4
    data.loc[ (data['Arrival Delay in Minutes'] > 360.0 ) & (data['Arrival Delay in Minutes'] <= 420.0 ) , 'Arrival Delay in Minutes']   = 5
    data.loc[ (data['Arrival Delay in Minutes'] > 420.0 ) & (data['Arrival Delay in Minutes'] <= 480.0 ) , 'Arrival Delay in Minutes']   = 6
    data.loc[ (data['Arrival Delay in Minutes'] > 480.0 ) & (data['Arrival Delay in Minutes'] <= 540.0 ) , 'Arrival Delay in Minutes']   = 7
    data.loc[ (data['Arrival Delay in Minutes'] > 540.0 ) & (data['Arrival Delay in Minutes'] <= 600.0 ) , 'Arrival Delay in Minutes']   = 8
    data.loc[ (data['Arrival Delay in Minutes'] > 600.0 ) & (data['Arrival Delay in Minutes'] <= 660.0 ) , 'Arrival Delay in Minutes']   = 9
    data.loc[ (data['Arrival Delay in Minutes'] > 660.0 ) & (data['Arrival Delay in Minutes'] <= 720.0 ) , 'Arrival Delay in Minutes']   = 10
    data.loc[ (data['Arrival Delay in Minutes'] > 720.0 ) & (data['Arrival Delay in Minutes'] <= 780.0 ) , 'Arrival Delay in Minutes']   = 11
    data.loc[ (data['Arrival Delay in Minutes'] > 780.0 ) & (data['Arrival Delay in Minutes'] <= 840.0 ) , 'Arrival Delay in Minutes']   = 12
    data.loc[ (data['Arrival Delay in Minutes'] > 840.0 ) & (data['Arrival Delay in Minutes'] <= 900.0 ) , 'Arrival Delay in Minutes']   = 13
    data.loc[ (data['Arrival Delay in Minutes'] > 900.0 ) & (data['Arrival Delay in Minutes'] <= 960.0 ) , 'Arrival Delay in Minutes']   = 14
    data.loc[ (data['Arrival Delay in Minutes'] > 960.0 ) & (data['Arrival Delay in Minutes'] <= 1020.0 ) , 'Arrival Delay in Minutes']  = 20
    data.loc[ (data['Arrival Delay in Minutes'] > 1020.0 ) & (data['Arrival Delay in Minutes'] <= 1080.0 ) , 'Arrival Delay in Minutes'] = 21
    data.loc[ (data['Arrival Delay in Minutes'] > 1080.0 ) & (data['Arrival Delay in Minutes'] <= 1140.0 ) , 'Arrival Delay in Minutes'] = 22
    data.loc[ (data['Arrival Delay in Minutes'] > 1140.0 ) & (data['Arrival Delay in Minutes'] <= 1200.0 ) , 'Arrival Delay in Minutes'] = 23
    data.loc[ (data['Arrival Delay in Minutes'] > 1200.0 ) , 'Arrival Delay in Minutes']                                               = 24
    data['Arrival Delay in Minutes'] = data['Arrival Delay in Minutes'].fillna(0)
    # classify Departure Delay in Minutes
    data.loc[  data['Departure Delay in Minutes'] <= 60  , 'Departure Delay in Minutes']                                                       = 0 
    data.loc[ (data['Departure Delay in Minutes'] > 60 ) &   (data['Departure Delay in Minutes'] <= 120 ) ,  'Departure Delay in Minutes']   = 1 
    data.loc[ (data['Departure Delay in Minutes'] > 120 ) &  (data['Departure Delay in Minutes'] <= 180 ) ,  'Departure Delay in Minutes']   = 2 
    data.loc[ (data['Departure Delay in Minutes'] > 180 ) &  (data['Departure Delay in Minutes'] <= 240 ) ,  'Departure Delay in Minutes']   = 3
    data.loc[ (data['Departure Delay in Minutes'] > 240 ) &  (data['Departure Delay in Minutes'] <= 300 ) ,  'Departure Delay in Minutes']   = 4
    data.loc[ (data['Departure Delay in Minutes'] > 360 ) &  (data['Departure Delay in Minutes'] <= 420 ) ,  'Departure Delay in Minutes']   = 5
    data.loc[ (data['Departure Delay in Minutes'] > 420 ) &  (data['Departure Delay in Minutes'] <= 480 ) ,  'Departure Delay in Minutes']   = 6
    data.loc[ (data['Departure Delay in Minutes'] > 480 ) &  (data['Departure Delay in Minutes'] <= 540 ) ,  'Departure Delay in Minutes']   = 7
    data.loc[ (data['Departure Delay in Minutes'] > 540 ) &  (data['Departure Delay in Minutes'] <= 600 ) ,  'Departure Delay in Minutes']   = 8
    data.loc[ (data['Departure Delay in Minutes'] > 600 ) &  (data['Departure Delay in Minutes'] <= 660 ) ,  'Departure Delay in Minutes']   = 9
    data.loc[ (data['Departure Delay in Minutes'] > 660 ) &  (data['Departure Delay in Minutes'] <= 720 ) ,  'Departure Delay in Minutes']   = 10
    data.loc[ (data['Departure Delay in Minutes'] > 720 ) &  (data['Departure Delay in Minutes'] <= 780 ) ,  'Departure Delay in Minutes']   = 11
    data.loc[ (data['Departure Delay in Minutes'] > 780 ) &  (data['Departure Delay in Minutes'] <= 840 ) ,  'Departure Delay in Minutes']   = 12
    data.loc[ (data['Departure Delay in Minutes'] > 840 ) &  (data['Departure Delay in Minutes'] <= 900 ) ,  'Departure Delay in Minutes']   = 13
    data.loc[ (data['Departure Delay in Minutes'] > 900 ) &  (data['Departure Delay in Minutes'] <= 960 ) ,  'Departure Delay in Minutes']   = 14
    data.loc[ (data['Departure Delay in Minutes'] > 960 ) &  (data['Departure Delay in Minutes'] <= 1020 ) , 'Departure Delay in Minutes']   = 20
    data.loc[ (data['Departure Delay in Minutes'] > 1020 ) & (data['Departure Delay in Minutes'] <= 1080 ) , 'Departure Delay in Minutes']   = 21
    data.loc[ (data['Departure Delay in Minutes'] > 1080 ) & (data['Departure Delay in Minutes'] <= 1140 ) , 'Departure Delay in Minutes']   = 22
    data.loc[ (data['Departure Delay in Minutes'] > 1140 ) & (data['Departure Delay in Minutes'] <= 1200 ) , 'Departure Delay in Minutes']   = 23
    data.loc[ (data['Departure Delay in Minutes'] > 1200 ) & (data['Departure Delay in Minutes'] <= 1260 ), 'Departure Delay in Minutes']    = 24
    data.loc[ (data['Departure Delay in Minutes'] > 1260 ) , 'Departure Delay in Minutes']                                                   = 25

    # classify Flight Distance

    data.loc[ (data['Flight Distance'] <= 1000 ) ,  'Flight Distance']                                      = 0
    data.loc[ (data['Flight Distance'] > 1000 ) & (data['Flight Distance'] <= 2000 ) ,  'Flight Distance']  = 1
    data.loc[ (data['Flight Distance'] > 2000 ) &  (data['Flight Distance'] <= 3000 ) , 'Flight Distance']  = 2
    data.loc[ (data['Flight Distance'] > 3000 ) & (data['Flight Distance'] <= 4000 ) , 'Flight Distance']   = 3
    data.loc[ (data['Flight Distance'] > 4000 ) , 'Flight Distance']                                        = 4
    
train = train.drop( "id", axis='columns' )
test = test.drop( "id", axis='columns' )