from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>Network Protocols and Applications</title>
</head>
<body>

    <h2>List of Network Protocols and Their Applications</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>S.No</th>
            <th>Protocol</th>
            <th>Application</th>
        </tr>

        <tr>
            <td>1</td>
            <td>HTTP</td>
            <td>Used to access web pages.</td>
        </tr>

        <tr>
            <td>2</td>
            <td>HTTPS</td>
            <td>Used for secure web browsing and online banking.</td>
        </tr>

        <tr>
            <td>3</td>
            <td>FTP</td>
            <td>Used to transfer files between computers.</td>
        </tr>

        <tr>
            <td>4</td>
            <td>SMTP</td>
            <td>Used to send emails.</td>
        </tr>

        <tr>
            <td>5</td>
            <td>POP3</td>
            <td>Used to download and receive emails.</td>
        </tr>

        <tr>
            <td>6</td>
            <td>IMAP</td>
            <td>Used to access and synchronize emails.</td>
        </tr>

        <tr>
            <td>7</td>
            <td>DNS</td>
            <td>Converts domain names into IP addresses.</td>
        </tr>

        <tr>
            <td>8</td>
            <td>TCP</td>
            <td>Provides reliable data transmission.</td>
        </tr>

        <tr>
            <td>9</td>
            <td>UDP</td>
            <td>Supports fast data transmission, such as online gaming.</td>
        </tr>

        <tr>
            <td>10</td>
            <td>SSH</td>
            <td>Provides secure remote computer access.</td>
        </tr>
    </table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()