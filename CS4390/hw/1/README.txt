# Execution
The program requires the following actions
- input the command into the terminal

    python simple-web-server.py

- in a browser search bar, a query may be made using the following line

    http://localhost:8080/{filename}

The program should return the contents of the file that is found to exist. If the file
does note exist, then it returns a 404 error message. There is a provided text file
that may be used to demonstrate the program's is capabilities.

    http://localhost:8080/something.txt

# Constraints
- The file is relative to the program - that is, no additional paths would mean that
  the file is assumed to be in the same folder as the program. 
- The program is not well equipped for special characters in its name. Filename should only
  be in lowercase followed by a '.' and the file extension.
