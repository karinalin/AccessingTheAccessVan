import requests
import json
import jinja2, webbrowser, os
import resultsTemplate
reload(resultsTemplate)
from resultsTemplate import resultsTemplate

###############################################################################
# Provided Helper Functions

def writeJSONforExploration(jsonData, filename):
    """Write results as JSON to explore them."""
    with open(filename, 'w') as fw:
        json.dump(jsonData, fw, sort_keys= True, indent=2)
        

def fillHTMLTemplate(templateString, paramsDict):
    """Invokes the jinja2 methods to fill in the slots in the template."""
    templateObject = jinja2.Template(templateString)
    htmlContent = templateObject.render(paramsDict)
    return htmlContent


def writeHTMLFile(htmlText, filename):
    """Helper file to write the HTML file from the given text. It uses the
       codecs module, which can deal correctly with UTF8 encoding.
    """
    import codecs
    with codecs.open(filename, 'w', 'utf8') as htmlFile:
        htmlFile.write(htmlText)


def openBrowserForHTMLFile(HTMLfilename):
    '''Open a browser to display the HTML in the file named HTMLfilename'''
    URL = 'file:' + os.getcwd() + '/' + HTMLfilename
    print '\n\n\Opening web page', URL
    webbrowser.open(URL)

def __main__():
        resultsList = []
        
        
        with open("results.txt", "r") as myfile:
            for line in myfile:
                request = myfile.readline().split
                name = request[0]
                bNum = request[1]
                date = request[2]
                time = request[3]
                pickUp = request[4]
                dropOff = request[5]
                
                resultsList.append({"name": name,
                            "bNum": bNum,
                            "date": date,
                            "time": time,
                            "pickUp": pickUp,
                            "dropOff": dropOff})

        parametersForTemplate = {'resultsList': resultsList}  
                                       
        htmlText = fillHTMLTemplate(resultsTemplate, parametersForTemplate)
        filename = 'results' + ".html"
        writeHTMLFile(htmlText, filename)
        openBrowserForHTMLFile(filename)
        

#Uncomment the invocation of the main function below
if __name__ == '__main__':
    main()
