import pprintpp
from tabulate import tabulate
from utils import columns, data, rows

# pprintpp.pprint(data)



my_row = rows(
    data['metaData']['items'],
    data['metaData']['dimensions']['ou']
    )

cols = columns(
    data['metaData']['items'],
    data['metaData']['dimensions']['pe'])

# table = zip())


def createTable(my_row, cols):
    data_cell = []
    for d in data['rows']:
        for cell in d:
            data_cell.append(d[-1])

    table = zip(my_row, data_cell)
    print(tabulate(my_row, headers=cols,  tablefmt="fancy_grid"))
    
createTable(my_row, cols)