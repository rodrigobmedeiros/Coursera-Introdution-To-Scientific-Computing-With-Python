segundos_str = input('Por favor, entre com o número de segundos que deseja converter: ')

segundos_int = int(segundos_str)


dias = segundos_int//86400
segundosrestantes = segundos_int % 86400

horas = segundosrestantes//3600
segundosrestantes = segundosrestantes % 3600

minutos = segundosrestantes//60
segundosrestantes = segundosrestantes % 60


print(dias, 'dias,',horas,'horas,',minutos,'minutos e',segundosrestantes, 'segundos.' )
