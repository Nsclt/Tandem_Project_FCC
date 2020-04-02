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


    run_172, tag_172, cross_172, error_172, Nb_event_172 = np.genfromtxt('Scenario_interference/172.5/cross_sections.txt', unpack = True)
    run_177, tag_177, cross_177, error_177, Nb_event_177 = np.genfromtxt('Scenario_interference/177.5/cross_sections.txt', unpack = True)
    run_182, tag_182, cross_182, error_182, Nb_event_182 = np.genfromtxt('Scenario_interference/182.5/cross_sections.txt', unpack = True)
    run_250, tag_250, cross_250, error_250, Nb_event_250 = np.genfromtxt('Scenario_interference/250/cross_sections.txt', unpack = True)


    C = np.c_[ctW_array_mix, ctZ_array_mix]
    def three_dimensional_ctZ_ctW(C, 
                                    v_sm_sm,
                                    v_sm_ctZ, v_ctW_sm,
                                    v_ctW_ctZ,
                                    v_ctW_ctW, v_ctZ_ctZ):
        ctW = C[:,0]
        ctZ = C[:,1]
        return v_sm_sm + v_sm_ctZ * ctZ + v_ctW_sm * ctW + v_ctW_ctZ * ctW * ctZ + v_ctW_ctW * ctW * ctW + v_ctZ_ctZ * ctZ * ctZ 
    

    params_172, cov_172 = curve_fit(three_dimensional_ctZ_ctW, C, cross_172)
    errors_172 = np.sqrt(np.diag(cov_172))
    print('HERE ITS INTERFERENCE FOR 172.5 GEV')
    print('172.5 v_sm_sm :', params_172[0], '\pm', errors_172[0] )
    print('172.5 v_sm_ctZ :', params_172[1], '\pm', errors_172[1] )
    print('172.5 v_ctW_sm :', params_172[2], '\pm', errors_172[2] )
    print('172.5 v_ctW_ctZ :', params_172[3], '\pm', errors_172[3] )
    print('172.5 v_ctW_ctW :', params_172[4], '\pm', errors_172[4] )
    print('172.5 v_ctZ_ctZ :', params_172[5], '\pm', errors_172[5] )
    print('')
    print('')
    print('')
    params_177, cov_177 = curve_fit(three_dimensional_ctZ_ctW, C, cross_177)
    errors_177 = np.sqrt(np.diag(cov_177))
    print('HERE ITS INTERFERENCE FOR 177.5 GEV')
    print('177.5 v_sm_sm :', params_177[0], '\pm', errors_177[0] )
    print('177.5 v_sm_ctZ :', params_177[1], '\pm', errors_177[1] )
    print('177.5 v_ctW_sm :', params_177[2], '\pm', errors_177[2] )
    print('177.5 v_ctW_ctZ :', params_177[3], '\pm', errors_177[3] )
    print('177.5 v_ctW_ctW :', params_177[4], '\pm', errors_177[4] )
    print('177.5 v_ctZ_ctZ :', params_177[5], '\pm', errors_177[5] )
    print('')
    print('')
    print('')
    params_182, cov_182 = curve_fit(three_dimensional_ctZ_ctW, C, cross_182)
    errors_182 = np.sqrt(np.diag(cov_182))
    print('HERE ITS INTERFERENCE FOR 182.5 GEV')
    print('182.5 v_sm_sm :', params_182[0], '\pm', errors_182[0] )
    print('182.5 v_sm_ctZ :', params_182[1], '\pm', errors_182[1] )
    print('182.5 v_ctW_sm :', params_182[2], '\pm', errors_182[2] )
    print('182.5 v_ctW_ctZ :', params_182[3], '\pm', errors_182[3] )
    print('182.5 v_ctW_ctW :', params_182[4], '\pm', errors_182[4] )
    print('182.5 v_ctZ_ctZ :', params_182[5], '\pm', errors_182[5] )
    print('')
    print('')
    print('')   
    params_250, cov_250 = curve_fit(three_dimensional_ctZ_ctW, C, cross_250)
    errors_250 = np.sqrt(np.diag(cov_250))
    print('HERE ITS INTERFERENCE FOR 250 GEV')
    print('250 v_sm_sm :', params_250[0], '\pm', errors_250[0] )
    print('250 v_sm_ctZ :', params_250[1], '\pm', errors_250[1] )
    print('250 v_ctW_sm :', params_250[2], '\pm', errors_250[2] )
    print('250 v_ctW_ctZ :', params_250[3], '\pm', errors_250[3] )
    print('250 v_ctW_ctW :', params_250[4], '\pm', errors_250[4] )
    print('250 v_ctZ_ctZ :', params_250[5], '\pm', errors_250[5] )
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