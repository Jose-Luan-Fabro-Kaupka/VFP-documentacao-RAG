# Função WREAD( )

Incluída para compatibilidade com versões anteriores. Use o Form Designer em vez disso.

Determina se a janela atual ou especificada está envolvida no READ atual.

```foxpro
WREAD([window name])
```

#### Parâmetros
 window name

 Para determinar se uma janela está participando de um READ, especifique o nome da janela com window name.

 Se um nome de janela não for incluído, WREAD() retorna um valor lógico para a janela que está na frente, ou seja, a janela cujo nome é retornado por WONTOP().

# Valor de retorno

Valor de retorno - Lógico

# Observações

WREAD() retorna true (.T.) se a janela especificada estiver participando do READ atual; false (.F.) é retornado se a janela especificada não estiver envolvida no READ atual ou não existir.

Você pode fazer uma janela participar de um READ:

 - Incluindo o título da janela na cláusula READ WITH. Janelas que normalmente não estão envolvidas em um READ podem participar dessa forma. Janelas Browse, janelas de edição de memo e texto, janelas do sistema FoxPro e assim por diante podem participar de um READ.
- Criando um controle na janela. Um READ pode abranger várias janelas se você criar controles em várias janelas e depois emitir READ.
