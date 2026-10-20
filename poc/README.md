# Spike de Integración con Servicios de IA para Observabilidad

Este spike valida la integración básica con un servicio de IA para detección de anomalías en métricas de observabilidad de una plataforma de e-commerce. El código actual simula la llamada a un servicio externo (ej: AWS SageMaker, Google Vertex AI o un endpoint propio) que analiza patrones de tráfico para detectar anomalías.

## Contexto
La plataforma de e-commerce maneja **50,000 solicitudes por segundo** en hora pico. El spike demuestra:
1. **Integración con un servicio de IA**: Llamada a una API externa (simulada) para detección de anomalías en métricas como latencia, tasa de errores y throughput.
2. **Manejo de errores**: Gestión de fallos en la conexión, timeouts y respuestas inválidas del servicio.
3. **Configuración dinámica**: Uso de variables de entorno para parámetros críticos (URL del servicio, umbrales de alerta).

## ¿Qué debes completar?
El spike actual **no implementa la lógica de negocio real** para:
- **Validar umbrales de anomalías**: El servicio de IA retorna un puntaje (ej: `0.85`), pero el código no decide si es una anomalía.
- **Persistencia de resultados**: Los resultados de la detección no se guardan en un sistema de observabilidad (ej: CloudWatch, Prometheus).
- **Alertas proactivas**: No se notifica a los equipos cuando se detecta una anomalía.

## Instrucciones de ejecución
1. **Requisitos previos**:
   - Python 3.12+.
   - Dependencias instaladas: `pip install -r requirements.txt`.

2. **Configuración**:
   - Crea un archivo `.env` en la carpeta `poc/` con las siguientes variables:
     ```
     # URL del endpoint del servicio de IA (simulado o real)
     IA_SERVICE_URL=http://localhost:8000/detect-anomalies
     
     # Umbral de puntuación para considerar una anomalía (ej: 0.75)
     ANOMALY_THRESHOLD=0.75
     
     # Tiempo máximo de espera para la respuesta del servicio (en segundos)
     REQUEST_TIMEOUT=5
     ```

3. **Ejecutar el spike**:
   ```bash
   cd poc/
   python spike_integracion_ia.py
   ```

4. **Salida esperada**:
   - Si la llamada al servicio es exitosa:
     ```
     [INFO] Datos enviados al servicio de IA: {"latency": 120, "error_rate": 0.05, "throughput": 45000}
     [INFO] Respuesta del servicio de IA: {"anomaly_score": 0.85}
     [WARNING] Posible anomalía detectada. Puntaje: 0.85 (umbral: 0.75)
     ```
   - Si el servicio falla:
     ```
     [ERROR] Error al llamar al servicio de IA: ConnectionError(...)
     ```

## Validaciones clave
- **Conectividad**: El spike debe fallar si la URL del servicio es inaccesible o el timeout se excede.
- **Manejo de respuestas**: Debe procesar correctamente respuestas con formato inválido (ej: JSON malformado).
- **Configuración**: Debe leer las variables de entorno y fallar si no están definidas.

## Limitaciones del spike
- **Servicio simulado**: El endpoint `http://localhost:8000/detect-anomalies` no existe. Para probar con un servicio real, reemplaza la URL en `.env`.
- **Datos hardcodeados**: Las métricas enviadas (`latency`, `error_rate`, `throughput`) son estáticas. En un entorno real, se obtendrían de un sistema de monitoreo.
- **Sin persistencia**: Los resultados no se guardan en una base de datos o sistema de logs.

## Preguntas guía para el candidato
1. ¿Cómo integrarías este spike con un sistema de observabilidad existente (ej: Prometheus, CloudWatch)?
2. ¿Qué estrategias usarías para escalar la detección de anomalías en un entorno con 50,000 TPS?
3. ¿Cómo garantizarías la resiliencia del servicio de IA ante fallos (ej: circuit breaker, retries)?
4. ¿Qué métricas adicionales incluirías para mejorar la precisión de la detección de anomalías?

---
*Nota: Este spike es autocontenido. No importa módulos fuera de `poc/`.*