from os import listdir
from os.path import isfile, join
import re

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
    
    
    def __init__(self,input=None,output=None):
        self.input = input
        if input is None:
            print("No input has been specified. This can not work.")
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
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                        newLine =  line 
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                elif i == 2:
                    if line != "\n":
                        titleQuestionMark = False
                        newLine = "<p>" + titleStorage + "</p>"
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                        newLine = "<p>" + line 
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                elif i == 3:
                    if titleQuestionMark == True:
                        newLine = "<h1>" + titleStorage + "</h1>"
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                        newLine = "<p>" + line 
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                else:
                    if line == "\n":
                        newLine = "</p>" + "<p>"
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
                    else:
                        newLine = line
                        paragraphs.append(SSJ.convertMarkdown(newLine) if inputFile.endswith(".md") else newLine)
            #print (paragraphs)
            
            outputName = inputFile[:inputFile.find('.')] + '.html'
            
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
            if file.endswith(".txt") or file.endswith(".md"):
                self.parseFile(file, inputFolder)
                outputName = (file[:file.find('.')] + '.html')
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

    def markdownSearch(regex, indChars, tag, line):
        newLine = line
        match = re.search(regex,newLine)
        while match != None:
            if (tag == "hr"):
                newLine = newLine[:match.span()[0]] + "<" + tag + ">"+ newLine[match.span()[1]:]
            else:
                newLine = newLine[:match.span()[0]] + "<" + tag + ">" + newLine[match.span()[0]+indChars:match.span()[1]-indChars] + "</"+ tag +">" + newLine[match.span()[1]:]
            match = re.search(regex,newLine)
        return newLine

    def convertMarkdown(line):
        newLine = line
        #bold
        newLine = SSJ.markdownSearch("\*\*[^*]+\*\*", 2, "b", newLine)
        newLine = SSJ.markdownSearch("__[^*]+__", 2, "b", newLine)
        #italics
        newLine = SSJ.markdownSearch("\*[^*]+\*", 1, "i", newLine)
        newLine = SSJ.markdownSearch("_[^*]+_", 1, "i", newLine)
        #code
        newLine = SSJ.markdownSearch("\`\`\`[^*]+\`\`\`", 3, "code", newLine)
        newLine = SSJ.markdownSearch("\`[^*]+\`", 1, "code", newLine)
        #hr
        newLine = SSJ.markdownSearch("\-\-\-[^*]", 3, "hr", newLine)

        return newLine