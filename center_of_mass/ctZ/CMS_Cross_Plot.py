import matplotlib.pyplot as plt 
import numpy as np 
import sys 
import uncertainties 
from scipy.optimize import curve_fit
from matplotlib import colors


def main():

    run, tag, cross, error, Nb_event = np.genfromtxt('1/cross_sections.txt', unpack = True)

    desired_cms = np.arange(345,376,1)
   # desired_cms = desired_cms/2
   # desired_cms = np.asarray(desired_cms)

    #def fit(x,a,b,c):
    #    return a + b*x + c*x**2
#
    #params,cov = curve_fit(fit, coefficients, cross)
    #errors = np.sqrt(np.diag(cov))
    #a = params[0]
    #b = params[1]
    #c = params[2]
    #
    #t = np.linspace(-20,20,1000)
    print(len(desired_cms))
    print(len(cross))
    print(desired_cms)
    plt.plot(desired_cms, cross, 'o', color='deeppink')

    #plt.plot(desired_cms, cross2[1:], '-', color='green')
    #plt.plot(desired_cms, cross3, '-', color='green')

    #plt.plot(desired_cms, cross4, '-', color='lightblue')
    #plt.plot(desired_cms, cross5, '-', color='lightblue')

    plt.grid()
    plt.xlabel('$\sqrt{s}$/ [GeV]')
    plt.ylabel('$\sigma$ / [pb]')
    plt.title('$e^+e^-$-> tt~'  '   '   'ctZ = 1' '   ' 'dim6top_LO_UFO' ' '' ' '$m_t$ = 172.0 GeV' ' ''  ' '$w_t$ = 1.51 GeV' )
    plt.savefig('ctZ_1_CMS_cross_section_defaults.pdf')
    plt.show()
if __name__ == "__main__":
   main()
