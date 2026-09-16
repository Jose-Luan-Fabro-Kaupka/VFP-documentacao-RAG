# Propriedade BufferMode

Especifica se os registros são atualizados pessimisticamente ou optimisticamente. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.BufferMode[ = nValue]
```

# Valor de retorno
 **nValue**
As configurações da propriedade BufferMode são: Configuração Descrição 0 (Padrão) Nenhum. Os registros são bloqueados quando a edição começa e os campos são gravados quando o ponteiro de registro se move. Simula o comportamento do FoxPro 2.x. 1 Pessimista. Os registros são bloqueados quando a edição começa e os campos são gravados quando o ponteiro de registro se move. Você pode usar TABLEREVERT( ) para desfazer suas alterações no registro atual. 2 Otimista. Os registros não são bloqueados quando editados e o Visual FoxPro tenta bloquear os registros quando são gravados no disco com TABLEUPDATE( ).

# Observações

Aplica-se a: Form Object | FormSet Object | _SCREEN System Variable

Se BufferMode estiver definido como 1 ou 2, qualquer cursor usado por um controle Grid é habilitado para buffer de tabela. Qualquer outro controle vinculado a dados usa buffer de linha.

A configuração da propriedade BufferMode substituirá quaisquer configurações de buffer feitas nos cursors do formulário antes do método Init do formulário, incluindo aquelas feitas no método Load do formulário.
