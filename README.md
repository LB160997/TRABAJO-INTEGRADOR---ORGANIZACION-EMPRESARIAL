# Chatbot de Gestión de Vacaciones

## Descripción

Proyecto desarrollado para la materia Organización Empresarial.

El sistema permite automatizar la gestión de solicitudes de vacaciones mediante un chatbot desarrollado en Python.

## Funcionalidades

- Validación de legajo.
- Consulta de días disponibles.
- Solicitud de vacaciones.
- Registro automático de solicitudes.
- Actualización de saldo de días.
- Persistencia mediante Excel.

## Tecnologías utilizadas

- Python
- Pandas
- OpenPyXL
- Excel
- BPMN 2.0

## Estructura de datos

BaseDatosVacaciones.xlsx

### Hoja Empleados

- Legajo
- Nombre
- DiasDisponibles

### Hoja Solicitudes

- ID
- Legajo
- DiasSolicitados
- Estado

## Ejecución

```bash
python chatbot.py
