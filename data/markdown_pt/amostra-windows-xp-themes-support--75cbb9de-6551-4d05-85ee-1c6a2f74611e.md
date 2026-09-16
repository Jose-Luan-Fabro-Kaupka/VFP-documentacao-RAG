# Amostra Windows XP Themes Support

Arquivo: ...\Samples\Solution\Toledo\Themes.scx

Esta amostra demonstra diferentes níveis de suporte do Visual FoxPro para Windows XP Themes. Themes estão ativados por padrão.

O Visual FoxPro suporta Windows XP themes em três níveis:
 - Nível de aplicação usando SYS(2700) - Enables Windows XP Themes e propriedade Themes de _SCREEN
- Nível de formulário usando a propriedade Themes do Form
- Nível de controle

# Suporte a Themes no nível de aplicação

Nesta amostra, você pode ativar Themes em toda a aplicação Visual FoxPro usando a função SYS(2700) - Enables Windows XP Themes selecionando Enable Themes at the application level - SYS(2700), que usa o seguinte código:

```foxpro
SYS(2700,1)
```

Para desativar Themes, passe zero (0) como o segundo parâmetro para SYS(2700).

```foxpro
SYS(2700,0)
```

Para ativar Themes usando a variável _SCREEN, selecione Enable Themes at the application level - _SCREEN.Themes, que define _SCREEN Themes como True (.T.):

```foxpro
_SCREEN.Themes = .T.
```

Para desativar Themes usando _SCREEN, defina _SCREEN Themes como False (.F.):

```foxpro
_SCREEN.Themes = .F.
```

Para obter mais informações, consulte SYS(2700) - Enables Windows XP Themes e Themes Property.

# Suporte a Themes no nível de formulário

Nesta amostra, para ativar Themes no nível de formulário, selecione Enable Themes at the form level, que define a propriedade Themes do formulário como True (.T.):

```foxpro
ThisForm.Themes = .T.
```

# Suporte a Themes no nível de controle

Você também pode ativar o suporte a Themes para controles individuais. Desativar Themes no nível de controle substitui a configuração de Themes no nível de aplicação ou formulário. Dependendo do controle, você pode definir o suporte a Themes através das propriedades Themes ou Style.

Para obter mais informações, consulte Style Property.
