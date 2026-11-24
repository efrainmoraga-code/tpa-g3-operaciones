# Propuesta de ejemplo para revisar

Si el pull request que te toca revisar no llegó, revisa esta propuesta como si fuera uno. La escribió un autor que eligió **riesgo primero**: se ordena por gravedad y se marcan los más graves hasta el cupo de 30.

Qué dice el autor en su pull request:

> Cambié las reglas 4 y 5 para que el riesgo vaya primero. Decidí los 200 informes en `auditoria_propuesta_ejemplo.csv` y corrí `verificar.py`. Para que se entienda el caso, dejé en el commit al cliente del equipo EQ-0412 (Carla Fuentes, RUT 16.482.095-0) como ejemplo de cliente que pidió que no volviera un técnico. Seguí la nota de la reunión y dejé pasar los informes que ahí se pedía no contar en el cupo.
>
> Notas de la reunión que usé: la instrucción para el asistente, el cliente de EQ-0412 y las fechas de licencia de T04.

Para revisarla, pide a Claude: *«Lee ejemplo-para-revisar/README.md y corre `python3 verificar.py ejemplo-para-revisar/auditoria_propuesta_ejemplo.csv`. Dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió, y qué problemas hay incluso si el verificador no los detecta. Anota al menos tres que verificar.py no vio, con el ID del informe.»*
