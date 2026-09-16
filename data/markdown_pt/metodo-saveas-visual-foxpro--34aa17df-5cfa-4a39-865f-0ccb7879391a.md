# Método SaveAs (Visual FoxPro)

Salva um objeto como um arquivo .scx.

```foxpro
Object.SaveAs(cFileName [, oDataEnvironment])
```

#### Parâmetros
 **cFileName**
Especifica o arquivo .scx no qual você deseja salvar o objeto.
**oDataEnvironment**
Especifica uma referência a um objeto DataEnvironment. O objeto DataEnvironment deve ter sua propriedade Name definida como "DataEnvironment".

# Observações

Aplica-se a: Comando DEFINE CLASS | Objeto Form | Objeto FormSet | Variável de sistema _SCREEN

Use o método SaveAs para criar um formulário ou form set e salvá-lo como um arquivo .scx. O método SaveAs está disponível apenas durante uma sessão interativa do Visual FoxPro.

Quando você usa o método SaveAs, todas as propriedades, eventos e métodos associados ao objeto também são armazenados. Observe que apenas objetos criados a partir de classes base do Visual FoxPro podem ser salvos. Classes definidas pelo usuário não podem ser salvas. Para uma lista completa das classes base do Visual FoxPro, consulte Classes base no Visual FoxPro.
