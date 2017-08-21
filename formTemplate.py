# HTML jinja2 template for the requesting a ride website

__author__ = 'Olivia Salomon, Karina Lin, and Teresa Li'

#write your HTML template in the variable below
formTemplate = """
<html>
<head>
                
                
<title>Submit a Transportation Request</title>
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
                
<!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
                
    <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
                
    <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
                
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>jQuery UI Datepicker - Default functionality</title>
    <link rel="stylesheet" href="http://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel="stylesheet" href="/resources/demos/style.css">
    
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
                <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
                <script>
                $( function() {
                    $( "#datepicker" ).datepicker();
                } );
                </script>
                
                
</head>
                

<body>
                
    <h1> Transportation Request Form </h1>
    <div id='requests'></div>
                
    <form id="requestForm">
        <label>Name:</label>
             <input type="text" id="studentName">
             <br>
             
        <label>B Number:</label>
             <input type="text" id="bNum">
            <br>
                
        <label>Event Date: </label>
             <input type="text" id="datepicker">
             <br>
        
        <label>Pickup Time: </label>
             <select id="time">
             	<option value="8:20am">8:20am</option>
             	<option value="9:40am">9:40am</option>
             	<option value="11:00am">11:00am</option>
             	<option value="12:20pm">12:20pm</option>
             	<option value="1:20pm">1:20pm</option>
             	<option value="2:40pm">2:40pm</option>
             	<option value="4:00pm">4:00pm</option>
             </select>
             <br>
                
        <label>Pickup Location: </label>
             <input type="text" id="pickUp">
             <br>
                
        <label>Dropoff Location: </label>
             <input type="text" id="dropOff">
             <br>
             <br>
             
        <input type="submit">
    </form>
    
    </body>
    </html>
    
    """