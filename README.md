# WebServerPythonTCP
Client + Server Code


In this assignment, you will develop a simple Web server in Python that is capable of processing only one request. Specifically, your web server will...
1.) Create a connection socket when contacted by a client. (browser)
2.) Receive the HTTP request from this connection.
3.) Parse the request to determine the specific file being requested.
4.) Get the requested file from the file system.
5.) Create an HTTP response message consisting of the requested file preceded by header lines.
6.) Send the response over the TCP connection to the requesting browser.

If a browser requests a file not present in your server, you server should return "404 Not Found" error message.
