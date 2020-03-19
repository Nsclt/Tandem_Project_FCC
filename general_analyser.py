import matplotlib.pyplot as plt 
import numpy as np 
import sys 
import uncertainties 
from scipy.optimize import curve_fit
from matplotlib import colors
import itertools 

def main():

    run_W, tag_W, cross_W, error_W, Nb_event_W = np.genfromtxt('Scenario_ctW_only/cross_sections.txt', unpack=True)

    run_Z, tag_Z, cross_Z, error_Z, Nb_event_Z = np.genfromtxt('Scenario_ctZ_only/cross_sections.txt', unpack=True)


    coefficient_strength_Z = np.arange(-0.5,2.5,0.1)

    def two_dimensional_parabole_ctZ(ctZ, v_sm_Z, v_ctZ, v_ctZ_quad):
        return v_sm_Z + v_ctZ * ctZ + v_ctZ_quad * ctZ**2

    params_Z, cov_Z = curve_fit(two_dimensional_parabole_ctZ, coefficient_strength_Z, cross_Z)
    errors_Z = np.sqrt(np.diag(cov_Z))
    v_sm_Z = params_Z[0]
    v_ctZ = params_Z[1]
    v_ctZ_quad = params_Z[2]

    v_sm_Z_error = np.sqrt(cov_Z[0][0])
    v_ctZ_error = np.sqrt(cov_Z[1][1])
    v_ctZ_quad_error = np.sqrt(cov_Z[2][2])

    print('')
    print('This is CtZ strength regarded:')
    print('')
    print('The function given is:  v_sm_Z + v_ctZ * ctZ + v_ctZ_quad * ctZ**2')
    print('')
    print('With v_sm_Z = ', v_sm_Z ,'\pm', v_sm_Z_error )
    print('With v_ctZ = ', v_ctZ ,'\pm', v_ctZ_error )
    print('With v_ctZ_quad = ', v_ctZ_quad ,'\pm', v_ctZ_quad_error)

    #######################################################################################

    def two_dimensional_parabole_ctW(ctW, v_sm_W, v_ctW, v_ctW_quad):
        return v_sm_W + v_ctW * ctW + v_ctW_quad * ctW**2

    coefficient_strength_W = np.arange(-2.5,0.5,0.1)


    params_W, cov_W = curve_fit(two_dimensional_parabole_ctW, coefficient_strength_W, cross_W)
    errors_W = np.sqrt(np.diag(cov_W))
    v_sm_W = params_W[0]
    v_ctW = params_W[1]
    v_ctW_quad = params_W[2]

    v_sm_W_error = np.sqrt(cov_W[0][0])
    v_ctW_error = np.sqrt(cov_W[1][1])
    v_ctW_quad_error = np.sqrt(cov_W[2][2])

    
    print('')
    print('')
    print('')
    print('This is CtW strength regarded:')
    print('')
    print('The function given is:  v_sm_W + v_ctW * ctW + v_ctW_quad * ctW**2')
    print('')
    print('With v_sm_W = ', v_sm_W ,'\pm', v_sm_W_error )
    print('With v_ctW = ', v_ctW ,'\pm', v_ctW_error )
    print('With v_ctW_quad = ', v_ctW_quad ,'\pm', v_ctW_quad_error)


    print('')
    print('')
    print('')
    ######################################################################################

    x = np.arange(-4.0,4.0,0.5)
    y = np.arange(-4.0,4.0,0.5)
    Iterations = list(itertools.product(x,y))

    #CtW corresponds to xi 
    #ctZ corresponds to yi 

    ctW_array_mix = []
    ctZ_array_mix = [] 

    for xi,yi in Iterations:
        ctW_array_mix.append(xi)
        ctZ_array_mix.append(yi)

    ctW_array_mix = np.asarray(ctW_array_mix)
    ctZ_array_mix = np.asarray(ctZ_array_mix)


    run_mix, tag_mix, cross_mix, error_mix, Nb_event_mix = np.genfromtxt('Scenario_interference/cross_sections.txt', unpack = True)


    C = np.c_[ctW_array_mix, ctZ_array_mix]
    def three_dimensional_ctZ_ctW(C, 
                                    v_sm_sm,
                                    v_sm_ctZ, v_ctW_sm,
                                    v_ctW_ctZ,
                                    v_ctW_ctW, v_ctZ_ctZ):
        ctW = C[:,0]
        ctZ = C[:,1]
        return v_sm_sm + v_sm_ctZ * ctZ + v_ctW_sm * ctW + v_ctW_ctZ * ctW * ctZ + v_ctW_ctW * ctW * ctW + v_ctZ_ctZ * ctZ * ctZ 
    

    params_mix, cov_mix = curve_fit(three_dimensional_ctZ_ctW, C, cross_mix)
    errors_mix = np.sqrt(np.diag(cov_mix))

    print('v_sm_sm :', params_mix[0], '\pm', errors_mix[0] )
    print('v_sm_ctZ :', params_mix[1], '\pm', errors_mix[1] )
    print('v_ctW_sm :', params_mix[2], '\pm', errors_mix[2] )
    print('v_ctW_ctZ :', params_mix[3], '\pm', errors_mix[3] )
    print('v_ctW_ctW :', params_mix[4], '\pm', errors_mix[4] )
    print('v_ctZ_ctZ :', params_mix[5], '\pm', errors_mix[5] )


        

    ################################################################################

    #t = np.linspace(-3,0.7,1000)
    #plt.plot(coefficient_strength_W, cross_W, 'o', color='deeppink')
    #plt.errorbar(coefficient_strength_W,cross_W, yerr=error_W ,xerr=None, fmt='o', color='deeppink')
    #plt.plot(t, two_dimensional_parabole_ctW(t, v_sm_W, v_ctW, v_ctW_quad))
    #plt.hlines(0.1351634 , -10,10, 'crimson', linestyle='solid', label='SM Value')
    #plt.hlines(0.1211634 , -10,10, 'pink', linestyle='solid', label='lower limit on SM')
    #plt.hlines(0.1491634 , -10,10, 'pink', linestyle='solid', label='lower limit on SM')
    #plt.fill_between(t, 0.1211634,0.1491634 ,facecolor='pink')
    #plt.grid()
    #plt.xlim(-2.3,0.5)
    #plt.ylim(0,0.4)
    #plt.xlabel('ctW')
    #plt.ylabel('$\sigma$ / pb')
    #plt.legend(loc='best')
    #plt.title('$e^+e^-$-> tt~'  '   '   '$\sqrt{s} = 345$GeV' '   ' 'dim6top_LO_UFO' )
    #plt.savefig('345_ctW_cross_section.pdf')
    #plt.show()


    ################################################################################


    #t = np.linspace(-1,3,1000)
    #plt.plot(coefficient_strength_Z, cross_Z, 'o', color='deeppink')
    #plt.errorbar(coefficient_strength_Z,cross_Z, yerr=error_Z ,xerr=None, fmt='o', color='deeppink')
    #plt.plot(t, two_dimensional_parabole_ctZ(t, v_sm_Z, v_ctZ, v_ctZ_quad))
    #plt.hlines(0.1368778 , -10,10, 'crimson', linestyle='solid', label='SM Value')
    #plt.hlines(0.1228778 , -10,10, 'pink', linestyle='solid', label='lower limit on SM')
    #plt.hlines(0.1508778 , -10,10, 'pink', linestyle='solid', label='lower limit on SM')
    #plt.fill_between(t, 0.1228778,0.1508778 ,facecolor='pink')
    #plt.grid()
    #plt.xlabel('ctZ')
    #plt.xlim(-0.6,2.5)
    #plt.ylim(0,0.5)
    #plt.ylabel('$\sigma$ / pb')
    #plt.legend(loc='best')
    #plt.title('$e^+e^-$-> tt~'  '   '   '$\sqrt{s} = 345$GeV' '   ' 'dim6top_LO_UFO' )
    #plt.savefig('345_ctZ_cross_section.pdf')
    #plt.show()

if __name__ == "__main__":
   main()