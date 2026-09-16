# Propriedade RowSourceType

Especifica o tipo pertencente ao conjunto de origem de linhas para a propriedade RowSource. Leitura/gravação em tempo de design e em tempo de execução.

Para obter mais informações sobre o uso da propriedade RowSourceType, consulte Como: escolher o tipo de dados para uma list box ou combo box.

```foxpro
Control.RowSourceType [= nValue]
```

# Valor de retorno
 **nValue**
Especifica um valor indicando o tipo para o valor de origem de linhas no controle. A tabela a seguir lista os valores de nValue. nValue Descrição 0 Nenhum. (Padrão) 1 Valor. 2 Alias de tabela. 3 Instrução SQL. 4 Arquivo de consulta (.qpr). 5 Matriz. 6 Campos. 7 Arquivos. 8 Estrutura de campos de uma tabela. 9 Pop-up. Incluído para compatibilidade com versões anteriores. 10 Objeto de coleção.

# Observações

Aplica-se a: ComboBox Control | ListBox Control
