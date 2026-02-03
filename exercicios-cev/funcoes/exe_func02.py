def escreva(txt: str):
    tam = len(txt) + 2
    print("~" * tam)
    print(txt.upper().strip().center(tam))
    print("~" * tam)


recebe_txt = str(input("Digite o título: "))
escreva(recebe_txt)
