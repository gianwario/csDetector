from csDetector import CsDetector
import os
import argparse
from typing import Sequence
# this is the adapter class. we can use it to call the adaptee from different sources of input
# by inheriting csDetector, we override the method with bad specicied interface with a better
# one that will call the superclass method after parsing the given input


class CsDetectorAdapter(CsDetector):
    def __init__(self):
        super().__init__()

    def executeTool(self, gitRepository, gitPAT, startingDate="null", sentiFolder="./senti", outputFolder="./out"):

        if(startingDate == "null"):
            # in this branch we execute the tool normally because no date was provided
            return super().executeTool(
                ["-p", gitPAT, "-r", gitRepository, "-s", sentiFolder, "-o", outputFolder])

        else:
            # if a date is specified we have to execute with one more parameter
            return super().executeTool(['-p', gitPAT, '-r', gitRepository,
                                        '-s', sentiFolder, '-o', outFolder, '-sd', startingDate])


if __name__ == "__main__":

    tool = CsDetectorAdapter()
    formattedResult, result = tool.executeTool("https://github.com/tensorflow/ranking",
                                               "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")
    print(result)
    print(formattedResult)
