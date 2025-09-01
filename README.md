# EX01 Developing a Simple Webserver
## Date:30-08-2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
'''
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
    <HEAD>
        </TITLE>
    </HEAD>
    <BODY bgcolor="pink">
        <table border="1" align="center" bgcolor="cyan" cellpadding="10"
            <tr><th>S.no.</th><th>Name of the layers</th>
                <th>Name of the protocols</th>
            </tr>
            <tr>
            I   <td>1</td><td>Application layer</td><td>HTML,FTP,Telnet,RDP,DNS,SSH,SMTP,SNTP</td>
            </tr>
            <tr>
                <td>2</td><td>Transport layer</td><td>TCP & UDP</td>
            </tr>
            <tr>
                <td>3</td><td>Network layer</td><td>ICMP,IGMP,IPv6,IPv4,ARP</td>
            </tr>
            <tr>
                <td>4</td><td>Physical layer</td><td>Ethernet,FDDI,Frame Relay,Token Ring</td>
            </tr>
            
        </table>
    </BODY>
</HTML>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
'''

## OUTPUT:
![alt text](<Screenshot 2025-08-30 093859-1.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
