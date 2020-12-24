import glob
filepath = "Path to files includiding wildcard.txt"
files = glob.glob(filepath)
output = open("ACLs.txt","a+")
for ios in files:
  data = open(ios,'r')
  for line in data:
    if "hostname " in line:
      output.write(line)
    elif "access-list " in line:
      output.write(line)
  data.close()
output.close()
