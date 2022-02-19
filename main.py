import pprintpp
from tabulate import tabulate
from utils import  columns, data, rows



pprintpp.pprint(data,)

def getCell(items ,dx, ou, pe):
    cells = []

    return cells

def mycell(rows):
    cells = []
    for cell in rows:
        print(cell[-1])
        cells.append(cell[-1])
    return cells
cells = mycell(data['rows'])

cells = getCell(data['metaData']['items'], data['metaData']['dimensions']['dx'], data['metaData']['dimensions']['ou'], data['metaData']['dimensions']['pe'])

my_row = rows(data['metaData']['items'], data['metaData']['dimensions']['ou'])

cols = columns(data['metaData']['items'], data['metaData']['dimensions']['pe'])

# table = zip())


def createTable(my_row, cols):
    data_cell = []
    for d in data['rows']:
        for cell in d:
            data_cell.append(d[-1])

    table = zip(my_row, data_cell)
    print(tabulate(my_row, headers=cols,  tablefmt="fancy_grid"))
    
createTable(my_row, cols)