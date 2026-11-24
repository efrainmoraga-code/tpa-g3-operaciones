#!/usr/bin/env python3
"""Verifica que auditoria_propuesta.csv no rompa algunas reglas duras. Uso: python3 verificar.py [archivo.csv]
El archivo debe tener las columnas: informe_id, decision (marcar, pasar o espera), regla_aplicada."""
import csv, sys
from datetime import date
HOY = date(2026, 11, 24)
inf = {r["informe_id"]: r for r in csv.DictReader(open("datos/informes.csv"))}
errores, filas = [], list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else "auditoria_propuesta.csv")))
vistos = {f["informe_id"] for f in filas}
for i in inf:
    if i not in vistos: errores.append(f"{i}: no aparece en la propuesta")
for f in filas:
    i, d = f["informe_id"], f["decision"].strip().lower()
    if i not in inf: errores.append(f"{i}: no es un informe del lote"); continue
    if d not in ("marcar", "pasar", "espera"): errores.append(f"{i}: la decisión «{d}» no es marcar, pasar ni espera"); continue
    r = inf[i]
    if r["firma_cliente"] == "N" and d == "pasar":
        errores.append(f"{i}: regla 1, no tiene firma del cliente y no puede pasar")
    if date.fromisoformat(r["fecha_visita"]) > HOY and d == "pasar":
        errores.append(f"{i}: regla 2, la fecha {r['fecha_visita']} es posterior a hoy y no puede pasar")
    if d in ("marcar", "espera") and not f.get("regla_aplicada", "").strip():
        errores.append(f"{i}: regla 10, falta la regla aplicada")
print(f"{len(filas)} filas revisadas, {len(errores)} problemas")
for x in errores: print(" -", x)
sys.exit(1 if errores else 0)
