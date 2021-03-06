import pandas as pd
from ev import vehicle
import numpy as np
import matplotlib.pyplot as plt 
#from test1 import policy
def main():
    #Power = vehicle()
    data = pd.read_excel ('trip.xlsx') 
    df = pd.DataFrame(data, columns= ['Time','Speed', 'Acceleration', 'Inclination_x', 'Inclination_y', 'Power(kW)', 'Inclination'])
    d = np.array(df.as_matrix())
    Time = d[:, 0]
    Speed = d[:, 1]
    Acceleration = d[:, 2]
    Inclination_x = d[:, 3] #cos theta
    Inclination_y = d[:, 4] #sin theta
    Pw = d[:, 5]
    #inclination=d[:,6]
    Power = vehicle()
    P = Power.Power_Required(Speed, Inclination_x, Inclination_y, Acceleration)
    #from test1 import acc,vel
    
    plt.plot(Time, Pw, label = "Obs")  
    plt.plot(Time, P, label = "Power Required") 
    plt.xlabel('Time')
    plt.ylabel('y - axis')
    plt.title('Comparision') 
    plt.legend() 
    plt.show() 
    with open('do_2.csv', 'wb') as abc:
       np.savetxt(abc, P, delimiter=",")
    
if __name__ == "__main__":
    main()
