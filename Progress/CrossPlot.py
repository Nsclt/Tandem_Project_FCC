import matplotlib.pyplot as plt 
import numpy as np 
import sys 
import uncertainties 
from scipy.optimize import curve_fit
from matplotlib import colors


def main():
    #coefficient = sys.argv[1]
    #center = str(sys.argv[2])
    #stepspace = float(sys.argv[3])
    #positivesteps = int(sys.argv[4])
    #negativesteps = int(sys.argv[5])
    #scriptname = sys.argv[6]
    #outputdir = sys.argv[7]


    #run, tag, cross, error, Nb_event = np.genfromtxt(outputdir +'/'+ center + '/' + coefficient +'/cross_sections.txt', unpack = True)

    run, tag, cross, error, Nb_event = np.genfromtxt('OtB/172.5/ctZ/cross_sections_narrow.txt', unpack = True)

    positivesteps = 10
    negativesteps = 40
    stepspace = 0.1
    new= 1

    positiverange = []
    negativerange = []
    zero = []
    c = 0 
    for i in range(positivesteps):
        c = c + stepspace 
        positiverange.append(c) 

    for i in range(new):
        c = 0
        zero.append(c)
    c = 0
    for i in range(negativesteps):
        c = c - stepspace
        negativerange.append(c)
    
    coefficients = zero + positiverange + negativerange 
    coefficients = np.asarray(coefficients)


    sin_squared_weinberg = 0.2312215
    #OtZ = cos(tetha) OtW3 - sin(tetha) OtB 
    #Otb = -arcsin(tetha) OtZ

    def fit(x,a,b,c):
        return a + b*x + c*x**2

    params,cov = curve_fit(fit, coefficients, cross)
    errors = np.sqrt(np.diag(cov))
    a = params[0]
    b = params[1]
    c = params[2]
    a_err= np.sqrt(cov[0][0])
    b_err = np.sqrt(cov[1][1])
    c_err = np.sqrt(cov[2][2])

    print('value a:',a ,'with error', a_err)
    print('value b:',b ,'with error', b_err)
    print('value c:',c ,'with error', c_err)

    t = np.linspace(-20,20,1000)

    plt.plot(coefficients, cross, 'o', color='deeppink')
    plt.errorbar(coefficients,cross, yerr=error ,xerr=None, fmt='o', color='deeppink')
    plt.plot(t, fit(t, a,b,c), 'k-')
    plt.hlines(0.1369516 , -20,20, 'crimson', linestyle='solid', label='SM Value')
    plt.hlines(0.1229516 , -20,20, 'pink', linestyle='solid', label='lower limit on SM')
    plt.hlines(0.1509516 , -20,20, 'pink', linestyle='solid', label='lower limit on SM')
    plt.fill_between(t, 0.1229516,0.1509516 ,facecolor='pink')
    plt.xlim(-4.2,1.2)
    plt.ylim(0,0.4)
    plt.grid()
    plt.xlabel('ctB')
    plt.ylabel('$\sigma$ / pb')
    plt.legend(loc='best')
    plt.title('$e^+e^-$-> tt~'  '   '   '$\sqrt{s} = 345$GeV' '   ' 'dim6top_LO_UFO' )
    plt.savefig('345_OtB_cross_section_narrow_band.pdf')
    plt.show()
if __name__ == "__main__":
   main()