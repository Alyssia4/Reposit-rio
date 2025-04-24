import calendar

def UltimoDia(mes, ano):
    dia = calendar.monthrange(ano, mes)[1]
    return f"{dia:02d}/{mes:02d}/{ano:04d}"