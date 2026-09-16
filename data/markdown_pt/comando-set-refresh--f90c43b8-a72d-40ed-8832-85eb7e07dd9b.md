# Comando SET REFRESH

Determina se e com que frequência atualizar uma janela de navegação ou de edição de memo, ou atualizar os buffers de memória locais com alterações de outros usuários na rede.

```foxpro
SET REFRESH TO nSeconds1 [, nSeconds2]
```

#### Parâmetros
 **nSeconds1**
Especifica o número de segundos entre as atualizações da exibição de uma janela de navegação ou de edição de memo. nSeconds1 pode ser um valor inteiro de 0 (padrão) a 3.600 segundos. Definir nSeconds1 como 0 não atualiza os registros que você está visualizando. Observação Valores fracionários são truncados. Se você especificar um valor diferente de 0 para nSeconds1 e omitir nSeconds2, então nSeconds2 será definido com o mesmo valor de nSeconds1. No entanto, se você especificar 0 segundos para nSeconds1 e omitir nSeconds2, então nSeconds2 será definido como 5 segundos.
**[, nSeconds2 ]**
Especifica o número de segundos entre a atualização dos buffers de memória locais com os dados atuais da rede. O valor padrão é 5 segundos. Definir nSeconds2 como 0 não atualiza os buffers. Dica Você pode melhorar o desempenho aumentando o valor de nSeconds2. Você também pode definir essa opção na guia Data da caixa de diálogo Options. A tabela a seguir descreve os valores para nSeconds2. nSeconds2 Descrição -1 Sempre ler dados do disco. 0 Sempre usar dados no buffer de memória, mas não atualizar o buffer. .001 a 3.600 Atualizar os buffers de memória locais a cada número de segundos especificado. Valores fracionários são aceitos. Observação Para fins de exibição, o Visual FoxPro arredonda o valor de nSeconds2 para o milissegundo mais próximo.

# Observações

Como as tabelas podem ser abertas para uso compartilhado em uma rede, é possível que outros usuários na rede estejam editando os registros que você está visualizando em uma janela de navegação. Ao definir SET REFRESH, você pode controlar o intervalo de tempo entre as atualizações da janela de navegação. Quando você define o comando SET REFRESH com um valor diferente de zero e outros usuários alteram registros que você está visualizando, os registros são atualizados quando o intervalo de atualização expira.

SET REFRESH afeta os registros exibidos em uma janela de navegação aberta com os comandos BROWSE, CHANGE ou EDIT. Campos Memo abertos para edição em uma janela de navegação, por exemplo, usando o comando MODIFY MEMO, também são atualizados. Para obter mais informações, consulte BROWSE Command, CHANGE Command, EDIT Command e MODIFY MEMO Command.

O Visual FoxPro armazena em buffer partes das tabelas na memória da sua estação de trabalho. SET REFRESH pode especificar a frequência com que os dados armazenados em buffer localmente na sua estação de trabalho são atualizados.
