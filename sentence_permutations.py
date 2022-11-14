"""Given an input CSV with two columns of options and an input sentence, return all possible sentence permutations."""
import argparse
import csv
import time


def sentence_permutations(sentence: str):
    output_list = []

    with open("input.csv", mode="r") as input_csv:
        reader = csv.reader(input_csv, delimiter=",")

        column_1 = set()
        column_2 = set()

        for row in reader:
            if row[0]:
                column_1.add(row[0])
            if row[1]:
                column_2.add(row[1])

        sentences = [sentence.replace("AAA", i).replace("BBB", j) for i in list(column_1) for j in list(column_2)]

        with open("output.csv", "w", newline='') as output_file:
            wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
            wr.writerow(sentences)


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
