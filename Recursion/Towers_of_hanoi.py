def towerOfHanoi(noOfDisks,startPeg = 1, endPeg = 3):
    if noOfDisks:
        towerOfHanoi(noOfDisks - 1, startPeg, 6 - startPeg - endPeg)
        print("move disk %d from peg %d to peg %d" % (noOfDisks, startPeg, endPeg))
        towerOfHanoi(noOfDisks - 1, 6 - startPeg - endPeg, endPeg)

towerOfHanoi(noOfDisks=4)