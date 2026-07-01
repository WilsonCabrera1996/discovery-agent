# Requisitos de Producto — Caso Estudio 01

## Funcionales (FR)
1.  **RF01: Agendamiento Autogestionado:** El sistema debe permitir al paciente reservar citas sin intervención de la recepcionista. [Fuente: `recepcionista.md`, `paciente.md`]
2.  **RF02: Sincronización de Disponibilidad:** El sistema debe mostrar la disponibilidad real en tiempo real para evitar duplicidades de citas. [Fuente: `recepcionista.md`]
3.  **RF03: Recordatorios Automatizados:** El sistema debe enviar notificaciones de recordatorio (vía WhatsApp/digital) de forma automática. [Fuente: `paciente.md`, `recepcionista.md`]
4.  **RF04: Consulta de Información:** Los pacientes deben poder consultar horarios de atención y disponibilidad sin realizar llamadas telefónicas. [Fuente: `recepcionista.md`]
5.  **RF05: Acceso Remoto Médico:** El sistema debe permitir al médico visualizar su agenda desde dispositivos móviles. [Fuente: `doctora.md`]
6.  **RF06: Captura de Motivo de Consulta:** El proceso de agendamiento debe incluir un campo para que el paciente indique el motivo de la consulta. [Fuente: `doctora.md`]
7.  **RF07: Gestión de Disponibilidad y Bloqueos:** El médico debe poder definir sus horarios de atención y realizar bloqueos temporales por eventos externos. [Fuente: `doctora.md`]
8.  **RF08: Gestión de Cancelaciones:** El sistema debe permitir al paciente cancelar o reprogramar citas con facilidad para liberar espacios. [Inferencia de `doctora.md` para mitigar huecos]

## No Funcionales (NFR)
1.  **RNF01: Accesibilidad:** El método de agendamiento debe ser sencillo para adultos mayores. [Inferencia basada en perfil de `paciente.md`]
2.  **RNF02: Disponibilidad 24/7:** El canal de agendamiento debe estar disponible fuera del horario de oficina de la clínica. [Fuente: `paciente.md`]
3.  **RNF03: Seguridad de Datos:** El acceso remoto a la agenda médica debe estar debidamente autenticado. [Inferencia técnica de `RF05`]
