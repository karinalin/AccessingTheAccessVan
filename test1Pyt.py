#!/usr/local/bin/python2.7
 
import sys
 
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda


 
if __name__ == '__main__':
    print 'Content-type: text/html\n'
 
    form_data = cgi.FieldStorage()
    if 'username' in form_data:
        tmpl = cgi_utils_sda.file_contents('name-response.html')
        username = form_data.getfirst('username')
        page = tmpl.format(name=username)
        print page
    else:
        print '''Error: This script, {script}, should be given form data
that includes a "username" input'''.format(script=sys.argv[0])
    
