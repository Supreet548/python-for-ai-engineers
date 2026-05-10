try:
    file = open("notes.txt", "r")
    content = file.read()
    print(content)

    file.close()

except FileNotFoundError:
    print("File does not exist")

except Exception as e:
    print("Error:", e)