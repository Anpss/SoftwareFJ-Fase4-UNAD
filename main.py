# Script de prueba inicial para validar la arquitectura base y la clase Cliente.
from modelos.cliente import Cliente  # Importa la clase Cliente.
from utilidades.excepciones import ErrorSistemaFJ  # Importa la excepción base del sistema.
from utilidades.logger import GestorLogs  # Importa el registrador de logs.


def probar_modulo_base():
    """Ejecuta casos válidos e inválidos de clientes para comprobar estabilidad y logs."""
    print("=== INICIANDO PRUEBAS DE ARQUITECTURA BASE (ESTUDIANTE 1) ===\n")

    # Caso 1: Registro válido de un cliente.
    try:
        cliente1 = Cliente("CLI-001", "ana maria gomez", "ana.gomez@correo.com", "3001234567")
        print("[OK] Cliente creado:", cliente1.obtener_resumen())
    except ErrorSistemaFJ as error:
        GestorLogs.registrar_evento("ERROR", "MainPrueba", str(error))
        print("[ERROR CONTROLADO]:", error)

    # Caso 2: Registro inválido por correo mal formado (debe capturar error y seguir ejecutando).
    try:
        cliente_invalido = Cliente("CLI-002", "Carlos Ruiz", "correo-sin-arroba.com", "3109876543")
    except ErrorSistemaFJ as error:
        GestorLogs.registrar_evento("ERROR", "MainPrueba", str(error))
        print("[ERROR CONTROLADO]:", error)

    # Caso 3: Registro inválido por teléfono corto.
    try:
        cliente_tel_malo = Cliente("CLI-003", "Luis Perez", "luis@empresa.co", "123")
    except ErrorSistemaFJ as error:
        GestorLogs.registrar_evento("ERROR", "MainPrueba", str(error))
        print("[ERROR CONTROLADO]:", error)

    print("\n=== PRUEBAS FINALIZADAS SIN INTERRUPCIONES (Revisa logs/sistema.log) ===")


if __name__ == "__main__":
    probar_modulo_base()