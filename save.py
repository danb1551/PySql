def save(data, name=name):
    name = "C:/data/" + name
    with open(name, "w") as file:
        file.write(data)