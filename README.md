# sentence-permutations

Given an input CSV with two columns of options and an input sentence, return all possible sentence permutations as CSV.

## Usage Instructions:

1) Download this Github repository to your computer.
   1) The easiest way to do this is by clicking `<> Code`, then `Download Zip` on Github. Unzip the file, and move it to wherever you want the folder to live.
2) Open your Terminal, and navigate to the unzipped `sentence-permutations` folder you downloaded. You should be at the same level as the `perms.py` file.
3) Replace the `input.csv` file included in the folder with a file of the same format/name, but different contents. 
   1) The words listed in column "A" will replace the `AAA` sentence input. The words in column "B" will replace the `BBB` sentence input. 
   2) You can also directly edit the `input.csv` file, but it makes no difference whether you replace it or edit as long as the name is correct.
4) Back at the terminal, run the `perms.py` Python file with your desired sentence as the only input. Your sentence must be contained in double quotes, and have both `AAA` and `BBB` present as variables for the script to replace with words from the CSV.
   1) EX: ```python perms.py --sentence "The AAA lives in BBB."```
   2) EX: ```python perms.py --sentence "In BBB, he placed AAA on the table."```
      1) "AAA" and "BBB" can be present in any order within the sentence
5) The script will complete, and create/replace a file called `output.txt` within the `sentence-permutations` folder with sentence permutations. The script will show you this output at your terminal as well:
   1) ```shell
      Creating permutations for sentence: "The AAA lives in BBB."
      [0.00027s] Success! Sentence permutations have been generated to: 'output.txt'
      ```
