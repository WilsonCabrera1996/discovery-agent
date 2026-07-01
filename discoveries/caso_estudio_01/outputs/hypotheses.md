# Hipótesis de Validación: Caso Estudio 01

## H-001: Recordatorios Automatizados por WhatsApp
**Supuesto Riesgoso:** Los pacientes olvidan sus citas porque no tienen una herramienta moderna de recordatorio.
**Enunciado:** Si enviamos recordatorios automatizados por WhatsApp, reduciremos la tasa de no-show del 30% al 10% en un periodo de 1 mes.
**Métrica:** Tasa de inasistencia (no-show rate) medida en el sistema de agenda.
**Umbral de Éxito:** Reducción >= 20% absoluto en la tasa de inasistencia.
**Regla de Decisión:** 
- **Éxito (Perseverar):** Si no-show <= 10%, escalar a toda la base de pacientes.
- **Fallo (Pivotar):** Si no-show > 15% tras 4 semanas, pivotar a recordatorios por llamada telefónica.
