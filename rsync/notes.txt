One 
This is a tool that is used to show the basic functionality of rsync.
We use grpc for the client and the server.
We don't want to be sending the entire directory everytime.
Therefore, we make some optimizations. One optimization is we send the timestamp from the client.
The server only sends back files that have changed since then. One problematic situation is that we don't know about deleted files. 

We have seperate directories for rsync client and rsync server to make it easier for testing, as in real life scenearioes they would be running in different locations
