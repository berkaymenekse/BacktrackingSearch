import csv
import pandas as pd
import plotly.express as px

# Do not modify the line below.
# Variables
countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay",
             "Peru", "Suriname", "Uruguay", "Venezuela"]

# Do not modify the line below.
# Domains
colors = ["blue", "green", "red", "yellow"]


# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    Map = {}
    with open(path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] not in Map:
                Map[row[0]] = []
                isHeader = 1
            for cell in row:
                if isHeader:
                    isHeader = 0
                    continue
                Map[row[0]].append(cell)

    return Map



def checkValid(path,country,color):

    for neighbor in myGraph[country]:
        if neighbor in path and path[neighbor] == color:
            return False

    return True

#backtrackingSearch(myGraph,colors,{},list(myGraph.keys()),0) the call
def backtrackingSearch(graph, colors, path, keys, index):
    if index == len(keys):
        return path
    else:
        current_country = keys[index]
        for color in colors:
            path[current_country] = color
            if checkValid(path, current_country, color):
                return backtrackingSearch(graph, colors, path, keys, index + 1)
            else:
                del path[current_country]



# Do not modify this method, only call it with an appropriate argument.
# colormap should be a dictionary having countries as keys and colors as values.
def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


# Implement main to call necessary functions
if __name__ == "__main__":
    myGraph = build_graph("sa.csv")

    colormap = backtrackingSearch(myGraph, colors, {}, list(myGraph.keys()), 0)

    # coloring test
    colormap_test = {"Argentina": "blue", "Bolivia": "red", "Brazil": "yellow", "Chile": "yellow", "Colombia": "red",
                     "Ecuador": "yellow", "Falkland Islands": "yellow", "Guyana": "red", "Paraguay": "green",
                     "Peru": "green", "Suriname": "green", "Uruguay": "red", "Venezuela": "green"}

    plot_choropleth(colormap=colormap)
