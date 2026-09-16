# Função SYS(0) - Informações da máquina na rede

SYS(0) retorna informações da máquina na rede ao usar o Visual FoxPro em um ambiente de rede. A mesma funcionalidade está disponível usando ID( ).

```foxpro
SYS(0)
```

# Valor de retorno

Character

# Observações

As informações da máquina devem ser atribuídas primeiro pelo software de rede e o shell de rede deve estar carregado.

Se as informações da máquina não tiverem sido atribuídas ou o shell de rede não estiver carregado, SYS(0) retorna uma cadeia de caracteres composta por 15 espaços, um sinal de número (#) seguido de outro espaço e então 0. Consulte a documentação da sua rede para obter mais informações sobre como definir informações da máquina.

SYS(0) retorna 1 ao usar o Visual FoxPro em um ambiente autônomo.

Quando a máquina está conectada a uma rede, SYS(0) retorna o nome da máquina, um espaço, um sinal de número (#) seguido de outro espaço e então o id do usuário atual (ou o contexto de segurança no qual o Visual FoxPro está em execução). Por exemplo:

```foxpro
? SYS(0)
```

retorna o seguinte formato:

```foxpro
MACHINEID # userid
```
