# Exemplo SCATTER NAME...ADDITIVE

Arquivo: ...\Samples\Solution\Toledo\ScatterName.scx

Este exemplo demonstra como atualizar e salvar algumas propriedades de formulário de e para uma tabela usando o comando SCATTER com as cláusulas NAME e ADDITIVE e o comando GATHER com a cláusula NAME.

Neste exemplo, você pode atualizar um objeto existente com valores do registro atual usando a cláusula ADDITIVE com SCATTER NAME. Você pode então alterar a cor, redimensionar, mover ou minimizar o formulário e fechá-lo. Quando você executa o formulário novamente, ele aparece com a cor, tamanho, localização e estado anterior de quando foi fechado.

Para obter mais informações, consulte Comando GATHER e Comando SCATTER.

# Definindo propriedades de formulário a partir de uma tabela usando SCATTER...NAME... ADDITIVE

Neste exemplo, o seguinte código no evento Init do formulário abre uma tabela e define as propriedades do formulário a partir dos campos correspondentes na tabela, conforme mostrado:

```foxpro
USE (ThisForm.cRunPath+"FormProps")
SCATTER NAME ThisForm ADDITIVE
USE IN FormProps
```

A palavra-chave ADDITIVE torna possível atualizar e adicionar propriedades de objeto.

# Salvando propriedades de formulário em uma tabela usando GATHER NAME

Neste exemplo, quando o formulário é fechado, os valores das propriedades são salvos nos campos correspondentes da tabela, o que ocorre no evento Destroy do formulário.

```foxpro
USE (ThisForm.cRunPath+"FormProps")
GATHER NAME ThisForm
USE IN FormProps
```

> **Observação:** Esta tabela é criada em um banco de dados para que os comprimentos dos campos possam ser maiores que 10 caracteres.
