# Classe Empty

Cria uma classe vazia que é instanciada e liberada rapidamente para uso com objetos de negócios.

```foxpro
Empty
```

# Observações

A classe base Empty não contém propriedades, métodos ou eventos intrínsecos. Você não pode fazer subclass de ou adicionar métodos e eventos personalizados à classe Empty. No entanto, em tempo de execução, você pode adicionar propriedades personalizadas usando a função ADDPROPERTY( ) ou o comando SCATTER NAME...ADDITIVE.

A classe Empty é normalmente usada nos seguintes cenários:
 - Ao adicionar propriedades a ou remover propriedades de uma instância em execução da classe usando as funções ADDPROPERTY( ) e REMOVEPROPERTY( ).
- Ao usar o comando SCATTER...NAME com a cláusula ADDITIVE para preencher conteúdos do registro atual.
