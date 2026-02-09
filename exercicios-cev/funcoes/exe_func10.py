def notas(*args, situacao=False):
    notas_dict = {
        "total": len(args),
        "maior": max(args),
        "menor": min(args),
        "media": sum(args) / len(args),
    }

    if situacao:
        notas_dict["situacao"] = "Bom" if notas_dict["media"] >= 7 else "Ruim"

    return notas_dict


notas_aluno = notas(8, 10, 9, 2, situacao=True)
print(notas_aluno)
