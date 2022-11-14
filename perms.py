"""Given an input CSV with two columns of options and an input sentence, return all possible sentence permutations."""
import argparse
import csv
import time


def sentence_permutations(sentence: str):
    with open("input.csv", mode="r") as input_csv:
        reader = csv.reader(input_csv, delimiter=",")

        column_1 = []
        column_2 = []

        for row in reader:
            a, b = row[0], row[1]
            if a and a not in column_1:
                column_1.append(a)
            if b and b not in column_2:
                column_2.append(b)

        sentences = [sentence.replace("AAA", i).replace("BBB", j) for i in column_1 for j in column_2]

        with open("output.txt", "w") as f:
            for sentence in sentences:
                f.write(sentence + "\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sentence", type=str, required=True)
    args = parser.parse_args()

    print(f"Creating permutations for sentence: \"{args.sentence}\"")
    if "AAA" not in args.sentence or "BBB" not in args.sentence:
        raise Exception("Input sentence must include both 'AAA' and 'BBB'.")

    start = time.time()
    sentence_permutations(args.sentence)
    stop = time.time()

    print(f"[{round(stop - start, 5)}s] Success! Sentence permutations have been generated to: 'output.csv'")
