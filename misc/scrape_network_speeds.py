#!/usr/bin/python

# WARNING! This script is very hackey - it worked for me, but YMMV

import requests
import urllib3
import bs4
from bs4 import BeautifulSoup
from pprint import pprint
import itertools
import os
import matplotlib.pyplot as plt

download_dists = False

r =  requests.get('http://ipnetwork.bgtmo.ip.att.net/pws/network_delay.html')
page = BeautifulSoup(r.text, "lxml")

table = page.find("td", {"width": "69%"}).find("table")

locations = ["Atlanta, GA", "Austin, TX", "Cambridge, MA", "Chicago, IL", "Cleveland, OH", "Dallas, TX", "Denver, CO", "Detroit, MI", "Houston, TX", "Indianapolis, IN", "Kansas City, MO", "Los Angeles, CA", "Madison, WI", "Nashville, TN", "New Orleans, LA", "New York, NY", "Orlando, FL", "Philadelphia, PA", "Phoenix, AZ", "San Antonio, TX", "San Diego, CA", "San Francisco, CA", "St. Louis, MO", "Seattle, WA", "Washington DC"]

location_pairs = itertools.combinations(locations, 2)

if download_dists:
    app_id = os.getenv('WOLFRAM_APP_ID')
    for pair in location_pairs:
        loc1 = urllib3.util.parse_url(pair[0])
        loc2 = urllib3.util.parse_url(pair[1])
        r = requests.get('http://api.wolframalpha.com/v1/result?appid={}&i=distance+between+{}+and+{}'.format(app_id, loc1, loc2))
        dist = float(r.text.replace(" miles", ""))
        print("(\"{}\", \"{}\"): {},".format(pair[0], pair[1], dist))

dist_pairs = {
    ("Atlanta, GA", "Austin, TX"): 817.0,
    ("Atlanta, GA", "Cambridge, MA"): 936.0,
    ("Atlanta, GA", "Chicago, IL"): 585.0,
    ("Atlanta, GA", "Cleveland, OH"): 553.0,
    ("Atlanta, GA", "Dallas, TX"): 717.0,
    ("Atlanta, GA", "Denver, CO"): 1205.0,
    ("Atlanta, GA", "Detroit, MI"): 599.0,
    ("Atlanta, GA", "Houston, TX"): 701.0,
    ("Atlanta, GA", "Indianapolis, IN"): 426.0,
    ("Atlanta, GA", "Kansas City, MO"): 674.0,
    ("Atlanta, GA", "Los Angeles, CA"): 1945.0,
    ("Atlanta, GA", "Madison, WI"): 698.0,
    ("Atlanta, GA", "Nashville, TN"): 213.0,
    ("Atlanta, GA", "New Orleans, LA"): 422.0,
    ("Atlanta, GA", "New York, NY"): 748.0,
    ("Atlanta, GA", "Orlando, FL"): 403.0,
    ("Atlanta, GA", "Philadelphia, PA"): 670.0,
    ("Atlanta, GA", "Phoenix, AZ"): 1590.0,
    ("Atlanta, GA", "San Antonio, TX"): 881.0,
    ("Atlanta, GA", "San Diego, CA"): 1887.0,
    ("Atlanta, GA", "San Francisco, CA"): 2139.0,
    ("Atlanta, GA", "St. Louis, MO"): 467.0,
    ("Atlanta, GA", "Seattle, WA"): 2181.0,
    ("Atlanta, GA", "Washington DC"): 544.0,
    ("Austin, TX", "Cambridge, MA"): 1693.0,
    ("Austin, TX", "Chicago, IL"): 973.0,
    ("Austin, TX", "Cleveland, OH"): 1182.0,
    ("Austin, TX", "Dallas, TX"): 181.0,
    ("Austin, TX", "Denver, CO"): 766.0,
    ("Austin, TX", "Detroit, MI"): 1163.0,
    ("Austin, TX", "Houston, TX"): 147.0,
    ("Austin, TX", "Indianapolis, IN"): 926.0,
    ("Austin, TX", "Kansas City, MO"): 635.0,
    ("Austin, TX", "Los Angeles, CA"): 1235.0,
    ("Austin, TX", "Madison, WI"): 994.0,
    ("Austin, TX", "Nashville, TN"): 752.0,
    ("Austin, TX", "New Orleans, LA"): 461.0,
    ("Austin, TX", "New York, NY"): 1514.0,
    ("Austin, TX", "Orlando, FL"): 994.0,
    ("Austin, TX", "Philadelphia, PA"): 1439.0,
    ("Austin, TX", "Phoenix, AZ"): 871.0,
    ("Austin, TX", "San Antonio, TX"): 73.7,
    ("Austin, TX", "San Diego, CA"): 1155.0,
    ("Austin, TX", "San Francisco, CA"): 1501.0,
    ("Austin, TX", "St. Louis, MO"): 716.0,
    ("Austin, TX", "Seattle, WA"): 1769.0,
    ("Austin, TX", "Washington DC"): 1318.0,
    ("Cambridge, MA", "Chicago, IL"): 851.0,
    ("Cambridge, MA", "Cleveland, OH"): 547.0,
    ("Cambridge, MA", "Dallas, TX"): 1547.0,
    ("Cambridge, MA", "Denver, CO"): 1761.0,
    ("Cambridge, MA", "Detroit, MI"): 613.0,
    ("Cambridge, MA", "Houston, TX"): 1603.0,
    ("Cambridge, MA", "Indianapolis, IN"): 804.0,
    ("Cambridge, MA", "Kansas City, MO"): 1246.0,
    ("Cambridge, MA", "Los Angeles, CA"): 2603.0,
    ("Cambridge, MA", "Madison, WI"): 931.0,
    ("Cambridge, MA", "Nashville, TN"): 941.0,
    ("Cambridge, MA", "New Orleans, LA"): 1356.0,
    ("Cambridge, MA", "New York, NY"): 188.0,
    ("Cambridge, MA", "Orlando, FL"): 1114.0,
    ("Cambridge, MA", "Philadelphia, PA"): 265.0,
    ("Cambridge, MA", "Phoenix, AZ"): 2294.0,
    ("Cambridge, MA", "San Antonio, TX"): 1764.0,
    ("Cambridge, MA", "San Diego, CA"): 2576.0,
    ("Cambridge, MA", "San Francisco, CA"): 2698.0,
    ("Cambridge, MA", "St. Louis, MO"): 1037.0,
    ("Cambridge, MA", "Seattle, WA"): 2490.0,
    ("Cambridge, MA", "Washington DC"): 392.0,
    ("Chicago, IL", "Cleveland, OH"): 312.0,
    ("Chicago, IL", "Dallas, TX"): 799.0,
    ("Chicago, IL", "Denver, CO"): 912.0,
    ("Chicago, IL", "Detroit, MI"): 238.0,
    ("Chicago, IL", "Houston, TX"): 936.0,
    ("Chicago, IL", "Indianapolis, IN"): 163.0,
    ("Chicago, IL", "Kansas City, MO"): 407.0,
    ("Chicago, IL", "Los Angeles, CA"): 1752.0,
    ("Chicago, IL", "Madison, WI"): 124.0,
    ("Chicago, IL", "Nashville, TN"): 394.0,
    ("Chicago, IL", "New Orleans, LA"): 829.0,
    ("Chicago, IL", "New York, NY"): 720.0,
    ("Chicago, IL", "Orlando, FL"): 983.0,
    ("Chicago, IL", "Philadelphia, PA"): 668.0,
    ("Chicago, IL", "Phoenix, AZ"): 1447.0,
    ("Chicago, IL", "San Antonio, TX"): 1046.0,
    ("Chicago, IL", "San Diego, CA"): 1727.0,
    ("Chicago, IL", "San Francisco, CA"): 1858.0,
    ("Chicago, IL", "St. Louis, MO"): 259.0,
    ("Chicago, IL", "Seattle, WA"): 1737.0,
    ("Chicago, IL", "Washington DC"): 598.0,
    ("Cleveland, OH", "Dallas, TX"): 1023.0,
    ("Cleveland, OH", "Denver, CO"): 1222.0,
    ("Cleveland, OH", "Detroit, MI"): 96.3,
    ("Cleveland, OH", "Houston, TX"): 1113.0,
    ("Cleveland, OH", "Indianapolis, IN"): 262.0,
    ("Cleveland, OH", "Kansas City, MO"): 698.0,
    ("Cleveland, OH", "Los Angeles, CA"): 2060.0,
    ("Cleveland, OH", "Madison, WI"): 412.0,
    ("Cleveland, OH", "Nashville, TN"): 458.0,
    ("Cleveland, OH", "New Orleans, LA"): 921.0,
    ("Cleveland, OH", "New York, NY"): 408.0,
    ("Cleveland, OH", "Orlando, FL"): 893.0,
    ("Cleveland, OH", "Philadelphia, PA"): 358.0,
    ("Cleveland, OH", "Phoenix, AZ"): 1746.0,
    ("Cleveland, OH", "San Antonio, TX"): 1256.0,
    ("Cleveland, OH", "San Diego, CA"): 2030.0,
    ("Cleveland, OH", "San Francisco, CA"): 2170.0,
    ("Cleveland, OH", "St. Louis, MO"): 494.0,
    ("Cleveland, OH", "Seattle, WA"): 2028.0,
    ("Cleveland, OH", "Washington DC"): 304.0,
    ("Dallas, TX", "Denver, CO"): 660.0,
    ("Dallas, TX", "Detroit, MI"): 997.0,
    ("Dallas, TX", "Houston, TX"): 223.0,
    ("Dallas, TX", "Indianapolis, IN"): 763.0,
    ("Dallas, TX", "Kansas City, MO"): 454.0,
    ("Dallas, TX", "Los Angeles, CA"): 1252.0,
    ("Dallas, TX", "Madison, WI"): 814.0,
    ("Dallas, TX", "Nashville, TN"): 615.0,
    ("Dallas, TX", "New Orleans, LA"): 441.0,
    ("Dallas, TX", "New York, NY"): 1373.0,
    ("Dallas, TX", "Orlando, FL"): 961.0,
    ("Dallas, TX", "Philadelphia, PA"): 1300.0,
    ("Dallas, TX", "Phoenix, AZ"): 889.0,
    ("Dallas, TX", "San Antonio, TX"): 251.0,
    ("Dallas, TX", "San Diego, CA"): 1184.0,
    ("Dallas, TX", "San Francisco, CA"): 1486.0,
    ("Dallas, TX", "St. Louis, MO"): 544.0,
    ("Dallas, TX", "Seattle, WA"): 1683.0,
    ("Dallas, TX", "Washington DC"): 1183.0,
    ("Denver, CO", "Detroit, MI"): 1148.0,
    ("Denver, CO", "Houston, TX"): 874.0,
    ("Denver, CO", "Indianapolis, IN"): 996.0,
    ("Denver, CO", "Kansas City, MO"): 554.0,
    ("Denver, CO", "Los Angeles, CA"): 846.0,
    ("Denver, CO", "Madison, WI"): 833.0,
    ("Denver, CO", "Nashville, TN"): 1017.0,
    ("Denver, CO", "New Orleans, LA"): 1077.0,
    ("Denver, CO", "New York, NY"): 1629.0,
    ("Denver, CO", "Orlando, FL"): 1546.0,
    ("Denver, CO", "Philadelphia, PA"): 1574.0,
    ("Denver, CO", "Phoenix, AZ"): 585.0,
    ("Denver, CO", "San Antonio, TX"): 796.0,
    ("Denver, CO", "San Diego, CA"): 834.0,
    ("Denver, CO", "San Francisco, CA"): 957.0,
    ("Denver, CO", "St. Louis, MO"): 789.0,
    ("Denver, CO", "Seattle, WA"): 1026.0,
    ("Denver, CO", "Washington DC"): 1488.0,
    ("Detroit, MI", "Houston, TX"): 1105.0,
    ("Detroit, MI", "Indianapolis, IN"): 240.0,
    ("Detroit, MI", "Kansas City, MO"): 641.0,
    ("Detroit, MI", "Los Angeles, CA"): 1990.0,
    ("Detroit, MI", "Madison, WI"): 326.0,
    ("Detroit, MI", "Nashville, TN"): 472.0,
    ("Detroit, MI", "New Orleans, LA"): 939.0,
    ("Detroit, MI", "New York, NY"): 490.0,
    ("Detroit, MI", "Orlando, FL"): 960.0,
    ("Detroit, MI", "Philadelphia, PA"): 446.0,
    ("Detroit, MI", "Phoenix, AZ"): 1685.0,
    ("Detroit, MI", "San Antonio, TX"): 1237.0,
    ("Detroit, MI", "San Diego, CA"): 1965.0,
    ("Detroit, MI", "San Francisco, CA"): 2090.0,
    ("Detroit, MI", "St. Louis, MO"): 456.0,
    ("Detroit, MI", "Seattle, WA"): 1935.0,
    ("Detroit, MI", "Washington DC"): 400.0,
    ("Houston, TX", "Indianapolis, IN"): 866.0,
    ("Houston, TX", "Kansas City, MO"): 646.0,
    ("Houston, TX", "Los Angeles, CA"): 1381.0,
    ("Houston, TX", "Madison, WI"): 975.0,
    ("Houston, TX", "Nashville, TN"): 665.0,
    ("Houston, TX", "New Orleans, LA"): 320.0,
    ("Houston, TX", "New York, NY"): 1421.0,
    ("Houston, TX", "Orlando, FL"): 851.0,
    ("Houston, TX", "Philadelphia, PA"): 1344.0,
    ("Houston, TX", "Phoenix, AZ"): 1017.0,
    ("Houston, TX", "San Antonio, TX"): 190.0,
    ("Houston, TX", "San Diego, CA"): 1301.0,
    ("Houston, TX", "San Francisco, CA"): 1644.0,
    ("Houston, TX", "St. Louis, MO"): 677.0,
    ("Houston, TX", "Seattle, WA"): 1890.0,
    ("Houston, TX", "Washington DC"): 1221.0,
    ("Indianapolis, IN", "Kansas City, MO"): 452.0,
    ("Indianapolis, IN", "Los Angeles, CA"): 1820.0,
    ("Indianapolis, IN", "Madison, WI"): 285.0,
    ("Indianapolis, IN", "Nashville, TN"): 251.0,
    ("Indianapolis, IN", "New Orleans, LA"): 711.0,
    ("Indianapolis, IN", "New York, NY"): 648.0,
    ("Indianapolis, IN", "Orlando, FL"): 821.0,
    ("Indianapolis, IN", "Philadelphia, PA"): 585.0,
    ("Indianapolis, IN", "Phoenix, AZ"): 1497.0,
    ("Indianapolis, IN", "San Antonio, TX"): 999.0,
    ("Indianapolis, IN", "San Diego, CA"): 1785.0,
    ("Indianapolis, IN", "San Francisco, CA"): 1951.0,
    ("Indianapolis, IN", "St. Louis, MO"): 234.0,
    ("Indianapolis, IN", "Seattle, WA"): 1873.0,
    ("Indianapolis, IN", "Washington DC"): 492.0,
    ("Kansas City, MO", "Los Angeles, CA"): 1368.0,
    ("Kansas City, MO", "Madison, WI"): 382.0,
    ("Kansas City, MO", "Nashville, TN"): 472.0,
    ("Kansas City, MO", "New Orleans, LA"): 681.0,
    ("Kansas City, MO", "New York, NY"): 1098.0,
    ("Kansas City, MO", "Orlando, FL"): 1050.0,
    ("Kansas City, MO", "Philadelphia, PA"): 1037.0,
    ("Kansas City, MO", "Phoenix, AZ"): 1048.0,
    ("Kansas City, MO", "San Antonio, TX"): 703.0,
    ("Kansas City, MO", "San Diego, CA"): 1334.0,
    ("Kansas City, MO", "San Francisco, CA"): 1510.0,
    ("Kansas City, MO", "St. Louis, MO"): 235.0,
    ("Kansas City, MO", "Seattle, WA"): 1507.0,
    ("Kansas City, MO", "Washington DC"): 942.0,
    ("Los Angeles, CA", "Madison, WI"): 1679.0,
    ("Los Angeles, CA", "Nashville, TN"): 1790.0,
    ("Los Angeles, CA", "New Orleans, LA"): 1682.0,
    ("Los Angeles, CA", "New York, NY"): 2464.0,
    ("Los Angeles, CA", "Orlando, FL"): 2212.0,
    ("Los Angeles, CA", "Philadelphia, PA"): 2405.0,
    ("Los Angeles, CA", "Phoenix, AZ"): 365.0,
    ("Los Angeles, CA", "San Antonio, TX"): 1210.0,
    ("Los Angeles, CA", "San Diego, CA"): 111.0,
    ("Los Angeles, CA", "San Francisco, CA"): 343.0,
    ("Los Angeles, CA", "St. Louis, MO"): 1597.0,
    ("Los Angeles, CA", "Seattle, WA"): 961.0,
    ("Los Angeles, CA", "Washington DC"): 2310.0,
    ("Madison, WI", "Nashville, TN"): 498.0,
    ("Madison, WI", "New Orleans, LA"): 905.0,
    ("Madison, WI", "New York, NY"): 815.0,
    ("Madison, WI", "Orlando, FL"): 1099.0,
    ("Madison, WI", "Philadelphia, PA"): 770.0,
    ("Madison, WI", "Phoenix, AZ"): 1389.0,
    ("Madison, WI", "San Antonio, TX"): 1066.0,
    ("Madison, WI", "San Diego, CA"): 1660.0,
    ("Madison, WI", "San Francisco, CA"): 1767.0,
    ("Madison, WI", "St. Louis, MO"): 310.0,
    ("Madison, WI", "Seattle, WA"): 1620.0,
    ("Madison, WI", "Washington DC"): 709.0,
    ("Nashville, TN", "New Orleans, LA"): 467.0,
    ("Nashville, TN", "New York, NY"): 762.0,
    ("Nashville, TN", "Orlando, FL"): 614.0,
    ("Nashville, TN", "Philadelphia, PA"): 687.0,
    ("Nashville, TN", "Phoenix, AZ"): 1445.0,
    ("Nashville, TN", "San Antonio, TX"): 823.0,
    ("Nashville, TN", "San Diego, CA"): 1740.0,
    ("Nashville, TN", "San Francisco, CA"): 1964.0,
    ("Nashville, TN", "St. Louis, MO"): 255.0,
    ("Nashville, TN", "Seattle, WA"): 1975.0,
    ("Nashville, TN", "Washington DC"): 568.0,
    ("New Orleans, LA", "New York, NY"): 1168.0,
    ("New Orleans, LA", "Orlando, FL"): 534.0,
    ("New Orleans, LA", "Philadelphia, PA"): 1091.0,
    ("New Orleans, LA", "Phoenix, AZ"): 1317.0,
    ("New Orleans, LA", "San Antonio, TX"): 510.0,
    ("New Orleans, LA", "San Diego, CA"): 1608.0,
    ("New Orleans, LA", "San Francisco, CA"): 1927.0,
    ("New Orleans, LA", "St. Louis, MO"): 597.0,
    ("New Orleans, LA", "Seattle, WA"): 2102.0,
    ("New Orleans, LA", "Washington DC"): 964.0,
    ("New York, NY", "Orlando, FL"): 937.0,
    ("New York, NY", "Philadelphia, PA"): 77.6,
    ("New York, NY", "Phoenix, AZ"): 2145.0,
    ("New York, NY", "San Antonio, TX"): 1585.0,
    ("New York, NY", "San Diego, CA"): 2432.0,
    ("New York, NY", "San Francisco, CA"): 2577.0,
    ("New York, NY", "St. Louis, MO"): 879.0,
    ("New York, NY", "Seattle, WA"): 2414.0,
    ("New York, NY", "Washington DC"): 204.0,
    ("Orlando, FL", "Philadelphia, PA"): 867.0,
    ("Orlando, FL", "Phoenix, AZ"): 1847.0,
    ("Orlando, FL", "San Antonio, TX"): 1039.0,
    ("Orlando, FL", "San Diego, CA"): 2139.0,
    ("Orlando, FL", "San Francisco, CA"): 2443.0,
    ("Orlando, FL", "St. Louis, MO"): 863.0,
    ("Orlando, FL", "Seattle, WA"): 2551.0,
    ("Orlando, FL", "Washington DC"): 757.0,
    ("Philadelphia, PA", "Phoenix, AZ"): 2081.0,
    ("Philadelphia, PA", "San Antonio, TX"): 1510.0,
    ("Philadelphia, PA", "San Diego, CA"): 2370.0,
    ("Philadelphia, PA", "San Francisco, CA"): 2525.0,
    ("Philadelphia, PA", "St. Louis, MO"): 814.0,
    ("Philadelphia, PA", "Seattle, WA"): 2380.0,
    ("Philadelphia, PA", "Washington DC"): 126.0,
    ("Phoenix, AZ", "San Antonio, TX"): 848.0,
    ("Phoenix, AZ", "San Diego, CA"): 297.0,
    ("Phoenix, AZ", "San Francisco, CA"): 649.0,
    ("Phoenix, AZ", "St. Louis, MO"): 1268.0,
    ("Phoenix, AZ", "Seattle, WA"): 1107.0,
    ("Phoenix, AZ", "Washington DC"): 1981.0,
    ("San Antonio, TX", "San Diego, CA"): 1125.0,
    ("San Antonio, TX", "San Francisco, CA"): 1487.0,
    ("San Antonio, TX", "St. Louis, MO"): 789.0,
    ("San Antonio, TX", "Seattle, WA"): 1784.0,
    ("San Antonio, TX", "Washington DC"): 1388.0,
    ("San Diego, CA", "San Francisco, CA"): 454.0,
    ("San Diego, CA", "St. Louis, MO"): 1558.0,
    ("San Diego, CA", "Seattle, WA"): 1057.0,
    ("San Diego, CA", "Washington DC"): 2272.0,
    ("San Francisco, CA", "St. Louis, MO"): 1744.0,
    ("San Francisco, CA", "Seattle, WA"): 681.0,
    ("San Francisco, CA", "Washington DC"): 2443.0,
    ("St. Louis, MO", "Seattle, WA"): 1723.0,
    ("St. Louis, MO", "Washington DC"): 714.0,
    ("Seattle, WA", "Washington DC"): 2329.0,
}

output = []

for row in table:
    if type(row) == bs4.element.Tag:
        row_out = []
        for col in row:
            if type(col) == bs4.element.Tag:
                if col.text.isspace():
                    row_out.append(None)
                else:
                    try:
                        row_out.append(int(col.text))
                    except ValueError:
                        pass
        output.append(row_out)

# pprint(output, width=1000)

final_output = []

for rownum, row in enumerate(output):
    row_out = []
    for colnum, col in enumerate(row):
        if col is not None:
            dist = dist_pairs[(locations[colnum],locations[rownum])] * 1.609344 # in km
            row_out.append(round(dist*2/col,1))
        else:
            row_out.append(None)
    final_output.append(row_out)

# pprint(final_output, width=1000)

def output_table(arr, headers):
    print("||{}".format("|".join(headers)))
    print("---|"*(len(headers)+1))
    for rownum, row in enumerate(arr):
        print("{}|{}".format(headers[rownum], "|".join(map(str, row))).replace("None", ""))

output_table(final_output, locations)

output_flat = [z for z in [y for x in final_output for y in x] if z is not None]

plt.hist(output_flat, bins='auto')
plt.title("network speeds in km/ms")
plt.show()

output_flat_lightspeed = [(z*1000*1000/207110506) for z in output_flat]

plt.hist(output_flat_lightspeed, bins='auto')
plt.title("network speeds in percent speed of light in fiber")
plt.show()
