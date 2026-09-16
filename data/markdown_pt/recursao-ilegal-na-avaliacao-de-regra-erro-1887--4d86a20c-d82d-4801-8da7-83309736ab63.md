# Recursão ilegal na avaliação de regra (Erro 1887)

Um código de regra ou trigger fez com que o cursor original, o cursor do qual a regra ou o trigger foi disparado, tentasse avaliar uma regra ou trigger recursivamente. Isso pode ocorrer nas seguintes condições:
 - Tentativa de mover o ponteiro de registro ou alterar valores no cursor original.
- Tentativa de mover o ponteiro de registro no evento BeforeUpdate de um objeto CursorAdapter.

Verifique seu código de regra ou trigger.
