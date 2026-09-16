# Propriedade DataSessionID

Retorna o ID da sessão de dados que identifica a sessão de dados privada para o objeto. Somente leitura em tempo de design; leitura/gravação em tempo de execução.

Se a propriedade DataSession do objeto estiver definida como 1 (Default Data Session), retorna o ID da sessão de dados padrão.

```foxpro
Object.DataSessionID
```

# Observações

Aplica-se a: Objeto Form | Objeto FormSet | Variável de sistema _SCREEN | Objeto Session | Objeto ToolBar

Disponível somente se a propriedade DataSession do objeto estiver definida como 2 (Private data session).

Você pode usar SET DATASESSION com a propriedade DataSessionID para alterar sessões de dados.

Quando você define DataSessionID, a configuração afeta a sessão de dados de trabalho para o objeto. A configuração da propriedade DataSessionID não afeta objetos que você cria usando CREATEOBJECT( ).

Alterar a configuração da propriedade DataSessionID incrementa a contagem de referências da sessão de dados alterada para e decrementa a contagem de referências da sessão de dados alterada de. No entanto, se você criar uma sessão de dados definindo a propriedade DataSession como 2 (Private data session), alterar a configuração da propriedade DataSessionID não libera a sessão de dados inicial. Nesse caso, o objeto deve ser liberado para liberar a sessão inicial.

Para mais informações sobre várias sessões de dados, consulte Programação para acesso compartilhado.

> **Cuidado:** Alterar a configuração da propriedade DataSessionID de um objeto que contém controles vinculados a dados faz com que os controles percam suas fontes de dados originais. Em geral, use DataSessionID em objetos que não contêm controles vinculados a dados.
