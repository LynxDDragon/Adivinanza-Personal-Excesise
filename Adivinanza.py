#prompt part of riddle
adivinanza = "\nQue son dos cosas que van en la sopa,"
adivinanza += "\npero no te las puedes comer? ... "

#input function
while True:
    respuesta = input(adivinanza)
    if respuesta == "me rindo":
        break

    if respuesta == "la cuchara y el plato":
        while respuesta == "la cuchara y el plato":
             print("CORRECTO!!!!!")

#if answer is incorrect, ask for surrender. Second question/input
    if respuesta != "la cuchara y el plato":
        seguir = "Nope... te quieres rendir?"
        seguir = input(seguir)
        if seguir == "me rindo":
            print("No te puedes comer el plato, ni la cuchara")
            break