def area(largura: float, comprimento: float) -> float:
    return largura * comprimento


recebe_largura = float(input("Largura (m): "))
recebe_comprimento = float(input("Comprimento (m): "))
metro_quadrado = area(recebe_largura, recebe_comprimento)

print(
    f"A área de um terreno {recebe_largura}x{recebe_comprimento} é de {metro_quadrado}m²."
)
