from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<HTML>
    <HEAD>
        </TITLE>
    </HEAD>
    <BODY bgcolor="red">
        <table border="1" align="center" bgcolor="yellow" cellpadding="10"
            <tr><th>S.no.</th><th>Name of the layers</th>
                <th>Name of the protocols</th>
            </tr>
            <tr>
                <td>1</td><td>Application layer</td><td>HTML,FTP,Telnet,RDP,DNS,SSH,SMTP,SNTP</td>
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