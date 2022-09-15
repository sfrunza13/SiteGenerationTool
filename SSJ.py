from os import listdir
from os.path import isfile, join

class SSJ:
    defaultOutput = 'defaultOut.html'
    defaultOutputFolder = "./dist"
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
    
    def __init__(self,input,output=None):
        self.input = input
        if output is None:
            self.output = 'defaultOut.html'
        else:
            self.output = output
        
    
    def parseFile(self, inputFile, inputFolder = None):   
        paragraphs = []     
        try:
            if inputFolder is None:
                file = open(inputFile, "r")
            else:
                file = open(inputFolder + "/" + inputFile, "r")
            
            Lines = file.readlines()
        
            for line in Lines:
                if line != "\n":
                    newLine = "<p>" + line + "</p>"

                    paragraphs.append(newLine)
            print (paragraphs)
            
            outputName = inputFile[:inputFile.find('.txt')] + '.html'
            
            print("new name:", outputName)
            
            self.writeOut(outputName, self.defaultOutputFolder, paragraphs, self.pos)
        except OSError as e:
            print("Error: " + str(e))
        
    def writeOut(self, output, defaultOutputFolder, paragraphs, pos):    
        try:
            fileOut = open(defaultOutputFolder + "/" + output, "w")
            
            tempTemp = SSJ.template
            
            for paragraph in reversed(paragraphs):
                SSJ.template = SSJ.template[:pos] + paragraph + SSJ.template[pos:]
                
            fileOut.write(SSJ.template)
            SSJ.template = tempTemp
                                
        except OSError as err:
            print("Error: " + str(err)) 
        
        
    def parseDir(self, input):
        inputFolder = input
        
        print(self.defaultOutputFolder)
        #retrieve every txt file in dir omitting other dirs
        onlyfiles = [f for f in listdir(input) if isfile(join(input, f))]
        
        for file in onlyfiles:
            if file.endswith(".txt"):
                self.parseFile(file, inputFolder)
