===========================
WORD COUNTER – PYTHON TASK
===========================

📌 DESCRIPTION:
--------------
This program allows a user to input the name of a text file (.txt), reads the file, and counts the total number of words in it.

The user can provide any file they want (not a hardcoded file). The file must exist in the same directory or a full path must be given.

👤 USER INPUT:
--------------
- The program will ask:
  Enter the name of the text file:
- Example input:
  sample.txt

📂 REQUIREMENTS:
----------------
- Python installed (version 3.x recommended)
- A .txt file with some text content
- File should be in the same folder OR give full file path (e.g., C:\files\sample.txt)

🛠️ HOW IT WORKS:
-----------------
1. Takes file name from user using `input()`.
2. Opens the file in read mode using:
     with open(filename, 'r') as file
3. Reads the content using:
     content = file.read()
4. Splits the content into words using:
     words = content.split()
5. Counts the total number of words using:
     len(words)
6. Displays the result to the user.
7. If the file is not found, it shows an error message using `FileNotFoundError`.

✅ SAMPLE OUTPUT:
-----------------
Enter the name of the text file: sample.txt  
Total number of words in the file: 41

❌ ERROR HANDLING:
------------------
If the file does not exist:
> Error: File not found. Please check the filename.

📘 TIPS:
--------
- Make sure file extension is `.txt`.
- Avoid using double extensions like `file.txt.txt`.
- Don't leave the file name input blank.

🎓 AUTHOR:
     Attia Malik
