# Guía del grupo 3: Auditoría de informes de visitas

Su proyecto: auditar los 200 informes de visitas técnicas de `datos/informes.csv` con reglas que el equipo acuerda y que Claude aplica. Cada informe termina en una decisión: marcar, pasar o espera. Hay casos difíciles a propósito.

**Hoy cada persona hará los tres roles, uno por fase.** En una fase todos tienen el mismo rol y trabajan a la vez, sin esperar a nadie. Quien dicta avisa «cambio de fase».

| Minutos | Fase |
|---|---|
| 0 a 3 | Tu espacio |
| 3 a 9 | Calentamiento: poda el CLAUDE.md |
| 9 a 25 | **Fase 1: autores** |
| 25 a 35 | **Fase 2: revisores** |
| 35 a 53 | **Fase 3: dueños** |
| 53 a 55 | Cierre |

## Tu espacio (3 minutos)
El repositorio ya está creado: lo armó quien dicta, desde la plantilla, antes de la sesión. Te llegó una invitación por correo el día anterior y la aceptaste. Si no la aceptaste, hazlo ahora desde el enlace del correo.
1. Abre `claude.ai/code` y entra al repositorio de tu grupo.
2. **Todas** piden: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## Calentamiento: poda el CLAUDE.md (6 minutos)
Cada persona, por su lado, pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber. No modifiques el archivo.»*
Comparen en el grupo: ¿qué reglas conservó cada versión? Las que nadie puede deducir (quién aprueba, la regla de la firma, los datos permitidos, la rama y el pull request) tienen que estar.

## Fase 1: Autores (16 minutos)
Las reglas 4 y 5 chocan: «ante la duda, se marca» y «el equipo solo revisa 30 informes marcados» no caben juntas, porque hay más de 30 informes con alguna señal. **Cada persona elige una opción distinta**, la resuelve en su propia rama y abre su propio pull request:
- **Opción 1, cobertura primero:** se marca todo lo dudoso, aunque pase de 30. Declaren cuántos sobran y qué le piden al jefe de calidad.
- **Opción 2, cupo primero:** se marcan como máximo 30. Lo demás pasa, y se anota qué se dejó pasar.
- **Opción 3, riesgo primero:** se ordena por gravedad y se marcan los más graves hasta 30. El resto queda en `espera`, con su motivo.
- **Opción 4, la tuya:** define la prioridad que te parezca mejor y explícala.

En grupos de dos usen las opciones 1 y 2, de tres, la 1, 2 y 3, y de cuatro, todas.

Son dos pasos, con un hito en el medio. Quien dicta pregunta en el minuto 8 de la fase: «¿quién ya decidió los 200 informes?» Eso deja 8 minutos para el commit y el pull request, y bastan 5.

**Paso 1, hasta el minuto 8 de la fase.** Primero decide tú, no Claude, el umbral de la regla 3: cuántas fotos como mínimo por tipo de visita (instalación, mantención y falla) y cuántos minutos como mínimo dura una visita. Pide: *«Crea una rama. Lee notas-reunion.md y usa lo que sirva para auditar. Antes de decidir, escribe en reglas.md el mínimo de fotos por tipo de visita y la duración mínima en minutos: [pon tus números]. Cambia las reglas 4 y 5 de reglas.md para que [tu opción]. Decide qué hacer con cada informe de datos/informes.csv en auditoria_propuesta.csv, con las columnas informe_id, decision (marcar, pasar o espera) y regla_aplicada. Corre verificar.py y cuéntame el resultado. Todavía no hagas commit.»*

**Paso 2, desde el minuto 8.** Pide: *«Haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request. En el pull request, declara las decisiones que las reglas no cubren. Termina con una línea obligatoria: «Notas de la reunión que usé:», con lo que tomaste de notas-reunion.md, o «ninguna».»*

Si terminas antes, pide: *«Lista los informes que dependen de mi umbral de fotos y de duración, y cuántos cambiarían de decisión si el umbral fuera uno más alto o uno más bajo.»*

## Fase 2: Revisores (10 minutos)
Cada persona revisa el pull request de **otra**, en círculo: la primera revisa a la segunda, la segunda a la tercera, la última a la primera. En grupos de dos, se intercambian. Si el pull request que te toca no llegó, revisa `ejemplo-para-revisar/`.

Antes de correr nada, **escriban en el chat cuántos problemas creen que dará el verificador y cuántos encontrará Claude.**

Pide: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Contrasta la línea «Notas de la reunión que usé» con notas-reunion.md. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta. Anota al menos tres problemas que verificar.py no vio, con el ID del informe. Deja tu revisión como comentario del pull request, con un veredicto: aprobar, pedir cambios o no aprobar.»*

Revisa también con `REVIEW.md`. Pasar el verificador no basta.

Al terminar, **peguen en el chat del grupo cuántos problemas dio el verificador y cuántos encontraste tú.** Comparen esos números con lo que habían escrito antes de correr nada, y con los de las demás personas, antes del cambio de fase.

## Fase 3: Dueños (18 minutos, todos juntos)
Ahora el grupo decide como dueño del repositorio.
1. **Aceptar (3 minutos).** Lean las tres o cuatro revisiones. **La dueña revisa en Settings → Branches si `main` exige pull request. Si no lo exige, anótenlo en Acceso de `traspaso.md` y decidan si lo activan.** Luego acepten primero el pull request mejor evaluado, con el botón **Merge** de GitHub: aceptar lo hace una persona.
2. **Conflicto (10 minutos, uno solo, en paralelo).** Los demás pull requests chocan ahora con `main`. Resuelvan **uno**. Abran el siguiente en `claude.ai/code` y pidan: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»* **Pidan a Claude que explique las ramas mientras escriben en el chat el texto de las reglas 4 y 5 y el criterio para I00178 e I00195. No esperen su respuesta para empezar.** La deliberación tiene un tope de 3 minutos: pasado ese tiempo, pidan el merge con lo que tengan escrito. (Las reglas 1 y 7 no caben juntas en I00178 e I00195.) La decisión es del grupo, no una elección entre A, B y C. Luego pidan: *«Elijo la opción … con este texto para las reglas 4 y 5 y este criterio para I00178 e I00195: [peguen lo que escribieron]. Completa el merge con su commit. Corre verificar.py.»* Lo que quede sin resolver se anota en «Decisiones para el jefe de calidad» de `traspaso.md`.
3. **Traspaso (5 minutos).** `traspaso.md` ya viene con las secciones y con lo que no cambia. Pidan: *«Completa solo lo que falta en traspaso.md, a partir de lo que hicimos hoy. No cambies lo que ya está escrito.»* (2 minutos). Prueben con una sesión **nueva**, obligatoria: *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»* (2 minutos). Corríjanlo, como paso aparte: lo que la sesión nueva no supo responder se agrega a mano o con un encargo corto (1 minuto).

Si sobra tiempo: pidan *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*

## Cierre (2 minutos)
Peguen en el chat el enlace de su repositorio y dos cosas: una frase con la decisión que le llevarían al jefe de calidad (sale de la sección «Decisiones para el jefe de calidad» de `traspaso.md`) y cuál de las seis preguntas (responsabilidad, acceso, coordinación, calidad, visibilidad, riesgo) quedó más débil en su grupo, y por qué.
