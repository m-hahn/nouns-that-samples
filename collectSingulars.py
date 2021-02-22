with open("plurals.tsv", "r") as inFile:
   data = inFile.read().strip().split("\n")[1:]
with open("plurals.tsv", "w") as outFile:
 print("\t".join(["Singular", "Plural"]), file=outFile)
 for line in data:
   assert line.endswith("s")
   singulars = [line[:-1]]
   if line.endswith("es"):
     singulars.append(line[:-2])
   if line.endswith("ies"):
     singulars.append(line[:3]+"y")
   for s in singulars:
      print("\t".join([line, s]), file=outFile)
   
