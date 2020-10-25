import camelot

for page in range(40):
    try:
        tables = camelot.read_pdf('store_list.pdf', pages=str(page), flavor='stream', columns=['40, 60, 267, 505']*2, split_text=True)
        print(tables[0].parsing_report)
        print(len(tables))
        for tab in tables:
            print(tab.shape)
        tables.export('foo.csv', f='csv') 
    except IndexError as e:
        print('Error: a mulformed page found: ', e)

