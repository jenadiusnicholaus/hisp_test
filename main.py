import pprintpp
from tabulate import tabulate

data = {
    "headers":
    [{"name": "dx", "column": "Data"},
     {"name": "pe", "column": "Period"},
     {"name": "ou", "column": "Organisation unit"},
     {"name": "value", "column": "Value"}
     ], "metaData": {"items": {"202108": {"name": "August 2021"},
                               "202109": {"name": "September 2021"}, "202110": {"name": "October 2021"}, "202111": {"name": "November 2021"}, "202112": {"name": "December 2021"}, "202201": {"name": "January 2022"}, "sB79w2hiLp8": {"name": "ANC 3 Coverage"}, "jUb8gELQApl": {"name": "Kailahun"}, "TEQlaapDQoK": {"name": "Port Loko"}, "Vth0fbpFcsO": {"name": "Kono"}, "ou": {"name": "Organisation unit"}, "OdiHJayrsKo": {"name": "ANC 2 Coverage"}, "O6uvpzGd5pu": {"name": "Bo"}, "fdc6uOvgoji": {"name": "Bombali"}, "dx": {"name": "Data"}, "pe": {"name": "Period"}, "Uvn6LCg7dVU": {"name": "ANC 1 Coverage"}, "lc3eMKXaEfw": {"name": "Bonthe"}}, "dimensions": {"dx": ["Uvn6LCg7dVU", "OdiHJayrsKo", "sB79w2hiLp8"], "pe": ["202108", "202109", "202110", "202111", "202112", "202201"], "ou": ["O6uvpzGd5pu", "fdc6uOvgoji", "lc3eMKXaEfw", "jUb8gELQApl", "Vth0fbpFcsO", "TEQlaapDQoK"], "co": []}}, "rows": [["Uvn6LCg7dVU", "202108", "O6uvpzGd5pu", "147.1"], ["Uvn6LCg7dVU", "202108", "fdc6uOvgoji", "94.1"], ["Uvn6LCg7dVU", "202108", "lc3eMKXaEfw", "114.4"], ["Uvn6LCg7dVU", "202108", "jUb8gELQApl", "86.2"], ["Uvn6LCg7dVU", "202108", "Vth0fbpFcsO", "51.1"], ["Uvn6LCg7dVU", "202108", "TEQlaapDQoK", "112.4"], ["Uvn6LCg7dVU", "202109", "O6uvpzGd5pu", "169.9"], ["Uvn6LCg7dVU", "202109", "fdc6uOvgoji", "79.2"], ["Uvn6LCg7dVU", "202109", "lc3eMKXaEfw", "118.7"], ["Uvn6LCg7dVU", "202109", "jUb8gELQApl", "79.7"], ["Uvn6LCg7dVU", "202109", "Vth0fbpFcsO", "62.0"], ["Uvn6LCg7dVU", "202109", "TEQlaapDQoK", "105.6"], ["Uvn6LCg7dVU", "202110", "O6uvpzGd5pu", "144.6"], ["Uvn6LCg7dVU", "202110", "fdc6uOvgoji", "79.9"], ["Uvn6LCg7dVU", "202110", "jUb8gELQApl", "73.2"], ["Uvn6LCg7dVU", "202110", "TEQlaapDQoK", "89.7"], ["Uvn6LCg7dVU", "202111", "O6uvpzGd5pu", "193.3"], ["Uvn6LCg7dVU", "202111", "lc3eMKXaEfw", "109.7"], ["Uvn6LCg7dVU", "202111", "jUb8gELQApl", "84.6"], ["Uvn6LCg7dVU", "202111", "TEQlaapDQoK", "104.0"], ["Uvn6LCg7dVU", "202112", "O6uvpzGd5pu", "110.9"], ["Uvn6LCg7dVU", "202112", "fdc6uOvgoji", "81.7"], ["Uvn6LCg7dVU", "202112", "jUb8gELQApl", "74.5"], ["Uvn6LCg7dVU", "202112", "Vth0fbpFcsO", "78.9"], ["Uvn6LCg7dVU", "202201", "O6uvpzGd5pu", "129.6"], ["Uvn6LCg7dVU", "202201", "fdc6uOvgoji", "88.3"], ["Uvn6LCg7dVU", "202201", "lc3eMKXaEfw", "99.5"], ["Uvn6LCg7dVU", "202201", "jUb8gELQApl", "78.9"], ["Uvn6LCg7dVU", "202201", "Vth0fbpFcsO", "50.7"], ["Uvn6LCg7dVU", "202201", "TEQlaapDQoK", "101.3"], ["OdiHJayrsKo", "202108", "O6uvpzGd5pu", "160.7"], ["OdiHJayrsKo", "202108", "fdc6uOvgoji", "78.5"], ["OdiHJayrsKo", "202108", "lc3eMKXaEfw", "115.0"], ["OdiHJayrsKo", "202108", "jUb8gELQApl", "85.8"], ["OdiHJayrsKo", "202108", "Vth0fbpFcsO", "44.0"], ["OdiHJayrsKo", "202108", "TEQlaapDQoK", "90.2"], ["OdiHJayrsKo", "202109", "O6uvpzGd5pu", "150.9"], ["OdiHJayrsKo", "202109", "fdc6uOvgoji", "70.0"], ["OdiHJayrsKo", "202109", "lc3eMKXaEfw", "111.5"], ["OdiHJayrsKo", "202109", "jUb8gELQApl", "76.9"], ["OdiHJayrsKo", "202109", "Vth0fbpFcsO", "57.2"], ["OdiHJayrsKo", "202109", "TEQlaapDQoK", "106.6"], ["OdiHJayrsKo", "202110", "O6uvpzGd5pu", "109.6"], ["OdiHJayrsKo", "202110", "fdc6uOvgoji", "72.5"], ["OdiHJayrsKo", "202110", "jUb8gELQApl", "82.2"], ["OdiHJayrsKo", "202110", "TEQlaapDQoK", "81.8"], ["OdiHJayrsKo", "202111", "O6uvpzGd5pu", "179.4"], ["OdiHJayrsKo", "202111", "lc3eMKXaEfw", "108.7"], ["OdiHJayrsKo", "202111", "jUb8gELQApl", "91.5"], ["OdiHJayrsKo", "202111", "TEQlaapDQoK", "92.4"], ["OdiHJayrsKo", "202112", "O6uvpzGd5pu", "109.8"], ["OdiHJayrsKo", "202112", "fdc6uOvgoji", "79.6"], ["OdiHJayrsKo", "202112", "jUb8gELQApl", "76.4"], ["OdiHJayrsKo", "202112", "Vth0fbpFcsO", "74.7"], ["OdiHJayrsKo", "202201", "O6uvpzGd5pu", "114.3"], ["OdiHJayrsKo", "202201", "fdc6uOvgoji", "75.8"], ["OdiHJayrsKo", "202201", "lc3eMKXaEfw", "83.1"], ["OdiHJayrsKo", "202201", "jUb8gELQApl", "79.4"], ["OdiHJayrsKo", "202201", "Vth0fbpFcsO", "33.0"], ["OdiHJayrsKo", "202201", "TEQlaapDQoK", "71.6"], ["sB79w2hiLp8", "202108", "O6uvpzGd5pu", "86.0"], ["sB79w2hiLp8", "202108", "fdc6uOvgoji", "67.0"], ["sB79w2hiLp8", "202108", "lc3eMKXaEfw", "77.8"], ["sB79w2hiLp8", "202108", "jUb8gELQApl", "71.6"], ["sB79w2hiLp8", "202108", "Vth0fbpFcsO", "35.3"], ["sB79w2hiLp8", "202108", "TEQlaapDQoK", "57.3"], ["sB79w2hiLp8", "202109", "O6uvpzGd5pu", "102.1"], ["sB79w2hiLp8", "202109", "fdc6uOvgoji", "49.0"], ["sB79w2hiLp8", "202109", "lc3eMKXaEfw", "80.2"], ["sB79w2hiLp8", "202109", "jUb8gELQApl", "68.1"], ["sB79w2hiLp8", "202109", "Vth0fbpFcsO", "50.0"], ["sB79w2hiLp8", "202109", "TEQlaapDQoK", "59.7"], ["sB79w2hiLp8", "202110", "O6uvpzGd5pu", "91.6"], ["sB79w2hiLp8", "202110", "fdc6uOvgoji", "56.6"], ["sB79w2hiLp8", "202110", "jUb8gELQApl", "69.8"], ["sB79w2hiLp8", "202110", "TEQlaapDQoK", "52.6"], ["sB79w2hiLp8", "202111", "O6uvpzGd5pu", "206.5"], ["sB79w2hiLp8", "202111", "lc3eMKXaEfw", "92.3"], ["sB79w2hiLp8", "202111", "jUb8gELQApl", "82.4"], ["sB79w2hiLp8", "202111", "TEQlaapDQoK", "57.8"], ["sB79w2hiLp8", "202112", "O6uvpzGd5pu", "79.6"], ["sB79w2hiLp8", "202112", "fdc6uOvgoji", "51.2"], ["sB79w2hiLp8", "202112", "jUb8gELQApl", "64.6"], ["sB79w2hiLp8", "202112", "Vth0fbpFcsO", "47.3"], ["sB79w2hiLp8", "202201", "O6uvpzGd5pu", "73.2"], ["sB79w2hiLp8", "202201", "fdc6uOvgoji", "51.1"], ["sB79w2hiLp8", "202201", "lc3eMKXaEfw", "70.3"], ["sB79w2hiLp8", "202201", "jUb8gELQApl", "62.2"], ["sB79w2hiLp8", "202201", "Vth0fbpFcsO", "19.0"], ["sB79w2hiLp8", "202201", "TEQlaapDQoK", "41.3"]]}
pprintpp.pprint(data,)

def getNestedRow(dx , items ):
    nested_row = []
    for item in items:
        if item in dx:
            # print(item)
            nested_row.append(items[item]['name'])
            
    return nested_row
nested_rows = getNestedRow(data['metaData']['dimensions']['dx'], data['metaData']['items'])  

def getCell(dx, ou, pe):
    cells=[]
   
    return cells

    
    
cells = getCell(data['rows'])

def column(items, period):
    cols = [' ', ' ']
    for item in items:
        if item in period:
            cols.append(items[item]['name'])
            # print(items[item]['name'])
    return cols


def rows(items, ou):
    rows = []
    for item in items:
        if item in ou:
            rows.append([items[item]['name'], "\n".join(nested_rows), ''.join(['data']), ''.join('cells data') ,''.join('cells data'), ''.join('cells data'),''.join('cells data'),''.join('cells data') ])
            # print([items[item]['name']])
    # print(rows)
    return rows



my_row = rows(data['metaData']['items'], data['metaData']['dimensions']['ou'])

cols = column(data['metaData']['items'], data['metaData']['dimensions']['pe'])

# table = zip())


def createTable(my_row, cols):
    data_cell = []
    for d in data['rows']:
        for cell in d:
            data_cell.append(d[-1])

    table = zip(my_row, data_cell)
    print(tabulate(my_row, headers=cols,  tablefmt="fancy_grid"))
    
createTable(my_row, cols)