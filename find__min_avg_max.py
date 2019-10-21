#find_min_max_python.py
# Open file, read lines, parse each as an integer and append to vals list
import sys
import os
import string
import json
vals = []
if len(sys.argv) == 2:

        if sys.argv[1].endswith(".json"):
            with open(sys.argv[1], 'r') as f:
                    datastore = json.load(f)
                    vals.append(datastore["system_stats"]["memory_percent"])
        elif sys.argv[1].endswith(".txt"):
            with open(sys.argv[1], 'r') as f:
                    for line in f:
                            vals.append(float(line.strip()))
        elif os.path.exists(sys.argv[1]):
            json_files = [pos_json for pos_json in os.listdir(sys.argv[1]) if pos_json.endswith('.json')]
            if len(json_files) != 0:
                for json_file in json_files:
                    with open(os.path.abspath(sys.argv[1]+json_file), 'r') as f:
                        datastore = json.load(f)
                        if datastore["system_stats"]["memory_percent"]:
                            vals.append(datastore["system_stats"]["memory_percent"])
                        else
                            print "system_stats/memory_percent not found in json file named" +sys.argv[1] +json_file
            else :
                print "no json files found in specified folder"
                exit(1)
        else :
            print "unsupported file extension or folder option"
            exit(1)
else:
        print "give exactly one argument which is the planfile path"
        exit(1)

print(vals)     # Just to ensure it worked

# Create an average function (much more verbose than necessary)
def avg(lst):
    n = sum(lst)
    d = len(lst)
    return float(n)/d

# Print output
print("Min: %s" % min(vals))    # Min: 1
print("Max: %s" % max(vals))    # Max: 10
print("Avg: %s" % avg(vals))    # Avg: 5.5