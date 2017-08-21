import requests
import json
import jinja2, webbrowser, os
import formTemplate
import web
reload(formTemplate)
from formTemplate import formTemplate

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

def main():
    """Prompts the user for a search term (possibly containing multiple words
       separated by spaces), and then looks up this search term in the 
       Google Books web API. If the response status code is not 200, does
       nothing. Otherwise does the following:
     
           1. Writes a file named book4<search term>.json that contains the
              formatted JSON for the response, where <search term> is replaced
              by the actual search term, without spaces. E.g. for the search
              term 'joy luck', writes the file book4joyluck.json. Use the
              helper function writeJSONforExploration for this purpose. 

           2. Extracts relevant information from the response and uses
              this to fill the template gBooksTemplate to create the 
              HTML file named book4<search term>.html that is structured
              as specified in the PS10 problem description. E.g. for the search
              term 'joy luck', generates the file book4joyluck.html. 
              Use the helper functions fillHTMLTemplate and 
              writeHTMLFile in this step. 

           3. Opens a browser on the file generated in step 2. 
              Use the helper function openBrowserForHTMLFile in this step.
    """
    titleSearchString = raw_input("Please enter a search term: ")
    

        resultsDict = extractBookInfo(stringResponseFromAPI)
        
        resultsDict["bookList"] = sortByPublishedDate(resultsDict["bookList"])

        parametersForTemplate = {'query1': titleSearchString,
                                 'bookList': resultsDict}  
                                       
        htmlText = fillHTMLTemplate(gBooksTemplate, parametersForTemplate)
        filename = 'books4'+ "".join(titleSearchString.split()) + ".html"
        writeHTMLFile(htmlText, filename)
        openBrowserForHTMLFile(filename)
     
           
#invocation of the main function
if __name__ == '__main__':
    main()
