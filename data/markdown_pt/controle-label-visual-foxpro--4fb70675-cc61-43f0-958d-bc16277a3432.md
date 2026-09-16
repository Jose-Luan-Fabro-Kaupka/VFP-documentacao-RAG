# Controle Label (Visual FoxPro)

Cria uma etiqueta que exibe texto.

```foxpro
Label
```

# Observações

Um controle Label é um controle gráfico que exibe texto que não pode ser alterado diretamente. No entanto, como um controle Label tem um conjunto completo de propriedades, eventos e métodos que outros controles possuem, o controle Label pode responder a eventos e pode ser alterado dinamicamente em tempo de execução.

Para atribuir uma tecla de acesso a uma etiqueta, inclua uma barra invertida e um sinal de menor que ("\<") no caption imediatamente antes do caractere que deseja designar como tecla de acesso. Quando a etiqueta é exibida, o caractere é sublinhado. Pressionar a tecla de acesso de uma etiqueta ativa o próximo controle na ordem de tabulação. Use a propriedade TabIndex para atribuir uma ordem de tabulação a uma etiqueta.

Os captions são exibidos de forma diferente dependendo do objeto.

256 é o número máximo de caracteres para a propriedade Caption de um controle Label.

Para obter informações adicionais sobre como criar controles Label, consulte Using Controls.
