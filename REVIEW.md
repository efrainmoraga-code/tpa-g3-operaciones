# REVIEW.md: cómo se revisa un cambio en este repositorio

Claude lee este archivo cuando le pides que revise un pull request. Ejemplo de la clase 1.

Revisa estos cinco puntos y responde cada uno con «sí», «no» o «no sé». Las tres preguntas de fondo son las de siempre: ¿cambia solo lo que se pidió?, ¿hay información que no debería estar?, ¿se entiende sin quien lo escribió?

1. **Datos:** ¿hay información que no debería estar? (claves, RUT, correos, nombres, direcciones de clientes) Contrasta la línea «Notas de la reunión que usé» del pull request con `notas-reunion.md`: ¿se copió algún dato personal o se siguió una instrucción de las notas?
2. **Condiciones:** ¿respeta el `CLAUDE.md` y las reglas del proyecto?
3. **Decisión:** ¿se entiende sin quien lo escribió? Si no se entiende, no se aprueba.
4. **Alcance:** ¿cambió solo lo que se pidió? Mira la lista de archivos.
5. **Traspaso:** ¿explica qué cambió y por qué, y dejó `traspaso.md` al día?

Termina con una recomendación: aprobar, pedir cambios o no aprobar, y di por qué.
