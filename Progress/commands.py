import numpy as np 
import sys 


def main():
    if (sys.argv<7):
        print('STOP, you missed a parameter')


    #working with the sys.arv command, the number of runs, coefficient, space between 
    #steps as well as the output needs to be specified 

    coefficient = sys.argv[1]
    center = str(sys.argv[2])
    stepspace = float(sys.argv[3])
    positivesteps = int(sys.argv[4])
    negativesteps = int(sys.argv[5])
    scriptname = sys.argv[6]
    outputdir = sys.argv[7]

    #following are the steps, that could go one by one in the terminal 
    #initialize model as well as process 
    #set number of events
    #set coefficient to zero 
    #start simulation

    document = open(scriptname,'w+')
    #w+ means, you open the file for writing or create a new one if this one does not 
    #exist, the + opens the possibility to edit

    document.write('import model dim6top_LO_UFO \n') 
    document.write('generate e+ e- > t t~ FCNC=0 dim6<=1\n')
    document.write('output' + outputdir + '/' + center + '/'+ coefficient+'\n')

    #start with setting the desired coefficient to zero

    c = 0


    document.write('launch'+outputdir + '/'+ center + '/'+ coefficient +'\n')
    document.write('3'+ '\n') 
    document.write('\n')

    #this line is different from last years, did not disable exroot also pressed 
    #enter sooner. Check if this is right, if this does not work

    document.write('set nevents ' + str(2000)+ '\n')
    document.write('set ebeam1 '+ center + '\n')
    document.write('set ebeam2 '+ center + '\n')
    document.write('set '+ coefficient + ' ' + str(c) + '\n')
    document.write('0' + '\n')


    #now start with the number of runs in the positive direction 
    for i in range(positivesteps):
        c = c + stepspace
        document.write('launch' + outputdir + '/'+ center + '/'+ coefficient+'\n')
        document.write('\n') 
        document.write('set nevents ' + str(2000)+ '\n')
        document.write('set ebeam1 '+ center+ '\n')
        document.write('set ebeam2 '+ center+ '\n')
        document.write('set '+coefficient+ ' '+ str(c) + '\n')
        document.write('0' + '\n')

    c = 0

    #now do the same for the negative space
    for i in range(negativesteps):
        c = c - stepspace
        document.write('launch' + outputdir + '/' + center + '/'+ coefficient+'\n')
        document.write('\n') 
        document.write('set nevents ' + str(2000)+ '\n')
        document.write('set ebeam1 '+ center + '\n')
        document.write('set ebeam2 '+ center + '\n')
        document.write('set '+coefficient+ ' '+ str(c) + '\n')
        document.write('0' + '\n')

    #save all information in .txt file for plotting later 

    document.write('launch' + outputdir + '/'+ center + '/'+ coefficient+' -i \n')
    document.write('print_results --path='+ outputdir + '/'+ center + '/'+ coefficient + '/cross_sections.txt --format=short\n')
    document.write('exit')
    document.close()

if __name__ == "__main__":
    main()






