def read_matrix(filename):
    
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        
       dataMatrix = [[int(column) for column in row.split()] for row in input_file]

       return dataMatrix

def sum_RowMatrix(matrix):

    matrix = read_matrix(matrix)

    for row in matrix:
      rowSum =  list(map(sum, matrix))

    return rowSum

def sum_ColumnMatrix(matrix):
    matrix = read_matrix(matrix)

    col_sums = []
    
    for column in range(len(matrix[0])):
        sum_column = 0
        for row in range(len(matrix)):
            sum_column += matrix[row][column]
        col_sums.append(sum_column)
    
    return col_sums

def sortMatrix(matrix):
    readMatrix = read_matrix(matrix)
    col_sums = sum_ColumnMatrix(matrix)
    row_sums = sum_RowMatrix(matrix)

    rowDict = {}
    colDict = {}

    for value in range(0,len(readMatrix)):
        rowDict[sum(readMatrix[value])] = readMatrix[value]

    colDict = zip(sorted(col_sums, readMatrix))#figure out how to dict col sums with matrix and sort row and column

    return colDict


#print(sum_RowMatrix("testmatrix0.txt"))    
#print(sum_ColumnMatrix("testmatrix0.txt"))
print(sortMatrix("testmatrix0.txt"))

    
