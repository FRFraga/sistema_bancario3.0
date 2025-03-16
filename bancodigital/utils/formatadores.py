def formatar_valor(valor):
    """Formata valores monetários para o padrão brasileiro"""
    return f"R$ {valor:,.2f}".replace(",", "temp").replace(".", ",").replace("temp", ".")