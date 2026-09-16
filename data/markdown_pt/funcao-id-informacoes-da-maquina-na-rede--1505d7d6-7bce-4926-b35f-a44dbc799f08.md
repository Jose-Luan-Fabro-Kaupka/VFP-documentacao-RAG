# Função ID( ) — Informações da máquina na rede

ID( ) retorna informações da máquina em um ambiente de rede. A mesma funcionalidade está disponível por meio de SYS(0).

```foxpro
ID()
```

# Valor de retorno

Character

# Observações

As informações do computador devem primeiro ser atribuídas pelo software de rede, e o shell da rede deve estar carregado.

Se essas informações não tiverem sido atribuídas ou o shell não estiver carregado, ID( ) retornará uma cadeia com 15 espaços, um sinal de número (#), outro espaço e 0. Consulte a documentação da rede para obter mais informações sobre como definir os dados da máquina.

ID( ) retorna 1 quando o Visual FoxPro é usado em um ambiente autônomo.

Quando o computador está conectado a uma rede, ID( ) retorna o nome do computador, um espaço, um sinal de número (#), outro espaço e a identificação do usuário atual (ou o contexto de segurança no qual o Visual FoxPro está em execução). Por exemplo:

```foxpro
? ID()
```

retorna o seguinte formato:

```foxpro
MACHINEID # userid
```
