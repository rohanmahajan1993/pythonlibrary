This is a tool that is used to show the basic functionality of rsync.
We use grpc for the client and the server.
Most of the algorithms can be found here: https://rsync.samba.org/tech_report/.

One key original optimization is we use timestamps. The server always sends the time
to the client in it response. Therefore a clients timestamp is always equal to the timestamp of the server from  its previous request.
The server uses timestamps to not process files that have the older or the same timestamps
as the timestamp received from the client.
