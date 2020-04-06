import matplotlib.pyplot as plt 
import numpy as np 
import sys 
import uncertainties 
from scipy.optimize import curve_fit
from matplotlib import colors
import itertools 

def main():

    run_W, tag_W, cross_W, error_W, Nb_event_W = np.genfromtxt('Scenario_ctW_only/174.5/cross_sections.txt', unpack=True)

    run_Z, tag_Z, cross_Z, error_Z, Nb_event_Z = np.genfromtxt('Scenario_ctZ_only/174.5/cross_sections.txt', unpack=True)


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


    run_345, tag_345, cross_345, error_345, Nb_event_345 = np.genfromtxt('Scenario_interference/172.5/cross_sections.txt', unpack = True)
    run_346, tag_346, cross_346, error_346, Nb_event_346 = np.genfromtxt('Scenario_interference/173/cross_sections.txt', unpack = True)
    run_347, tag_347, cross_347, error_347, Nb_event_347 = np.genfromtxt('Scenario_interference/173.5/cross_sections.txt', unpack = True)
    run_348, tag_348, cross_348, error_348, Nb_event_348 = np.genfromtxt('Scenario_interference/174/cross_sections.txt', unpack = True)
    run_349, tag_349, cross_349, error_349, Nb_event_349 = np.genfromtxt('Scenario_interference/174.5/cross_sections.txt', unpack = True)

    
    
    
    
    
    
    
    #run_177, tag_177, cross_177, error_177, Nb_event_177 = np.genfromtxt('Scenario_interference/177.5/cross_sections.txt', unpack = True)
    #run_182, tag_182, cross_182, error_182, Nb_event_182 = np.genfromtxt('Scenario_interference/182.5/cross_sections.txt', unpack = True)
    #run_250, tag_250, cross_250, error_250, Nb_event_250 = np.genfromtxt('Scenario_interference/250/cross_sections.txt', unpack = True)


    C = np.c_[ctW_array_mix, ctZ_array_mix]
    def three_dimensional_ctZ_ctW(C, 
                                    v_sm_sm,
                                    v_sm_ctZ, v_ctW_sm,
                                    v_ctW_ctZ,
                                    v_ctW_ctW, v_ctZ_ctZ):
        ctW = C[:,0]
        ctZ = C[:,1]
        return v_sm_sm + v_sm_ctZ * ctZ + v_ctW_sm * ctW + v_ctW_ctZ * ctW * ctZ + v_ctW_ctW * ctW * ctW + v_ctZ_ctZ * ctZ * ctZ 
    

    params_345, cov_345 = curve_fit(three_dimensional_ctZ_ctW, C, cross_345)
    errors_345 = np.sqrt(np.diag(cov_345))
    print('HERE ITS INTERFERENCE FOR 345 GEV')
    print('345 GeV v_sm_sm :', params_345[0], '\pm', errors_345[0] )
    print('345 GeV v_sm_ctZ :', params_345[1], '\pm', errors_345[1] )
    print('345 GeV v_ctW_sm :', params_345[2], '\pm', errors_345[2] )
    print('345 GeV v_ctW_ctZ :', params_345[3], '\pm', errors_345[3] )
    print('345 GeV v_ctW_ctW :', params_345[4], '\pm', errors_345[4] )
    print('345 GeV v_ctZ_ctZ :', params_345[5], '\pm', errors_345[5] )
    print('')
    print('')
    print('')
    params_346, cov_346 = curve_fit(three_dimensional_ctZ_ctW, C, cross_346)
    errors_346 = np.sqrt(np.diag(cov_346))
    print('HERE ITS INTERFERENCE FOR 346 GEV')
    print('346 GeV v_sm_sm :', params_346[0], '\pm', errors_346[0] )
    print('346 GeV v_sm_ctZ :', params_346[1], '\pm', errors_346[1] )
    print('346 GeV v_ctW_sm :', params_346[2], '\pm', errors_346[2] )
    print('346 GeV v_ctW_ctZ :', params_346[3], '\pm', errors_346[3] )
    print('346 GeV v_ctW_ctW :', params_346[4], '\pm', errors_346[4] )
    print('346 GeV v_ctZ_ctZ :', params_346[5], '\pm', errors_346[5] )
    print('')
    print('')
    print('')
    params_347, cov_347 = curve_fit(three_dimensional_ctZ_ctW, C, cross_347)
    errors_347 = np.sqrt(np.diag(cov_347))
    print('HERE ITS INTERFERENCE FOR 347 GEV')
    print('347 GeV v_sm_sm :', params_347[0], '\pm', errors_347[0] )
    print('347 GeV v_sm_ctZ :', params_347[1], '\pm', errors_347[1] )
    print('347 GeV v_ctW_sm :', params_347[2], '\pm', errors_347[2] )
    print('347 GeV v_ctW_ctZ :', params_347[3], '\pm', errors_347[3] )
    print('347 GeV v_ctW_ctW :', params_347[4], '\pm', errors_347[4] )
    print('347 GeV v_ctZ_ctZ :', params_347[5], '\pm', errors_347[5] )
    print('')
    print('')
    print('')
    params_348, cov_348 = curve_fit(three_dimensional_ctZ_ctW, C, cross_348)
    errors_348 = np.sqrt(np.diag(cov_348))
    print('HERE ITS INTERFERENCE FOR 348 GEV')
    print('348 GeV v_sm_sm :', params_348[0], '\pm', errors_348[0] )
    print('348 GeV v_sm_ctZ :', params_348[1], '\pm', errors_348[1] )
    print('348 GeV v_ctW_sm :', params_348[2], '\pm', errors_348[2] )
    print('348 GeV v_ctW_ctZ :', params_348[3], '\pm', errors_348[3] )
    print('348 GeV v_ctW_ctW :', params_348[4], '\pm', errors_348[4] )
    print('348 GeV v_ctZ_ctZ :', params_348[5], '\pm', errors_348[5] )
    print('')
    print('')
    print('')
    params_349, cov_349 = curve_fit(three_dimensional_ctZ_ctW, C, cross_349)
    errors_349 = np.sqrt(np.diag(cov_349))
    print('HERE ITS INTERFERENCE FOR 349 GEV')
    print('349 GeV v_sm_sm :', params_349[0], '\pm', errors_349[0] )
    print('349 GeV v_sm_ctZ :', params_349[1], '\pm', errors_349[1] )
    print('349 GeV v_ctW_sm :', params_349[2], '\pm', errors_349[2] )
    print('349 GeV v_ctW_ctZ :', params_349[3], '\pm', errors_349[3] )
    print('349 GeV v_ctW_ctW :', params_349[4], '\pm', errors_349[4] )
    print('349 GeV v_ctZ_ctZ :', params_349[5], '\pm', errors_349[5] )
    print('')
    print('')
    print('')












    #params_177, cov_177 = curve_fit(three_dimensional_ctZ_ctW, C, cross_177)
    #errors_177 = np.sqrt(np.diag(cov_177))
    #print('HERE ITS INTERFERENCE FOR 177.5 GEV')
    #print('177.5 v_sm_sm :', params_177[0], '\pm', errors_177[0] )
    #print('177.5 v_sm_ctZ :', params_177[1], '\pm', errors_177[1] )
    #print('177.5 v_ctW_sm :', params_177[2], '\pm', errors_177[2] )
    #print('177.5 v_ctW_ctZ :', params_177[3], '\pm', errors_177[3] )
    #print('177.5 v_ctW_ctW :', params_177[4], '\pm', errors_177[4] )
    #print('177.5 v_ctZ_ctZ :', params_177[5], '\pm', errors_177[5] )
    #print('')
    #print('')
    #print('')
    #params_182, cov_182 = curve_fit(three_dimensional_ctZ_ctW, C, cross_182)
    #errors_182 = np.sqrt(np.diag(cov_182))
    #print('HERE ITS INTERFERENCE FOR 182.5 GEV')
    #print('182.5 v_sm_sm :', params_182[0], '\pm', errors_182[0] )
    #print('182.5 v_sm_ctZ :', params_182[1], '\pm', errors_182[1] )
    #print('182.5 v_ctW_sm :', params_182[2], '\pm', errors_182[2] )
    #print('182.5 v_ctW_ctZ :', params_182[3], '\pm', errors_182[3] )
    #print('182.5 v_ctW_ctW :', params_182[4], '\pm', errors_182[4] )
    #print('182.5 v_ctZ_ctZ :', params_182[5], '\pm', errors_182[5] )
    #print('')
    #print('')
    #print('')   
    #params_250, cov_250 = curve_fit(three_dimensional_ctZ_ctW, C, cross_250)
    #errors_250 = np.sqrt(np.diag(cov_250))
    #print('HERE ITS INTERFERENCE FOR 250 GEV')
    #print('250 v_sm_sm :', params_250[0], '\pm', errors_250[0] )
    #print('250 v_sm_ctZ :', params_250[1], '\pm', errors_250[1] )
    #print('250 v_ctW_sm :', params_250[2], '\pm', errors_250[2] )
    #print('250 v_ctW_ctZ :', params_250[3], '\pm', errors_250[3] )
    #print('250 v_ctW_ctW :', params_250[4], '\pm', errors_250[4] )
    #print('250 v_ctZ_ctZ :', params_250[5], '\pm', errors_250[5] )
    ################################################################################

    #Uncertainty calculation 
    #345GEV:
    sigma_345 = 0.544
    sigma_err_345 = 0.018
    factor_345 = sigma_err_345/sigma_345

    #346GEV:
    sigma_346 = 0.5235
    sigma_err_346 = 0.015
    factor_346 = sigma_err_346/sigma_346


    #347GEV:
    sigma_347 = 0.518
    sigma_err_347 = 0.02
    factor_347 = sigma_err_347/sigma_347


    #348GEV:
    sigma_348 = 0.53
    sigma_err_348 = 0.02
    factor_348 = sigma_err_348/sigma_348

    #349GEV:
    sigma_349 = 0.535
    sigma_err_349 = 0.02
    factor_349 = sigma_err_349/sigma_349



    
    #PLOTTING FOR CTW ONLY
    
    print('RUN ', run_W[25], 'with Cross section:',  cross_W[25])
    
    t = np.linspace(-3,0.7,1000)
    plt.plot(coefficient_strength_W, cross_W, 'o', color='deeppink')
    plt.errorbar(coefficient_strength_W,cross_W, yerr=error_W ,xerr=None, fmt='o', color='deeppink')
    plt.plot(t, two_dimensional_parabole_ctW(t, v_sm_W, v_ctW, v_ctW_quad), label='Polynomial Fitting Function of Second Degree')
    plt.hlines(cross_W[25] , -10,10, 'crimson', linestyle='solid', label='SM Value')
    plt.hlines(cross_W[25] + (cross_W[25] * (factor_349/2)), -10,10, 'pink', linestyle='solid', label='Accuracy')
    plt.hlines(cross_W[25] - (cross_W[25] * (factor_349/2)) , -10,10, 'pink', linestyle='solid')
    plt.fill_between(t, (cross_W[25] - (cross_W[25] * (factor_349/2))) ,(cross_W[25] + (cross_W[25] * (factor_349/2))) ,facecolor='pink')
    plt.grid()
    plt.xlim(-1.95,0.25)
    plt.ylim(0,0.5)
    plt.xlabel('ctW')
    plt.ylabel('$\sigma$ / pb')
    plt.legend(loc='best')
    plt.title('$e^+e^-$-> tt~'  '   '   '$\sqrt{s} = 349$GeV' '   ' 'dim6top_LO_UFO' )
    plt.savefig('349_ctW_cross_section.pdf')
    plt.show()


    ################################################################################


    #PLOTTING FOR CtZ ONLY
    #print('RUN ', run_Z[5], 'with Cross section:',  cross_Z[5])
#
    #t = np.linspace(-1,3,1000)
    #plt.plot(coefficient_strength_Z, cross_Z, 'o', color='deeppink')
    #plt.errorbar(coefficient_strength_Z,cross_Z, yerr=error_Z ,xerr=None, fmt='o', color='deeppink')
    #plt.plot(t, two_dimensional_parabole_ctZ(t, v_sm_Z, v_ctZ, v_ctZ_quad), label='Polynomial Fitting Function of Second Degree')
    #plt.hlines(cross_Z[5] , -10,10, 'crimson', linestyle='solid', label='SM Value')
    #plt.hlines(cross_Z[5] - (cross_Z[5] * (factor_349/2)) , -10,10, 'pink', linestyle='solid', label='Accuracy')
    #plt.hlines(cross_Z[5] + (cross_Z[5] * (factor_349/2)) , -10,10, 'pink', linestyle='solid')
    #plt.fill_between(t,(cross_Z[5] - (cross_Z[5] * (factor_349 /2))), (cross_Z[5] + (cross_Z[5] * (factor_349 /2))) ,facecolor='pink')
    #plt.grid()
    #plt.xlabel('ctZ')
    #plt.xlim(-0.25,1.85)
    #plt.ylim(0.065,0.45)
    #plt.ylabel('$\sigma$ / pb')
    #plt.legend(loc='best')
    #plt.title('$e^+e^-$-> tt~'  '   '   '$\sqrt{s} = 349$GeV' '   ' 'dim6top_LO_UFO' )
    #plt.savefig('349_ctZ_cross_section.pdf')
    #plt.show()

if __name__ == "__main__":
   main()