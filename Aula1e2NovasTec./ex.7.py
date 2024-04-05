def converter_segundos():
    segundos = int(input("Insira a quantidade em segundos: "))
    dias = segundos // (24 * 3600)
    horas = (segundos % (24 * 3600)) // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print("Dias:", dias)
    print("Horas:", horas)
    print("Minutos:", minutos)
    print("Segundos:", segundos_restantes)

converter_segundos()