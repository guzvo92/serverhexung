#1/Saca el primer registro de la N-basededatos
#E- Manejar excepcion si no hay registros
regx = modelocharsel.objects.first()
tiempoinicial = regx.created_at
