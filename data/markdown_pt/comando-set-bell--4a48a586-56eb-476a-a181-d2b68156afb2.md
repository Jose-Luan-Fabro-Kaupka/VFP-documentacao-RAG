# Comando SET BELL

Ativa ou desativa o sinal sonoro do computador e define os atributos do sinal.

```foxpro
SET BELL ON | OFF
-or-
SET BELL TO [cWAVFileName]
```

#### Parâmetros
 **ON**
(Padrão) Ativa o sinal sonoro.
**OFF**
Desativa o sinal sonoro.
**TO cWAVFileName**
Especifica um som de forma de onda a ser reproduzido quando o sinal é acionado. cWAVFileName pode incluir um caminho para o som de forma de onda. Emita SET BELL TO sem cWAVFileName para restaurar o som de forma de onda padrão.

# Observações

SET BELL habilita ou desabilita a emissão do sinal sonoro durante a edição quando você atinge o final de um campo ou insere dados inválidos.

# Exemplo

O exemplo a seguir reproduz o Ding.wav.

```foxpro
SET BELL TO (ADDBS(GETENV('windir')))+"MEDIA\DING.WAV"
?? CHR(7)
```
