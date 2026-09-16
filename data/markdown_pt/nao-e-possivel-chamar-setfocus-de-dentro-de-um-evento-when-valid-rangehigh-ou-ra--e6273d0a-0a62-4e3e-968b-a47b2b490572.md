# Não é possível chamar SetFocus de dentro de um evento When, Valid, RangeHigh ou RangeLow (Erro 2012)

O método SetFocus entra em conflito com esses eventos, que estão testando se o objeto pode receber ou perder o foco.
 - Você está chamando SetFocus de um evento When. Chame SetFocus do evento GotFocus em vez disso.
- Você está chamando SetFocus de um evento Valid, RangeHigh ou RangeLow. Chame SetFocus do evento LostFocus em vez disso.
