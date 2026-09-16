# Comando SET FIXED

Especifica se o número de casas decimais usadas na exibição de dados numéricos é fixo.

```foxpro
SET FIXED ON | OFF
```

#### Parâmetros
 **ON**
Usa a configuração SET DECIMALS para determinar o número de casas decimais exibidas nos resultados. O número padrão de casas decimais é 2.
**OFF**
(Padrão) Permite que o número de casas decimais exibidas nos resultados dependa das constantes, variáveis e operadores específicos usados em uma expressão numérica. O conteúdo dos campos é exibido com o número declarado de casas decimais.

# Observações

SET FIXED tem escopo na sessão de dados atual.
