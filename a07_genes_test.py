import sys
from inspect import getframeinfo, stack

from a07_genes_solved import *

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def genomics_test_suite():
    """
    The genomics_test_suite() is designed to test the following:
      is_nucleotide(sequence)
      complement_strand()
      mRNA()
      chunk_amino_acid()
      amino_acid_chunks()
      sequence_gene()
    :return: None
    """

    # The following tests test the is_nucleotide() function
    print("Testing is_nucleotide()")
    unittest(is_nucleotide("CGTAGGCAT") == True)
    unittest(is_nucleotide("CGTAFLCAT") == False)

    # Testing the complement_strand() function
    print("\nTesting complement_strand()")
    unittest(complement_strand("CC") == "GG")
    unittest(complement_strand("CA") == "GT")
    unittest(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    unittest(complement_strand("CGTAFLCAT") == "Sequencing Error")

    # Testing the mRNA() function
    print("\nTesting mRNA()")
    unittest(mRNA("GCATCCGTA") == "GCAUCCGUA")
    unittest(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    unittest(mRNA("AAGCACCG") == "AAGCACCG")

    # Testing chunk_amino_acid()
    print("\nTesting chunk_amino_acid()")
    unittest(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    unittest(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded

    # Testing amino_acid_chunks()
    print("\nTesting amino_acid_chunks()")
    unittest(amino_acid_chunks('AGA') == 'R')
    unittest(amino_acid_chunks('AFA') == '?')

    # Testing sequence_gene()
    print("\nTesting sequence_gene()")
    unittest(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    unittest(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    unittest(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                  # and ignoring the last two "extra" nucleotides,
                                                  # this returns amino acid "V".
    unittest(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                  # taking the complement and then replacing the T nucleotide with U.
                                                  # Grouping into triples, we  get the "ASV" amino acid sequence.


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code
    :return: None
    """
    genomics_test_suite()


if __name__ == "__main__":
    main()          # call to main() function
