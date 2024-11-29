1. import pdf into affinity publisher
2. Make sure all text boxes are converted into plaintext format
3. Use the Text Flow function to link all text boxes into 1 continuous script.
	1. This has to from bottom to top due to how text flow works
4. When all boxes are linked, Hold shift and arrow down to select all relevant text
	1. if step 4 is stopped because 2 boxes aren't linked, just keep going from the next section onwards. This is still a lot better than selecting each text box individually
5. Paste contents into text editor (I use notepad++)
6. use regex commands to weed out poor formatting
	1. The most important regex command is to form a newline after every period.


```regex
Find: \.
Replace: \.\R

Find: e\.\Rg\.(.*)
Replace: e\.g\.\1

Find: \t(\S)
Replace: \1

Find: \.(\S)
Replace:\. \1
```
