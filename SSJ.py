from os import listdir
from os.path import isfile, join

class SSJ:
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
    
    
    def __init__(self,input,output=None):
        self.input = input
        if output is None:
            self.output = SSJ.defaultOutputFolder
        else:
            self.output = output
        
    
    def parseFile(self, inputFile, inputFolder = None):   
        paragraphs = []   
        titleStorage = ""  
        titleQuestionMark = True
        try:
            if inputFolder is None:
                file = open(inputFile, "r")
            else:
                file = open(inputFolder + "/" + inputFile, "r")
            
            Lines = file.readlines()
        
            for i, line in enumerate(Lines):
                
                if i == 0:
                    titleStorage = line
                elif i == 1 or i == 2:
                    if line != "\n":
                        titleQuestionMark = False
                        newLine = "<p>" + titleStorage + "</p>"
                        paragraphs.append(newLine)
                        newLine = "<p>" + line + "</p>"
                        paragraphs.append(newLine)
                elif i == 3:
                    if titleQuestionMark == True:
                        newLine = "<h1>" + titleStorage + "</h1>"
                        paragraphs.append(newLine)
                        newLine = "<p>" + line + "</p>"
                        paragraphs.append(newLine)
                else:
                    if line != "\n":
                        newLine = "<p>" + line + "</p>"
                        paragraphs.append(newLine)
            print (paragraphs)
            
            outputName = inputFile[:inputFile.find('.txt')] + '.html'
            
            print("new name:", outputName)
            
            self.writeOut(outputName, self.defaultOutputFolder, paragraphs, titleQuestionMark)
        except OSError as e:
            print("Error: " + str(e))
        
    def writeOut(self, output, defaultOutputFolder, paragraphs, title):    
        try:
            if self.output:
                fileOut = open(self.output + "/" + output, "w")   
            
            tempTemp = SSJ.template
            
            if title:
                # SSJ.template = SSJ.template[:SSJ.template.find("<title>") + len("<title>")] + paragraphs[0] + SSJ.template[SSJ.template.find("<title>") + len("<title>"):]
                SSJ.template = SSJ.template.replace("Filename", paragraphs[0][4:-5])
                
            pos = SSJ.template.find(SSJ.token) + len(SSJ.token)    
                
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
