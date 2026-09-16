# Como: criar scripts do IntelliSense

Você pode criar scripts para itens da tabela IntelliSense. Eles permitem que comandos, funções ou propriedades executem código, por exemplo, abrindo um editor de valores. Consulte Estrutura da tabela IntelliSense.

As seções a seguir descrevem maneiras de criar e referenciar scripts:
 - Criando ou referenciando scripts para vários itens
- Referenciando scripts para itens únicos

# Criando ou referenciando scripts para vários itens

Na tabela IntelliSense, um registro Script pode conter no campo Data um procedimento personalizado ou código do Visual FoxPro executado por outros registros. Também é possível armazenar código para um único item. O campo Data ainda pode conter metadados passados automaticamente ao script pelo objeto de parâmetro FoxCode.

### Para criar scripts executados por outros registros IntelliSense
- Abra a tabela IntelliSense em FoxCode.dbf pelo IntelliSense Manager ou programaticamente.
- Crie um registro para um item Script.
- No campo Abbrev, digite a palavra-chave usada por outros registros para referenciar o script.
- No campo Data, digite o código Visual FoxPro. Observação O código deve conter PARAMETERS ou LPARAMETERS para receber a referência ao objeto FoxCode.
- No campo Cmd dos itens que executam o script, digite a palavra-chave de Abbrev entre chaves ({}).

Por exemplo, este texto em Abbrev define a palavra-chave:

`Picture`

Este código no campo Data exibe a caixa de diálogo Open Picture:

```foxpro
LPARAMETERS oFoxcode  && Required statement.
LOCAL lcPicture
oFoxcode.valuetype="V"
lcPicture = getpict()
IF LEN(lcPicture) > 0
   lcPicture = ['] + lcPicture+ [']
ENDIF
RETURN lcPicture
```

O texto a seguir no campo Cmd de outros registros define a referência:

`{picture}`

### Para referenciar scripts IntelliSense existentes
- Localize o item Script desejado.
- Localize sua palavra-chave no campo Abbrev.
- No campo Cmd do registro que executará o script, digite a palavra-chave entre chaves ({}).

# Referenciando scripts para itens únicos

Exceto em itens Typing e COM Component, quando Cmd contém apenas `{}`, digitar o texto de Abbrev executa o código de Data do mesmo item.

### Para criar scripts para registros IntelliSense únicos
- Localize o item desejado.
- Digite o código Visual FoxPro no campo Data.
- Digite chaves sem espaço ({}) no campo Cmd.

Exemplo de código no campo Data de um item Command:

| Nome do campo | Exemplo |
| --- | --- |
| Type | C |
| Abbrev | NOW |
| Cmd | {} |
| Data | (Armazenado em um campo memo) LPARAMETERS oFoxCode RETURN TRANSFORM(DATE( )) |
