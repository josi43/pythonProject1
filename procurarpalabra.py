word = 'ç'
with open("texto.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        if word in line:
          print(f"Word '{word}' found on line {line_number}")
          break
print("Search completed.")