#################################################
# Web API Clientes
# Consulta de cliente por Id
#################################################

from Clientes.Models.Clientes import Clientes

def ConsultarPorId(Id):
    Cliente = {}
    for Cliente in Clientes:
        if Cliente["Id"] == Id:
            break
        else:
            Cliente = {}
    return Cliente