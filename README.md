# sentence-permutations

Given an input CSV with two columns of options and an input sentence, return all possible sentence permutations as CSV.

## Usage Instructions:

1) Download this Github repository to your computer. The easiest way to do this is by clicking `Download Zip` on Github. Unzip the file, and move it to wherever you want the folder to live.
   1) ![](/Users/cdole/Desktop/Screen Shot 2022-11-14 at 9.45.35 AM.png)
2) Open your Terminal, and navigate to the unzipped `sentence-permutations` folder you downloaded. You should be at the same level as the `sentence_permutations.py` file.
3) Replace the `input.csv` file included in the folder with a file of the same format/name, but different contents. 
   1) The words listed in column "A" will replace the `AAA` sentence input. The words in column "B" will replace the `BBB` sentence input. 
   2) You can also directly edit the `input.csv` file, but it makes no difference whether you replace it or edit as long as the name is correct.
4) Back at the terminal, run the `sentence_permutations.py` Python file with your desired sentence as the only input. Your sentence must be contained in double quotes, and have both `AAA` and `BBB` present as variables for the script to replace with words from the CSV.
   1) EX: `python sentence_permutations.py --sentence "The XXX lives in YYY."`
   2) EX: `python sentence_permutations.py --sentence "In YYY, he placed XXX on the table.` <-- "XXX" and "YYY" can be present in any order within the sentence
5) The script will complete, and create/replace a file called `output.csv` within the `sentence-permutations` folder with sentence permutations. The script will show you this output at your terminal as well:
   1) ```shell
      Creating permutations for sentence: "The AAA lives in BBB."
      [0.00027s] Success! Sentence permutations have been generated to: 'output.csv'
      ```

