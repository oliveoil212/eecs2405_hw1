# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061213.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Remove the data whose value of the WDSD (wind speed) column is '-99.000' or '-999.000'.
# filter config
targets = ["C0A880", "C0F9A0", "C0G640","C0R190", "C0X260"]
ignored = ['-99.000','-999.000']
targets_data = {}
for row in data:
   id = row.get('station_id')
   wind_speed = row.get('WDSD')
   if id in targets and wind_speed not in ignored:
      targets_data.setdefault(id, []).append(float(wind_speed))
# print(targets_data)
# analyze
targets.sort()
result =[]
for target in targets:
   target_WDSD_data = targets_data.get(target)
    if target_WDSD_data == None:
      max_range = 'None'
   elif len(target_WDSD_data) < 2:
      max_range = 'None'
   else:
      max_range = str("{:.1f}".format(max(target_WDSD_data) - min(target_WDSD_data)))
#=======================================

# Part. 4
#=======================================
print(result)
#========================================
