def validar_dataset(split):
    erros = []

    for indice, exemplo in enumerate(dataset[split]):
        mensagens = exemplo.get("messages")

        if not isinstance(mensagens, list) or not mensagens:
            erros.append((indice, "messages ausente ou vazio"))
            continue

        roles = [mensagem.get("role") for mensagem in mensagens]

        if roles != ["system", "user", "assistant"]:
            erros.append((indice, f"ordem de roles: {roles}"))

        for mensagem in mensagens:
            content = mensagem.get("content")

            if not isinstance(content, str) or not content.strip():
                erros.append((indice, "content vazio ou inválido"))
                break

    return erros


for split in ["train", "validation"]:
    erros = validar_dataset(split)

    print(f"{split}: {len(erros)} erros")

    for erro in erros[:10]:
        print(erro)