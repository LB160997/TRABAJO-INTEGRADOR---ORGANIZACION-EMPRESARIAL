# Chatbot de Gestión de Vacaciones

## Trabajo Práctico Integrador - Organización Empresarial

### Tecnicatura Universitaria en Programación a Distancia (TUPaD)

---

## Descripción del Proyecto

Este proyecto fue desarrollado en el marco de la materia **Organización Empresarial** y tiene como objetivo automatizar el proceso administrativo de **gestión de vacaciones de empleados** mediante un chatbot.

La solución propuesta modela el proceso utilizando **BPMN 2.0** y lo implementa mediante una aplicación desarrollada en Python que interactúa con una base de datos simulada en Excel.

El chatbot permite:

* Validar el número de legajo del empleado.
* Consultar los días de vacaciones disponibles.
* Solicitar días de vacaciones.
* Validar reglas de negocio.
* Registrar solicitudes aprobadas y rechazadas.
* Actualizar automáticamente el saldo de días disponibles.

---

## Objetivo

Automatizar un proceso administrativo mediante un chatbot, garantizando la coherencia entre el modelo BPMN diseñado y la lógica implementada en el código.

---

## Tecnologías Utilizadas

* Python 3
* Pandas
* OpenPyXL
* Microsoft Excel
* BPMN 2.0
* GitHub

---

## Estructura del Proyecto

```text
TP-Organizacion-Empresarial/
│
├── chatbot.py
├── BaseDatosVacaciones.xlsx
├── README.md
│
└── docs/
    ├── Manual_Usuario_Sistema_Vacaciones.pdf
    ├── TPI-ORGANIZACION EMPRESARIAL.pdf
    └── USO DE HERRAMIENTAS DE INTELIGENCIA ARTIFICIAL.pdf
```

---

## Base de Datos

El sistema utiliza un archivo Excel denominado:

```text
BaseDatosVacaciones.xlsx
```

El archivo contiene dos hojas:

### Hoja: Empleados

| Campo           | Descripción                       |
| --------------- | --------------------------------- |
| Legajo          | Número identificador del empleado |
| Nombre          | Nombre completo                   |
| DiasDisponibles | Días de vacaciones disponibles    |

### Hoja: Solicitudes

| Campo           | Descripción                   |
| --------------- | ----------------------------- |
| ID              | Identificador de la solicitud |
| Legajo          | Legajo del empleado           |
| DiasSolicitados | Cantidad de días solicitados  |
| Estado          | Aprobada o Rechazada          |

---

## Requisitos Previos

Antes de ejecutar el proyecto es necesario tener instalado:

* Python 3.10 o superior
* Pip (gestor de paquetes de Python)

Verificar instalación:

```bash
python --version
```

---

## Instalación

### 1. Descargar el proyecto

Descargar o clonar este repositorio en una carpeta local.

### 2. Verificar la instalación de Python

Abrir una terminal y ejecutar:

```bash
python --version
```

Si Python está instalado correctamente, se mostrará la versión instalada.

### 3. Instalar las dependencias necesarias

Desde una terminal, ejecutar:

```bash
pip install pandas openpyxl
```

### 4. Verificar los archivos del proyecto

Asegurarse de que los siguientes archivos se encuentren en la misma carpeta:

```text
chatbot.py
BaseDatosVacaciones.xlsx
```

### 5. Ejecutar el chatbot

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python chatbot.py
```

El sistema iniciará el chatbot y solicitará el número de legajo del empleado para comenzar el proceso de gestión de vacaciones.

---

## Configuración

Verificar que el archivo:

```text
BaseDatosVacaciones.xlsx
```

se encuentre en la misma carpeta que:

```text
chatbot.py
```

---

## Ejecución

Para iniciar el chatbot ejecutar:

```bash
python chatbot.py
```

---

## Ejemplo de Uso

```text
===================================
 SISTEMA DE GESTIÓN DE VACACIONES
===================================

Ingrese su número de legajo:
1001

Empleado: Juan Pérez
Días disponibles: 15

Ingrese cantidad de días a solicitar:
5

Solicitud APROBADA

Solicitud registrada correctamente.
Proceso finalizado.
```

---

## Reglas de Negocio

El sistema implementa las siguientes validaciones:

1. El legajo debe existir en la base de datos.
2. La cantidad de días solicitados debe ser mayor a cero.
3. El empleado debe disponer de suficientes días para aprobar la solicitud.
4. Todas las solicitudes quedan registradas en la base de datos.
5. Las solicitudes aprobadas actualizan automáticamente el saldo disponible.

---

## BPMN Implementado

El proyecto incluye:

* Modelo AS-IS (proceso actual).
* Modelo TO-BE (proceso automatizado).
* Carriles de Usuario y Sistema.
* Eventos de inicio y fin.
* Gateways de decisión:

  * Validación de legajo.
  * Validación de disponibilidad de días.

---

## Documentación

La documentación del proyecto se encuentra en la carpeta:

```text
docs/
```

Incluye:

* Informe Final.
* Diagramas BPMN.
* Manual de Usuario.
* Evidencias del uso de Inteligencia Artificial.
* Capturas de pruebas de funcionamiento.

---

## Autor

Nicola Garda--Comision 16

Lucia Boyer--Comision 16

Tecnicatura Universitaria en Programación a Distancia (TUPaD)

##

