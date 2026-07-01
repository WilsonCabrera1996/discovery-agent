# User Stories — Caso Estudio 01 (INVEST)

## Épica 1: Agendamiento y Autogestión
### US01: Reserva de Cita Autogestionada
**Como** paciente,
**quiero** poder seleccionar un turno disponible desde un portal web,
**para** agendar mi cita sin tener que llamar por teléfono en horario de oficina.
*   **Criterio de Aceptación:** El sistema debe mostrar solo los espacios marcados como "libres" por la doctora. El paciente debe recibir una confirmación inmediata al finalizar.
*   **Fuente:** `paciente.md`, `recepcionista.md`

### US02: Cancelación Fácil
**Como** paciente,
**quiero** poder cancelar mi cita desde el mensaje de recordatorio,
**para** liberar el espacio si no puedo asistir sin tener que llamar.
*   **Criterio de Aceptación:** Al cancelar, el estado del turno en la agenda debe cambiar a "disponible" automáticamente en tiempo real.
*   **Fuente:** `doctora.md` (Mitigación de huecos)

## Épica 2: Gestión y Control Médico
### US03: Visualización de Agenda Remota
**Como** doctora,
**quiero** consultar mi lista de pacientes del día desde mi celular,
**para** estar preparada antes de llegar a la clínica.
*   **Criterio de Aceptación:** La vista móvil debe cargar en menos de 3 segundos y mostrar nombre, hora y motivo de consulta.
*   **Fuente:** `doctora.md`

### US04: Control de Disponibilidad
**Como** doctora,
**quiero** bloquear días u horas específicas (por congresos o vacaciones),
**para** que los pacientes no puedan agendar en esos periodos.
*   **Criterio de Aceptación:** Los bloques definidos deben ocultar los turnos correspondientes en el portal del paciente de inmediato.
*   **Fuente:** `doctora.md`, `recepcionista.md`

## Épica 3: Automatización Operativa
### US05: Recordatorios Automáticos
**Como** recepcionista,
**quiero** que el sistema envíe recordatorios por WhatsApp a los pacientes del día siguiente,
**para** no tener que dedicar 1.5 horas diarias a llamadas manuales.
*   **Criterio de Aceptación:** El sistema debe enviar el mensaje a las 4:00 PM del día anterior. Debe incluir un link para confirmar o cancelar.
*   **Fuente:** `recepcionista.md`, `paciente.md`
