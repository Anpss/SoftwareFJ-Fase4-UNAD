# Módulo que define la clase abstracta base para todas las entidades de Software FJ.
from abc import ABC, abstractmethod  # Importa ABC y el decorador abstractmethod para crear clases abstractas.
from datetime import datetime  # Importa datetime para registrar la fecha de creación de cada objeto.
from utilidades.excepciones import ErrorValidacionDatos  # Importa la excepción de validación personalizada.


class EntidadSistema(ABC):
    """Clase abstracta que representa cualquier entidad general del sistema."""

    # Constructor base que exige un identificador único para toda entidad.
    def __init__(self, id_entidad: str):
        # Valida que el identificador no esté vacío ni sea solo espacios en blanco.
        if not id_entidad or not isinstance(id_entidad, str) or not id_entidad.strip():
            # Lanza excepción personalizada si el ID es inválido.
            raise ErrorValidacionDatos("id_entidad", "El identificador no puede estar vacío.")
        # Asigna el identificador limpio de espacios en un atributo protegido.
        self._id_entidad = id_entidad.strip()
        # Registra automáticamente la fecha y hora en que se instanció la entidad.
        self._fecha_creacion = datetime.now()

    @property
    def id_entidad(self) -> str:
        """Getter encapsulado para consultar el identificador de la entidad."""
        # Retorna el valor del atributo protegido _id_entidad.
        return self._id_entidad

    @property
    def fecha_creacion(self) -> datetime:
        """Getter encapsulado para consultar la fecha de creación de la entidad."""
        # Retorna la marca de tiempo de creación.
        return self._fecha_creacion

    @abstractmethod
    def validar_integridad(self) -> bool:
        """Método abstracto que obliga a las clases hijas a validar sus propios datos."""
        pass

    @abstractmethod
    def obtener_resumen(self) -> str:
        """Método abstracto polimórfico para representar la entidad en formato texto."""
        pass