hour_seconds=3600
minute_seconds=60

hours=int(input('Ingrese las horas: '))
minutes=int(input('Ingrese los minutos: '))

minutes_to_seconds=minutes*minute_seconds
hours_to_second=hours*hour_seconds

print(f'Existen {hours_to_second + minutes_to_seconds} segundos en {hours} hora(s) y {minutes} minuto(s).')
