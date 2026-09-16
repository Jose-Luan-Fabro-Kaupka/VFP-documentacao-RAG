# Propriedade HeaderClass

Especifica o nome da classe membro a usar ao adicionar novos objetos membro de cabeçalho a um contêiner Column. Leitura/gravação em tempo de design e em tempo de execução.

A propriedade HeaderClass é usada em vez de MemberClass para um contêiner pai Column. Para obter mais informações sobre a propriedade MemberClass, consulte Propriedade MemberClass.

> **Observação:** Se a classe membro for baseada em uma classe armazenada em um arquivo de programa (.prg), certifique-se de que o arquivo de programa compilado (.fxp) esteja sincronizado com o arquivo .prg.

```foxpro
Column.HeaderClass [ = cClassName ]
```

# Valor de retorno

**cClassName**
Especifica o nome de uma classe membro em um arquivo de programa (.prg).

# Observações

Aplica-se a: objeto Column

Você não pode editar nem criar uma subclasse da classe Header em uma biblioteca de classes visuais (.vcx). É necessário usar um arquivo de programa (.prg) para definir uma classe Header.

A classe Column pode conter apenas um cabeçalho; portanto, nenhuma propriedade de contagem de cabeçalho está associada à coluna.

Em tempo de execução, alterar as propriedades HeaderClassLibrary e HeaderClass não afeta o cabeçalho. Você só pode alterar o cabeçalho usando os métodos AddObject ou NewObject, que substituem o cabeçalho atual pelo novo cabeçalho.
