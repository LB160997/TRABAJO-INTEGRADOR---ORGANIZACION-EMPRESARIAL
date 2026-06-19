import pandas as pd

ARCHIVO_EXCEL = "BaseDatosVacaciones.xlsx"

# ==========================
# FUNCIONES DE VALIDACIÓN
# ==========================

# Valida que el usuario ingrese un número entero.
def validar_numero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("❌ Error: debe ingresar un número válido.")


# Valida que la cantidad de días sea un número dentro de un rango permitido.
def validar_dias(mensaje):
    while True:
        valor = input(mensaje).strip()

        if not valor.isdigit():
            print("❌ Error: debe ingresar un número válido.")
            continue

        valor = int(valor)

        if valor <= 0:
            print("❌ Error: debe ser mayor a 0.")
        elif valor > 365:
            print("❌ Error: cantidad demasiado alta.")
        else:
            return valor


# ==========================
# CARGAR EXCEL
# ==========================

# Carga las hojas de empleados y solicitudes desde el archivo Excel.
try:
    empleados_df = pd.read_excel(ARCHIVO_EXCEL, sheet_name="Empleados")
    solicitudes_df = pd.read_excel(ARCHIVO_EXCEL, sheet_name="Solicitudes")
except Exception as e:
    print("❌ Error al leer el Excel:", e)
    exit()

# ==========================
# LIMPIEZA COLUMNAS
# ==========================

# Elimina espacios en blanco de los nombres de columnas.
empleados_df.columns = empleados_df.columns.str.strip()
solicitudes_df.columns = solicitudes_df.columns.str.strip()

# ==========================
# VALIDAR COLUMNAS
# ==========================

# Verifica que existan las columnas necesarias en cada hoja.
if not {"Legajo", "Nombre", "DiasDisponibles"}.issubset(empleados_df.columns):
    print(empleados_df.columns)
    exit()

if not {"ID", "Legajo", "DiasSolicitados", "Estado"}.issubset(solicitudes_df.columns):
    print(solicitudes_df.columns)
    exit()

# ==========================
# TÍTULO
# ==========================

# Muestra la cabecera del sistema.
print("\n===================================")
print(" SISTEMA DE GESTIÓN DE VACACIONES ")
print("===================================\n")

# ==========================
# LEGAJO (CON REINTENTO)
# ==========================

# Solicita el legajo y verifica que exista en la base de datos.
while True:

    legajo = validar_numero("Ingrese su número de legajo: ")

    empleado = empleados_df[empleados_df["Legajo"] == legajo]

    if empleado.empty:
        print("\n❌ Empleado no registrado.")

        opcion = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()

        if opcion in ["n", "no"]:
            print("👋 Programa finalizado.")
            exit()

        continue

    break

# ==========================
# DATOS EMPLEADO
# ==========================

# Obtiene los datos del empleado encontrado.
nombre = empleado.iloc[0]["Nombre"]

try:
    dias_disponibles = int(empleado.iloc[0]["DiasDisponibles"])
except:
    exit()

print(f"\n👤 Empleado: {nombre}")
print(f"📅 Días disponibles: {dias_disponibles}")

# ==========================
# SOLICITUD DE DÍAS
# ==========================

# Solicita la cantidad de días de vacaciones requeridos.
dias_solicitados = validar_dias("Ingrese cantidad de días a solicitar: ")

# ==========================
# DECISIÓN
# ==========================

# Evalúa si la solicitud puede aprobarse según el saldo disponible.
if dias_solicitados <= dias_disponibles:
    estado = "Aprobada"
    print("\n✅ Solicitud APROBADA")

    empleados_df.loc[
        empleados_df["Legajo"] == legajo,
        "DiasDisponibles"
    ] = dias_disponibles - dias_solicitados

else:
    estado = "Rechazada"
    print("\n❌ Solicitud RECHAZADA")
    print("Motivo: saldo insuficiente")

# ==========================
# NUEVA SOLICITUD
# ==========================

# Genera un nuevo registro y lo agrega al historial de solicitudes.
nuevo_id = int(solicitudes_df["ID"].max()) + 1 if not solicitudes_df.empty else 1

nueva_solicitud = pd.DataFrame([{
    "ID": nuevo_id,
    "Legajo": legajo,
    "DiasSolicitados": dias_solicitados,
    "Estado": estado
}])

solicitudes_df = pd.concat(
    [solicitudes_df, nueva_solicitud],
    ignore_index=True
)

# ==========================
# GUARDAR EXCEL
# ==========================

# Guarda los cambios realizados en ambas hojas del archivo Excel.
try:
    with pd.ExcelWriter(ARCHIVO_EXCEL, engine="openpyxl") as writer:
        empleados_df.to_excel(writer, sheet_name="Empleados", index=False)
        solicitudes_df.to_excel(writer, sheet_name="Solicitudes", index=False)

    print("\n💾 Datos guardados correctamente.")
    print("🏁 Proceso finalizado.")

except Exception as e:
    print("❌ Error al guardar el Excel:", e)