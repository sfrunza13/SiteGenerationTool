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
                file = open(inputFile, "r", encoding="utf8")
            else:
                file = open(inputFolder + "/" + inputFile, "r", encoding="utf8")
            
            
            Lines = file.readlines()
        
            for i, line in enumerate(Lines):
                #my logic doesnt work. I need it to be blank line delimiter.
                if i == 0:
                    titleStorage = line
                elif i == 1:
                    if line != "\n":
                        titleQuestionMark = False
                        newLine = "<p>" + titleStorage 
                        paragraphs.append(newLine)
                        newLine =  line 
                        paragraphs.append(newLine)
                elif i == 2:
                    if line != "\n":
                        titleQuestionMark = False
                        newLine = "<p>" + titleStorage + "</p>"
                        paragraphs.append(newLine)
                        newLine = "<p>" + line 
                        paragraphs.append(newLine)
                elif i == 3:
                    if titleQuestionMark == True:
                        newLine = "<h1>" + titleStorage + "</h1>"
                        paragraphs.append(newLine)
                        newLine = "<p>" + line 
                        paragraphs.append(newLine)
                else:
                    if line == "\n":
                        newLine = "</p>" + "<p>"
                        paragraphs.append(newLine)
                    else:
                        newLine = line
                        paragraphs.append(newLine)
            #print (paragraphs)
            
            outputName = inputFile[:inputFile.find('.txt')] + '.html'
            
            print("new name:", outputName)
            
            self.writeOut(outputName, paragraphs, titleQuestionMark)
        except OSError as e:
            print("Error: " + str(e))
        
    def writeOut(self, output, paragraphs, title):    
        try:
            if self.output:
                fileOut = open(self.output + "/" + output, "w", encoding="utf-8")   
            
            tempTemp = SSJ.template
            
            if title:
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
        
        print(onlyfiles)
        
        temp = SSJ.template
        
        SSJ.template = SSJ.template.replace("Filename", "Index Page")
        
        for file in onlyfiles:
            if file.endswith(".txt"):
                self.parseFile(file, inputFolder)
                outputName = (file[:file.find('.txt')] + '.html')
                hrefName = outputName.replace(" ", "%20")
                pos = SSJ.template.find(SSJ.token) + len(SSJ.token)
                SSJ.template = SSJ.template[:pos] + "<a href={}>{}</a><br>".format(hrefName, outputName) + SSJ.template[pos:]
                
                
        try:
            if self.output:
                fileOut = open(self.output + "/" + "Index.html", "w", encoding="utf-8")
                fileOut.write(SSJ.template)
        except OSError as err:
            print("Error: " + str(err)) 
            
        SSJ.template = temp