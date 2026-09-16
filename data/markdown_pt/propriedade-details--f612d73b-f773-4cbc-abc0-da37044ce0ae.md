# Propriedade Details

Especifica detalhes adicionais sobre um objeto de exceção que estão relacionados às informações especificadas pela propriedade Message. Leitura/gravação em tempo de execução.

```foxpro
Exception.Details
```

# Valor de retorno

Tipo de dados Character. Details pode ser NULL a menos que o erro tenha um parâmetro adicional; nesse caso, esta propriedade contém o texto do parâmetro de erro.

# Observações

Aplica-se a: classe Exception (Visual FoxPro)

Idêntico ao valor retornado por SYS(2018) e ao terceiro elemento na matriz produzida pela função AERROR().
