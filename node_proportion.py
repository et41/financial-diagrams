def node_arrangement(data):
    proportion = 1 / sum(data)
    return [proportion * data[0], proportion * data[1]]
