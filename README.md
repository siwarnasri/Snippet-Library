# Automating Snippets with Python

  Speeding up our snippets workflow with Python: Every good development workflow involves some kind of management of code snippets, where we are constantly storing and retrieving snippets of code to solve a wide range of tasks in our programming routine.

  It is important to note that, this is one approach, there are so many ways to save snippets and retrieve them, in the end, we should experiment with as many tools as we can to see what works for us.

The Steps to Save Snippets From the Clipboard:

 > 1. Specify a variable with the path for the snippets folder.

 > 2. Write the code to get the contents of our clipboard.
 
 > 3. Write the code to save the content in a pre-specified snippets file (to be determined when calling the script) with the right format.

 > 4. Save the final Python script in a folder.

 > 5. Write an alias to call that script from anywhere in the terminal.

Now, let’s go through each step one by one.

## 1. Specify a variable with the path to the snippets folder:

```python
global_snippets_folder = "snippets_path" 
```
Change "snippets_path" to your specific case.

## 2. Write the code to get the contents of your clipboard:
```python
import clipboard
clipboard.paste()
clipboard_content = clipboard.paste()
```
Here, we are using the clipboard package to get the contents of your clipboard.

## 3. Write the code to save the content in a pre-specified snippets file (to be determined when calling the script) with the right format:
```python
snippets_name = input("Snippet name: ")
snippet_dest_path = global_snippets_folder + snippets_name + ".code-snippets"

with open(snippet_dest_path, "w+") as snippet_file:
    snippet_file.write("{\n")
    snippet_file.write(f"\"{snippets_name}\":")
    snippet_file.write("{\n")
    snippet_file.write('    "scope": "python",\n')
    snippet_file.write('    "prefix": "' + snippets_name + '",\n')
    snippet_file.write('    "body": [\n')
    try:
        for line in clipboard_content.splitlines("\n"):
            snippet_file.write('        "' + line + '",\n')
    except TypeError:
        for line in clipboard_content.split("\n"):
            snippet_file.write('        "' + line + '",\n')
    snippet_file.write('    ],\n')
    snippet_file.write('    "description": "' + snippets_name + '"\n')
    snippet_file.write("}\n")
    snippet_file.write("}\n")
```
  This is code saves the content of the clipboard to the specified folder with a name given by the user when calling the script and with the required format needed to call the snippet.
    
## 4. Save the final Python script in a folder:

Here you can save it in wherever folder you want inside your computer.

## 5. Write an alias to call that script from anywhere in the terminal:

To do this all you have to do (assuming you are working in a Linux machine or in Windows but with WSL: Linux), is open your .bashrc file and write:
```python
alias save_snippet_from_clipboard="snippets_path"
```
Then, save the modified file and run source .bashrc to update your terminal.

Now you can start saving snippets directly from your clipboard!
