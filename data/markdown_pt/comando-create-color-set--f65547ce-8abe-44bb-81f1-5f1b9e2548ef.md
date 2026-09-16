# Comando CREATE COLOR SET

Cria um conjunto de cores a partir das configurações de cor atuais.

```foxpro
CREATE COLOR SET ColorSetName
```

#### Parâmetros
 **ColorSetName**
Especifica o nome do conjunto de cores a ser criado.

# Observações

Cada par de cores em cada esquema de cores é salvo no conjunto de cores que você cria. Um nome de conjunto de cores pode ter até 24 caracteres no Visual FoxPro (10 caracteres em versões anteriores do FoxPro) e pode conter números e sublinhados, mas não pode começar com um número.

Depois de criar um conjunto de cores, você pode carregá-lo com SET COLOR SET.

Conjuntos de cores são salvos no arquivo de recursos do Visual FoxPro. Se um conjunto de cores existir com o mesmo nome que você especificar, ele será substituído.
