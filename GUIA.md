# Guía del grupo 3: Auditoría de informes de visitas

Su proyecto: auditar los 200 informes de visitas técnicas de `datos/informes.csv` con reglas que el equipo acuerda y que Claude aplica. Cada informe termina en una decisión: marcar, pasar o espera. Hay casos difíciles a propósito.

**Hoy cada persona hará los tres roles, uno por fase.** En una fase todos tienen el mismo rol y trabajan a la vez, sin esperar a nadie. Quien dicta avisa «cambio de fase».

Palabras que vas a oír, en una línea cada una:
- **Rama:** una copia de trabajo del proyecto donde cambias cosas sin tocar la versión oficial.
- **Commit:** guardar tus cambios con una nota que dice qué cambiaste y por qué.
- **Pull request:** pedir que tu rama entre a la versión oficial, para que otra persona la revise antes.
- **Merge:** unir una rama a la versión oficial (`main`) cuando ya fue aceptada.
- **Conflicto:** dos ramas cambiaron la misma parte y alguien tiene que decidir con cuál se queda.

| Minutos | Fase |
|---|---|
| 0 a 6 | Tu espacio |
| 6 a 13 | Calentamiento: poda el CLAUDE.md *(opcional: si falta tiempo, recórtalo a 6 o sáltalo)* |
| 13 a 26 | **Fase 1: autores** |
| 26 a 36 | **Fase 2: revisores** |
| 36 a 52 | **Fase 3: dueños** |
| 52 a 55 | Cierre *(2 a 4 minutos, según lo que sobre)* |

Los encargos a Claude en la web tardan de 1 a 4 minutos cada uno: lanza el siguiente mientras lees lo anterior, y no esperes con la pantalla quieta. **Si el tiempo falta, lo primero que se recorta es el calentamiento, luego «Si terminas antes» de la Fase 1 y `proyecto.md`. Nunca se recorta el paso de las seis preguntas ni el traspaso.**

## Tu espacio (6 minutos)
El repositorio ya está creado: lo armó quien dicta, desde la plantilla, antes de la sesión. Te llegó una invitación por correo el día anterior y la aceptaste. Si no la aceptaste, hazlo ahora desde el enlace del correo. **La persona dueña** es la que tiene rol Admin; si esa persona falta, otra con Admin hace lo suyo, y si nadie lo tiene, anótenlo en «Qué decidimos y por qué» de `traspaso.md` y sigan.
1. Abre `claude.ai/code` y entra al repositorio de tu grupo.
2. **Todas** piden: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

## Calentamiento: poda el CLAUDE.md (7 minutos, opcional)
Cada persona, por su lado, pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber. No modifiques el archivo.»*
Comparen en el grupo: ¿qué reglas conservó cada versión? Las que nadie puede deducir (quién aprueba, la regla de la firma, los datos permitidos, la rama y el pull request) tienen que estar.

## Fase 1: Autores (13 minutos)
Las reglas 4 y 5 chocan: «ante la duda, se marca» y «el equipo solo revisa 30 informes marcados» no caben juntas, porque hay más de 30 informes con alguna señal. **Cada persona elige una opción distinta**, la resuelve en su propia rama y abre su propio pull request:
- **Opción 1, cobertura primero:** se marca todo lo dudoso, aunque pase de 30. Declaren cuántos sobran y qué le piden al jefe de calidad.
- **Opción 2, cupo primero:** se marcan como máximo 30. Lo demás pasa, y se anota qué se dejó pasar.
- **Opción 3, riesgo primero:** se ordena por gravedad y se marcan los más graves hasta 30. El resto queda en `espera`, con su motivo.
- **Opción 4, la tuya:** define la prioridad que te parezca mejor y explícala.

En grupos de dos usen las opciones 1 y 2, de tres, la 1, 2 y 3, y de cuatro, todas.

Son dos pasos, con un hito en el medio. Quien dicta pregunta en el minuto 8 de la fase: «¿quién ya decidió los 200 informes?» Eso deja 5 minutos para el commit y el pull request, y bastan.

**Paso 1, hasta el minuto 8 de la fase.** Las reglas las cambias en tu rama: es una propuesta, y el jefe de calidad las aprueba al final. Primero decide tú, no Claude, el umbral de la regla 3: cuántas fotos como mínimo por tipo de visita (instalación, mantención y falla) y cuántos minutos como mínimo dura una visita. Pide: *«Crea una rama. Lee notas-reunion.md y usa lo que sirva para auditar. Antes de decidir, escribe en reglas.md el mínimo de fotos por tipo de visita y la duración mínima en minutos: [pon tus números]. Cambia las reglas 4 y 5 de reglas.md para que [tu opción]. Decide qué hacer con cada informe de datos/informes.csv en auditoria_propuesta.csv, con las columnas informe_id, decision (marcar, pasar o espera) y regla_aplicada. Corre verificar.py y cuéntame el resultado. Todavía no hagas commit.»*

**Paso 2, desde el minuto 8.** Pide: *«Haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request. En el pull request, declara las decisiones que las reglas no cubren. Termina con una línea obligatoria: «Notas de la reunión que usé:», con lo que tomaste de notas-reunion.md, o «ninguna».»*

*(Opcional)* Si terminas antes, pide: *«Lista los informes que dependen de mi umbral de fotos y de duración, y cuántos cambiarían de decisión si el umbral fuera uno más alto o uno más bajo.»*

## Fase 2: Revisores (10 minutos)
Cada persona revisa el pull request de **otra**, en círculo: la primera revisa a la segunda, la segunda a la tercera, la última a la primera. En grupos de dos, se intercambian. Si el pull request que te toca no llegó, revisa `ejemplo-para-revisar/`.

Antes de correr nada, **escriban en el chat cuántos problemas creen que dará el verificador y cuántos encontrará Claude, y el ID de un informe que sospechen que el verificador dejará pasar.**

Pide: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Contrasta la línea «Notas de la reunión que usé» con notas-reunion.md. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta. Anota al menos tres problemas que verificar.py no vio, con el ID del informe. Deja tu revisión como comentario del pull request, con un veredicto: aprobar, pedir cambios o no aprobar.»*

Revisa también con `REVIEW.md`. Pasar el verificador no basta.

Al terminar, **peguen en el chat del grupo cuántos problemas dio el verificador y cuántos encontraste tú.** Comparen esos números con lo que habían escrito antes de correr nada, digan si acertó el informe que sospechaban, y comparen con las demás personas antes del cambio de fase.

*Para recordar:* cuando una persona ordena seguir una nota o una observación de los datos, Claude puede obedecer en parte. Eso lo decide la persona, no el archivo.

## Fase 3: Dueños (16 minutos, todos juntos)
Ahora el grupo decide como dueño del repositorio.
1. **Aceptar (3 minutos).** Lean las tres o cuatro revisiones. **La persona dueña revisa en Settings → Branches si `main` exige pull request. Si no lo exige, anótenlo en «Qué decidimos y por qué» de `traspaso.md` y decidan si lo activan.** Luego acepten primero el pull request mejor evaluado, con el botón **Merge** de GitHub: aceptar lo hace una persona.
2. **Conflicto (7 minutos, uno solo, en paralelo).** Los demás pull requests chocan ahora con `main`. Resuelvan **uno**. Abran el siguiente en `claude.ai/code` y pidan: *«Explícame qué cambió cada rama y propón cómo unirlas, y dime qué reglas que Git fusionó sin conflicto se contradicen igual. No apliques nada hasta que yo elija.»* **Pidan a Claude que explique las ramas mientras escriben en el chat el texto de las reglas 4 y 5 y el criterio para I00178 e I00195. No esperen su respuesta para empezar.** La deliberación tiene un tope de 2 minutos: pasado ese tiempo, pidan el merge con lo que tengan escrito. (Las reglas 1 y 7 no caben juntas en I00178 e I00195.) La decisión es del grupo, no una elección entre A, B y C. Luego pidan: *«Elijo la opción … con este texto para las reglas 4 y 5 y este criterio para I00178 e I00195: [peguen lo que escribieron]. Completa el merge con su commit. Corre verificar.py.»* Lo que quede sin resolver se anota en «Qué quedó pendiente» de `traspaso.md`.
3. **Traspaso (4 minutos).** `traspaso.md` tiene las cinco partes: qué cambió, qué quedó pendiente, qué decidimos y por qué, qué no hay que tocar y cuál es el siguiente paso. Pidan: *«Completa traspaso.md con las cinco partes, a partir de lo que hicimos hoy. Pregúntame lo que no sepas y no inventes. No cambies lo que ya está escrito.»* (2 minutos). Lo que quedó sin resolver (I00178 e I00195, el mínimo de fotos y la duración si los autores eligieron números distintos, los informes de la APK 2.3) va en «Qué quedó pendiente», como decisión para el jefe de calidad. Prueben con una sesión **nueva**, obligatoria: *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»* (2 minutos). Lo que la sesión nueva no supo responder se agrega a mano mientras escriben el paso siguiente.
4. **Las seis preguntas (2 minutos).** Cada persona escribe en el chat **una línea** que conteste **una** de las seis preguntas con algo que vivió hoy, con un ID, una rama o un número. Repártanse las seis (en grupos de dos o tres, cada persona toma más de una, o se repiten las más débiles):
   - **Responsabilidad:** ¿quién respondió por cada cambio y por las reglas?
   - **Acceso:** ¿quién podía cambiar `main` y quién no?
   - **Coordinación:** ¿cómo evitamos pisarnos, y qué chocó igual?
   - **Calidad:** ¿cómo supimos que lo que entró estaba bien?
   - **Visibilidad:** ¿dónde se ve qué se decidió y qué sigue?
   - **Riesgo:** ¿qué se pasó de largo o no tenía dueño?

Si sobra tiempo *(opcional)*: pidan *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*

## Cierre (2 a 4 minutos)
Peguen en el chat el enlace de su repositorio y dos cosas (la primera es lo mínimo; la segunda, si hay tiempo): una frase con la decisión que le llevarían al jefe de calidad (sale de «Qué quedó pendiente» de `traspaso.md`) y cuál de las seis preguntas (responsabilidad, acceso, coordinación, calidad, visibilidad, riesgo) quedó más débil en su grupo, y por qué.
