import argparse
import os
import sys

from evaluation.word_analogy import WordAnalogyW2VFormat

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]),
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=__doc__)
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        required=True,
                        help='Directory or Path to word2vec format file.')
    parser.add_argument('-a',
                        '--analogy-path',
                        type=str,
                        required=True,
                        help='Path to questions words file with analogy words.')
    parser.add_argument('-a',
                        '--simlex-path',
                        type=str,
                        help='Path to SimLex File file with words pairs.')

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    analogy_path = os.path.abspath(args.analogy_path)

    w2v_val = WordAnalogyW2VFormat(input_path, analogy_path)
    w2v_val.evaluate_word_analogy()
    if args.simlex_path:
        path_to_simlex = os.path.abspath(args.simlex_path)
        w2v_val.evaluate_word_pairs(path_to_simlex)
