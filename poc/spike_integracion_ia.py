"""
Spike para validar la integración con un servicio de IA que detecta anomalías 
en métricas de observabilidad de una plataforma de e-commerce.

El código simula la llamada a un servicio externo (ej: AWS SageMaker, Google Vertex AI)
y procesa la respuesta para detectar posibles anomalías. El candidato debe completar:
- Lógica de validación de umbrales.
- Integración con sistemas de persistencia (ej: CloudWatch, Prometheus).
- Mecanismos de alerta proactiva.
"""

import os
import json
import logging
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde .env
load_dotenv()

class AnomalyDetectionService:
    """Cliente para interactuar con el servicio de detección de anomalías."""

    def __init__(self):
        self.service_url = os.getenv("IA_SERVICE_URL")
        self.timeout = int(os.getenv("REQUEST_TIMEOUT", 5))
        self.anomaly_threshold = float(os.getenv("ANOMALY_THRESHOLD", 0.75))
        
        if not self.service_url:
            raise ValueError("La variable de entorno IA_SERVICE_URL no está configurada.")

    def detect_anomaly(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía métricas al servicio de IA y recibe un puntaje de anomalía.
        
        Args:
            metrics: Diccionario con métricas de observabilidad (ej: {"latency": 120, "error_rate": 0.05}).
            
        Returns:
            Diccionario con la respuesta del servicio (ej: {"anomaly_score": 0.85}).
            
        Raises:
            requests.exceptions.RequestException: Si hay un error en la llamada al servicio.
        """
        try:
            logger.info(f"Datos enviados al servicio de IA: {json.dumps(metrics)}")
            
            response = requests.post(
                self.service_url,
                json=metrics,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            logger.info(f"Respuesta del servicio de IA: {json.dumps(result)}")
            return result
            
        except requests.exceptions.Timeout:
            logger.error("Timeout al llamar al servicio de IA")
            raise
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Error de conexión al servicio de IA: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al llamar al servicio de IA: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Respuesta inválida del servicio de IA: {e}")
            raise ValueError("Respuesta no es un JSON válido")

    def is_anomaly(self, anomaly_score: float) -> bool:
        """
        Determina si el puntaje de anomalía supera el umbral configurado.
        
        Args:
            anomaly_score: Puntaje de anomalía recibido del servicio (ej: 0.85).
            
        Returns:
            True si el puntaje supera el umbral, False en caso contrario.
            
        Nota:
            El candidato debe implementar la lógica de validación según los requisitos
            del sistema (ej: usar umbrales dinámicos, considerar métricas adicionales).
        """
        # TODO: Implementar lógica de validación de umbrales.
        # Pregunta guía: ¿Cómo ajustarías este umbral dinámicamente en función de
        # la hora del día o el tráfico histórico?
        return anomaly_score >= self.anomaly_threshold


def simulate_metrics() -> Dict[str, Any]:
    """
    Simula métricas de observabilidad de la plataforma de e-commerce.
    
    Returns:
        Diccionario con métricas como latencia, tasa de errores y throughput.
    """
    return {
        "latency": 120,  # ms
        "error_rate": 0.05,  # % de errores
        "throughput": 45000,  # solicitudes/segundo
        "timestamp": "2024-05-20T15:30:00Z"
    }


def main():
    """Punto de entrada del spike."""
    try:
        # Inicializar el cliente del servicio de IA
        service = AnomalyDetectionService()
        
        # Obtener métricas simuladas
        metrics = simulate_metrics()
        
        # Detectar anomalías
        result = service.detect_anomaly(metrics)
        
        # Validar si es una anomalía
        if "anomaly_score" not in result:
            logger.error("La respuesta del servicio no contiene 'anomaly_score'")
            return
            
        if service.is_anomaly(result["anomaly_score"]):
            logger.warning(
                f"Posible anomalía detectada. Puntaje: {result['anomaly_score']} "
                f"(umbral: {service.anomaly_threshold})"
            )
            # TODO: Integrar con sistema de alertas (ej: Slack, PagerDuty)
            # TODO: Persistir el resultado en un sistema de observabilidad (ej: CloudWatch)
        else:
            logger.info("No se detectaron anomalías.")
            
    except Exception as e:
        logger.error(f"Error en el spike: {e}")
        raise


if __name__ == "__main__":
    main()