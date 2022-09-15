import sys, getopt

def main(argv):
    inputFile = ''
    outputFile = 'defaultOut.txt'
    outputFolder = "./dist"
    name = "SSJ SSG the Super Saiyan Site Tool"
    version = "0.0.1"
    token = "<body>"
    template = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Filename</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  
</body>
</html>"""
    pos = template.find(token) + len(token)    


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
            inputFile = arg
        elif opt in ("-o", "--output"):
            outputFile = arg
            
    paragraphs = []        
            
    try:
        file = open(inputFile, "r")
        
        Lines = file.readlines()
    
        for line in Lines:
            if line != "\n":
                newLine = "<p>" + line + "</p>"

                paragraphs.append(newLine)
        
    except OSError as e:
        print("Error: " + str(e))
        
        
    try:
        fileOut = open(outputFile, "w")
        
        for paragraph in reversed(paragraphs):
            template = template[:pos] + paragraph + template[pos:]
                               
    except OSError as err:
        print("Error: " + str(err))
    

    print ("Input file: ", inputFile)
    print ("Output file: ", outputFile)
    print (template)
    print (paragraphs)
    
    
if __name__ == "__main__":
   main(sys.argv[1:])