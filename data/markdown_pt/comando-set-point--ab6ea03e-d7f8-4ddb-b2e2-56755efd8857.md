# Comando SET POINT

Determina o caractere de ponto decimal usado na exibição de expressões numéricas e de moeda.

```foxpro
SET POINT TO [cDecimalPointCharacter]
```

#### Parâmetros
 **cDecimalPointCharacter**
Especifica o caractere do ponto decimal.

# Observações

Use SET POINT para alterar o ponto decimal do padrão, que é um ponto (.). Emita SET POINT TO sem cDecimalPointCharacter para redefinir o ponto decimal para um ponto. Embora você possa definir o ponto decimal exibido como um caractere diferente, deve usar um ponto como ponto decimal em cálculos.

SET POINT tem escopo na sessão de dados atual.

# Exemplo

```foxpro
gnX = 1.25
gcNewPoint = '_'
SET POINT TO gcNewPoint
? gnX
SET POINT TO      && Reset the decimal point to a period (.)
? gnX
```
