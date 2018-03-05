from PartSearchReader import PartSearchReader

headers = ['Digi-Key Part Number', 'Quantity Available', 'Manufacturer Part Number', 'Manufacturer Standard Lead Time', 'Price Break', 'Unit Price', 'Ship Date Estimate']

searcher = PartSearchReader(headers)
url_list = searcher.readUrlListFromCSV('test_list_of_urls.csv')
tempDic = dict()
list_of_parts = []
for url in url_list:
    soup = searcher.getSoupData(url)
    d = {}
    tempDic = searcher.scrapeTopHalf(soup, d)
    tempDic = searcher.scrapeRightCol(soup, tempDic)

    if searcher.available(tempDic) == False:
        part_id = searcher.scrapePartId(soup, tempDic)
        shipDateHtml = searcher.makeLeadTimeRequest(tempDic, part_id)
        tempDic = searcher.getShipDate(tempDic, shipDateHtml)

    list_of_parts.append(searcher.filterHeaders(tempDic))


searcher.writeToCSV('DKPartScrapev6.csv', list_of_parts)
