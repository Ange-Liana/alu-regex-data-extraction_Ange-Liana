From the instructions given by the assignment, two data types (emails and credit cards) are mandatory to work on, and for the other ones, I chose to work on regex patterns for phone numbers and hashtags. So this program implements regex patterns that extract such data types from the raw data inputs provided. These regex patterns are also meant to reject the inputs that are not valid or unsafe according to the instructions.

Therefore, the program reads the file raw-text.txt, which contains raw inputs and unordered data, as well as emails, credit cards, hashtags, and phone numbers. The program also has the main.py, which is a Python code file that contains the regex patterns that verify authorized or valid data inputs of emails, phone numbers, credit card numbers and hashtags. 
As a result, the extractions made by the regex patterns are automatically put in a .json file of sample outputs (sample-output.json) 

To run the program, 
Move to the src/ directory, which has the Python file main.py, which contains the source code
Run python3 main.py  in the terminal
And finally, the extracted results are saved in the output file, which is in the output directory (output/)

