import numpy as np 
import sys

def main():
    if(sys.argv<7):
        print('STOP, more arguments needed')

    coefficient = sys.argv[1]
    center = str(sys.argv[2])
    stepspace = float(sys.argv[3])
    total_steps = int(sys.argv[4])
    scriptname = sys.argv[5]
    outputdir = sys.argv[6]

    document = open(scriptname, 'w+')

    document.write('import model dim6top_LO_UFO \n') 
    document.write('generate e+ e- > t t~ FCNC=0 dim6<=1\n')
    document.write('output' + outputdir + '/OtB/' + center + '/'+ coefficient+'\n')

    desired_try = np.arange(-20,20,1)

    sin_squared_weinberg = 0.2312215

    #ctZ = - np.sqrt(sin_squared_weinberg) * desired_ctB
    desired_ctB = np.array([ 0, 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19, 20, -1, -2 ,-3 ,-4 ,-5 ,-6 ,-7, -8, -9, -10, -11, -12, -13 , -14,
           -15, -16, -17,-18,-19,-20])
    
    for i in range(total_steps): 
        ctZ = -np.sqrt(sin_squared_weinberg) * desired_ctB[i]
        document.write('launch' + outputdir + '/OtB/' + center + '/'+ coefficient+'\n')
        document.write('\n') 
        document.write('set nevents ' + str(2000)+ '\n')
        document.write('set ebeam1 '+ center+ '\n')
        document.write('set ebeam2 '+ center+ '\n')
        document.write('set '+coefficient+ ' '+ str(ctZ) + '\n')
        document.write('0' + '\n')


    document.write('launch' + outputdir + '/OtB/'+ center + '/'+ coefficient+' -i \n')
    document.write('print_results --path='+ outputdir + '/OtB/'+ center + '/'+ coefficient + '/cross_sections.txt --format=short\n')
    document.write('exit')
    document.close()
    print('Am I doing anything') 
    
if __name__ == "__main__":
    main()
