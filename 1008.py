#URI Online Judge - Iniciantes 1008

numEmpregado = int(input()) #Número que identifica o empregado
horasTrabalhadas = int(input()) #Número de horas trabalhadas
qntPorHora = float(input()) #Valor recebido por hora trabalhada

print("NUMBER =", numEmpregado)
print("SALARY = U$", "%.2f" % float(horasTrabalhadas*qntPorHora))
