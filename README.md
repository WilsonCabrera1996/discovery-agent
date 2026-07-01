# Discovery Agent (Gemini Edition) 🚀

Este proyecto es un **Agente de Descubrimiento de Producto** diseñado para transformar evidencia cruda (entrevistas, notas, observaciones) en artefactos de producto estructurados y trazables. Representa el estándar de calidad de la **Unidad 1 de Ingeniería de Software (Maestría en Software)**.

## 🧠 Metodología y Calidad

El agente opera bajo un marco de trabajo de **evidencia-primero**, donde cada hallazgo debe estar respaldado por una fuente real. Para asegurar el rigor, el sistema implementa dos "Gates" de calidad obligatorios:

1.  **Readiness-Gate:** Valida que exista evidencia de primera mano para todos los actores core antes de permitir el diseño del MVP.
2.  **Hypothesis-Gate:** Audita las hipótesis para asegurar que utilicen métricas de negocio (no de vanidad), tengan umbrales exactos y definan reglas de decisión claras (perseverar o pivotar).

## 📁 Estructura del Proyecto

*   `/agent`: Núcleo lógico del agente, incluyendo habilidades (skills) y gates.
*   `/discoveries`: Directorio de casos de estudio.
    *   `/<caso>/interviews`: Evidencia cruda en formato Markdown.
    *   `/<caso>/outputs`: Artefactos generados (Personas, Historias de Usuario, MVP Canvas, Hipótesis).
*   `main.py`: Punto de entrada de la CLI.

## 🛠️ Comandos Disponibles

El agente se invoca a través de la CLI de Python:

```bash
# Analizar evidencia y generar Personas/Requisitos
python main.py analyze --case discoveries/caso_estudio_01

# Diseñar experimentos e hipótesis (Requiere Hypothesis-Gate)
python main.py experiment --case discoveries/caso_estudio_01

# Generar MVP Canvas y User Stories (Requiere Readiness-Gate)
python main.py mvp --case discoveries/caso_estudio_01
```

## 📄 Artefactos de Salida

Al completar un ciclo de descubrimiento, el agente genera en la carpeta `/outputs`:
*   `personas.md`: Arquetipos de usuarios basados en evidencia.
*   `requisitos.md`: Listado de necesidades funcionales y no funcionales.
*   `mvp-canvas.md`: Definición del Producto Mínimo Viable.
*   `hypotheses.md`: Hipótesis falsables validadas por el gate.
*   `report.html`: Reporte visual interactivo con diagramas Mermaid.

---
*Generado por el Discovery Agent - Unidad 1 Ingeniería de Software.*
