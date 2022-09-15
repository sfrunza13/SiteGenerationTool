import sys, getopt, os, shutil
from SSJ import SSJ
from os.path import isdir

def main(argv):   
    name = "SSJ SSG the Super Saiyan Site Tool"
    version = "0.0.1"


    try:
        opts, args = getopt.getopt(argv, "vhi:o:", ["version", "help", "input=", "output="])
    except getopt.GetoptError:
        print ('Error with GetOpt')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-v", "--version"):
           print ("Name: " + name, "\nVersion: " + version)  
        elif opt in ("-h", "--help"):
            print("This tool is designed to take a plain text file and generate a HTML markup file based upon it.\nPossible options:\n -i or --input to specify an input file\n -o or --output to specify the name of the output file that will be created\n -v or --version to see the name and version of the tool\n")
        elif opt in ("-i", "--input"):
            input = arg
        elif opt in ("-o", "--output"):
            output = arg 
    
    SiteGen = SSJ(input)
    
    try:
        shutil.rmtree(SiteGen.defaultOutputFolder)
        os.mkdir(SiteGen.defaultOutputFolder)
    except OSError as error:
        print(error)

    if SiteGen.input.endswith(".txt"):
        SiteGen.parseFile(input)
    elif isdir(SiteGen.input):
        SiteGen.parsePath(input)

    print ("Input option: ", SiteGen.input)
    print ("Output option: ", SiteGen.output)
    
if __name__ == "__main__":
   main(sys.argv[1:])
   
