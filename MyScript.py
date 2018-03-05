from PartSearchReader import PartSearchReader

headers = ['Digi-Key Part Number', 'Quantity Available', 'Manufacturer Part Number', 'Manufacturer Standard Lead Time', 'Price Break', 'Unit Price', 'Ship Date Estimate']

searcher = PartSearchReader(headers)
url_list = searcher.readUrlListFromCSV('test_list_of_urls.csv')
tempDic = {}
list_of_parts = []
for url in url_list:
    soup = searcher.getSoupData(url)
    tempDic = searcher.scrapeTopHalf(soup, tempDic)
    tempDic = searcher.scrapeRightCol(soup, tempDic)

    if searcher.available(tempDic) == False:
        part_id = searcher.scrapePartId(soup, tempDic)
        tempDic = searcher.makeLeadTimeRequest(tempDic, part_id)

    list_of_parts.append(searcher.filterHeaders(tempDic))


searcher.writeToCSV('DKPartScrapev6.csv', list_of_parts)
