import numpy as np 
import sys 

def main():
    if sys.argv(< 6):
        print('error')

    coefficient = sys.argv[1]
    coef_value = sy.argv[2]
    steps = sys.argv[3]
    scriptname = sys.argv[4]
    outputdir = sys.argv[5]

    document = open(scriptname, 'w+')
    document.write('import model dim6top_LO_UFO \n') 
    document.write('generate e+ e- > t t~ FCNC=0 dim6<=1\n')
    document.write('output' + outputdir + '/'+ coefficient+ '/' + coef_value +'\n')

    desired_cms = np.arange(335,376,1)
    desired_cms = np.asarray(desired_cms)

    
    for i in range(len(desired_cms)):
        document.write('launch' + outputdir + '/'+ coefficient+ '/' + coef_value +'\n')
        document.write('\n') 
        document.write('set nevents ' + str(2000)+ '\n')
        document.write('set ebeam1 '+ desired_cms[i] + '\n')
        document.write('set ebeam2 '+ desired_cms[i] + '\n')
        document.write('set '+coefficient+ ' '+ str(coef_value) + '\n')
        document.write('0' + '\n')

    document.write('launch' + outputdir + '/'+ coefficient+ '/' + coef_value +' -i \n')
    document.write('print_results --path='+ outputdir + '/'+ coefficient+ '/' + coef_value + '/cross_sections.txt --format=short\n')
    document.write('exit')
    document.close()

if __name__ == "__main__":
main()
