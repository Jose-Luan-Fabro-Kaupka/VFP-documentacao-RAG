# Propriedade Text (Visual FoxPro)

Contém o texto não formatado digitado na parte de caixa de texto de um controle. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.Text
```

# Observações

Aplica-se a: ComboBox Control | EditBox Control | Spinner Control | TextBox Control (Visual FoxPro)

Diferentemente da propriedade Value, o valor contido na propriedade Text não é formatado e é idêntico ao texto digitado no controle pelo usuário.

O texto não formatado contido na propriedade Text de um controle pode diferir da propriedade Value do controle pelos seguintes motivos:
 - A propriedade Value pode não ser do tipo Caractere; pode conter um valor Date ou Numeric.
- Para uma caixa de edição, a propriedade Value pode adicionar quebras de linha ao texto digitado na caixa de edição, fornecendo compatibilidade com versões anteriores. Por esse motivo, usar a propriedade Text é o método preferido para selecionar texto com as propriedades SelStart e SelLength.
- Se a propriedade Format do controle usar a configuração R, os caracteres da máscara de entrada são removidos da propriedade Value.

Se a propriedade Style de um controle de caixa de combinação estiver definida como 2 (Drop-down List), a propriedade Text contém a cadeia de caracteres vazia porque o ComboBox não tem uma caixa de texto.
