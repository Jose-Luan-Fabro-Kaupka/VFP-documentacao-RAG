# Função INSMODE( )

Retorna o modo de inserção atual ou define o modo de inserção como ligado ou desligado.

```foxpro
INSMODE([lExpression])
```

#### Parâmetros
 **lExpression**
Liga ou desliga o modo de inserção. INSMODE(.T.) liga o modo de inserção e INSMODE(.F.) desliga. Um valor lógico correspondente à configuração do modo de inserção antes de INSMODE(.T.) ou INSMODE(.F.) ser emitido é retornado.

# Observações

Se você omitir o argumento opcional e o modo de inserção estiver ligado (caracteres são inseridos antes do cursor), INSMODE( ) retorna verdadeiro (.T.). Se o modo de inserção estiver desligado (caracteres são sobrescritos no ponto de inserção), INSMODE( ) retorna falso (.F.).

# Valor de retorno

Lógico

# Exemplo

O exemplo abaixo usa INSMODE( ) para ligar o modo de inserção e depois alterna o modo de inserção para o estado oposto.

```foxpro
SET TALK ON
=INSMODE(.T.)  && Set insert mode on
? INSMODE()
= INSMODE(!INSMODE())  && Toggle insert mode to opposite state
? INSMODE()
```
