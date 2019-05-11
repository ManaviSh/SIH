import pandas as pd
from ev import vehicle
import numpy as np
import matplotlib.pyplot as plt 
def main():
    print('hello')
    #Power = vehicle()
    data = pd.read_excel (r'C:\Users\manav\Downloads\Datasets\Trip_1.xls') 
    df = pd.DataFrame(data, columns= ['Time','Speed', 'Acceleration', 'Inclination_x', 'Inclination_y', 'Power (kW)'])
    d = np.array(df.as_matrix())
    Time = d[:, 0]
    Speed = d[:, 1]
    Acceleration = d[:, 2]
    Inclination_x = d[:, 3]
    Inclination_y = d[:, 4]
    Pw = d[:, 5]
    Power = vehicle()
    P = Power.Power_Required(Speed, Inclination_x, Inclination_y, Acceleration)

    plt.plot(Time, Pw, label = "Obs")  
    plt.plot(Time, P, label = "Power Required") 
    plt.xlabel('Time')
    plt.ylabel('y - axis')
    plt.title('Comparision') 
    plt.legend() 
    plt.show() 
    with open('do.csv', 'wb') as abc:
       np.savetxt(abc, P, delimiter=",")
    
if __name__ == "__main__":
    main()