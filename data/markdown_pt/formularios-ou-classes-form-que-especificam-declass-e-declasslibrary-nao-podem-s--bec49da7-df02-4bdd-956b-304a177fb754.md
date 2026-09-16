# Formulários ou classes Form que especificam DEClass e DEClassLibrary não podem ser convertidos para ou usados com um FormSet. (Erro 2069)

O Visual FoxPro não suporta as propriedades DEClass e DEClassLibrary do DataEnvironment para conjuntos de formulários. Um erro ocorre nas seguintes condições em tempo de design:
 - Ao tentar converter um formulário em um conjunto de formulários depois que as propriedades DEClass e DEClassLibrary foram especificadas para o formulário.
- Ao tentar adicionar uma classe Form que especifica as propriedades DEClass e DEClassLibrary a uma classe FormSet quando o conjunto de formulários está aberto no Form Designer.
