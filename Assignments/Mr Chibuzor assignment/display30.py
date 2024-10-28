counter = 0
graph = ""
graphdata = ""

while counter <= 4:
    entree= int(input("Enter between 1 to 30: "))

    if entree >= 0 and entree <= 30:
      graph = entree * "*"
      graph = graph + "\n"
      graphdata = graphdata + graph
    
    else:
      print("Value out of range.")

    counter = counter + 1		
    print("Graph data\n")
    print(graphdata + "\n")