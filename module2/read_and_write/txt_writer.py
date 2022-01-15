some_file = open("../files/example_write.txt", "w")

text = """когда илье звонит начальник
он сразу трубку не берет
а выжидает полминуты
и в это время он бунтарь
"""

some_file.write(text)

some_file.close()
