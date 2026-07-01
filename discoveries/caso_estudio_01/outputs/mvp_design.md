# MVP Design: Automated WhatsApp Reminders (Caso de Estudio 01)

## Goal
Validate if automated reminders reduce no-shows and receptionist workload with minimal technical effort.

## Core Features (The "Minimum")
1.  **Manual Trigger:** A simple button or script that reads a list of patients for the next day.
2.  **WhatsApp Integration:** Use a low-code tool (like Twilio or a simple WhatsApp API wrapper) to send a templated message.
3.  **Confirmation Loop:** Patients can reply "YES" to confirm.

## Success Metrics
- **No-show Rate:** Reduction of at least 20% compared to the previous month.
- **Time Saved:** Receptionist spends less than 15 minutes managing reminders (down from 90 minutes).
- **Patient Satisfaction:** At least 5 patients mention the convenience of the WhatsApp reminder.

## Implementation Plan (1-Week Sprint)
- **Day 1-2:** Clean up the existing Excel "Agenda" to have a consistent format (Name, Phone, Time).
- **Day 3:** Set up a simple Python script to send messages using a template.
- **Day 4:** Test with 5 "friendly" patients.
- **Day 5:** Full rollout for one day of appointments.

## Low-Fidelity Mockup (Text-based)
> "Hola [Nombre], te recordamos tu cita con la Dra. en la Clínica Médica mañana a las [Hora]. ¿Confirmas tu asistencia? Responde SI para confirmar o llama al [Teléfono] para reprogramar."
