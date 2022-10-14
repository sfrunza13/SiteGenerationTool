import sys, getopt, os, shutil
from SSJ import SSJ
from os.path import isdir

def main(argv):   
    name = "SSJ SSG the Super Saiyan Site Tool"
    version = "0.0.1"


    try:
        opts, args = getopt.getopt(argv, "vhi:o:c:", ["version", "help", "input=", "output=", "config="])
    except getopt.GetoptError:
        print ('Error with GetOpt')
        sys.exit(2)

    configExists = 0

    for opt, arg in opts:
        if opt in ("-c", "--config"):
            config = arg
            configExists = 1
            break

    if (configExists == 1):
        if os.path.exists(config) and config.endswith(".json"):
            configOpts = SSJ.parseConfig(SSJ, config)
            if configOpts[0] != '':
                input = configOpts[0]
            if configOpts[1] !='':
                output = configOpts[1]

    if (configExists == 0):
        for opt, arg in opts:
            if opt in ("-v", "--version"):
                print ("Name: " + name, "\nVersion: " + version)  
            if opt in ("-h", "--help"):
                print("This tool is designed to take a plain text file and generate a HTML markup file based upon it.\nPossible options:\n -i or --input to specify an input file\n -o or --output to specify the name of a specific directory you would like to output to (it must be an existing valid directory).\n -v or --version to see the name and version of the tool\n")
            if opt in ("-i", "--input"):
                input = arg
            if opt in ("-o", "--output"):
                output = arg 
    
    if 'output' in locals():
        superSiteJen = SSJ(input, output)
    elif 'input' in locals():
        superSiteJen = SSJ(input)
    else:
        print ('There must be at least a valid .txt, .md, or directory input specified') 
        sys.exit(1)       
    try:    
        shutil.rmtree(superSiteJen.output)
    except OSError as error:
        print(error)
        
    os.mkdir(superSiteJen.output)

    if superSiteJen.input.endswith(".txt") or superSiteJen.input.endswith(".md") :
        superSiteJen.parseFile(input)
    elif isdir(superSiteJen.input):
        superSiteJen.parseDir(input)

    print ("Input option: ", superSiteJen.input)
    print ("Output option: ", superSiteJen.output)
    
if __name__ == "__main__":
   main(sys.argv[1:])
   
