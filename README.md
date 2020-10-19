# Get-the-files-name-in-a-specific-directory
You can extract the names of the files in current directory (path) or another custom directory in your OS.
## Description
You can extract just the files in a specific directory or path, for example, if you have files inside another directory the script can not walk into it, so it behaves like a  `-maxdepth 2`  parameter if you are familiar with the Linux command.
So, It's shown only the files exists in that current directory without entering to other folders to look for all files into it.

After extracting all the files names in the target directory, the script stores them in a file called directory.txt with the number of files out there.

You can either pass an absolute path or relative path.

The script comes with more comments to describe almost every line of code on it.
## Requirement
* `Python 3.8`, It can work with other versions especially any version of python 3.x (I've not tested it on version 2.x).
* `OS` Module, It comes preinstalled with python package.
## Usage
You have all the right to use the script for personal use.
## Running the Script
![Run the script](http://4.bp.blogspot.com/-RDLUbaB-h4Q/X4W19HuIGcI/AAAAAAAAChg/0Mi5TPYDlp0ri4Ihgi5OGjGx7ot38a2eQCK4BGAYYCw/s1600/get%2Bfiles.png)
#### Open the output file `directory.txt`
* [Output file](./directory.txt)
