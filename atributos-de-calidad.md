# Atributos de Calidad para Observabilidad con IA

## Requisitos Arquitectónicamente Significativos (ASRs)

| ID | ASR | Valor Medible | Métrica | Umbral |
|----|-----|---------------|---------|--------|
| ASR-01 | Detección automática de anomalías | Reducir falsos positivos | Precisión de alertas | ≥ 95% |
| ASR-02 | Latencia de detección de incidentes | Tiempo desde evento hasta alerta | Tiempo medio de detección (MTTD) | ≤ 2 minutos |
| ASR-03 | Escalabilidad del procesamiento | Volumen de datos procesados en tiempo real | Throughput de logs/métricas | 1.5 TB/día sin degradación |
| ASR-04 | Insights predictivos | Predecir incidentes antes de que ocurran | Precisión de predicción | ≥ 85% |
| ASR-05 | Integración con stack existente | Compatibilidad con herramientas actuales | Tiempo de integración | ≤ 4 semanas |
| ASR-06 | Costo operativo | Reducir costos de observabilidad | Costo mensual por TB procesado | ≤ $500/TB |

## Escenarios de Calidad (ISO 25010)

Los escenarios de calidad describen cómo el sistema debe responder a estímulos específicos bajo condiciones definidas. Completa la tabla siguiente para cada ASR:

| ID | Fuente | Estímulo | Artefacto | Entorno | Respuesta | Medida |
|----|--------|----------|-----------|---------|-----------|--------|
| **ASR-01** | <br>¿Quién o qué genera el estímulo? (ej. usuario, sistema externo, sensor) | <br>¿Qué evento desencadena el escenario? (ej. aumento repentino de latencia, error 500) | <br>¿Qué componente o sistema se ve afectado? | <br>¿En qué condiciones ocurre el escenario? (ej. hora pico, despliegue multi-región) | <br>¿Cómo debe responder el sistema? (ej. enviar alerta, escalar recursos) | <br>¿Cómo se mide el éxito? (ej. tiempo de respuesta, tasa de errores) |
|    |        |          |           |         |           |        |
| **ASR-02** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-03** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-04** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-05** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-06** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |

### Preguntas Guía para Completar los Escenarios
1. **Fuente:**
   - ¿Qué actores (humanos o sistemas) interactúan con el sistema en este escenario?
   - ¿Qué eventos externos podrían desencadenar este escenario? (ej. pico de tráfico, fallo de red)

2. **Estímulo:**
   - ¿Qué condición específica debe ocurrir para que el sistema reaccione? (ej. latencia > 100ms, error 4xx en 5% de solicitudes)
   - ¿Cómo se manifiesta el estímulo en términos de logs, métricas o traces?

3. **Artefacto:**
   - ¿Qué componente del sistema es responsable de manejar este estímulo? (ej. servicio de detección de anomalías, pipeline de logs)
   - ¿Qué otros componentes podrían verse afectados indirectamente?

4. **Entorno:**
   - ¿En qué condiciones opera el sistema cuando ocurre el estímulo? (ej. modo de alta disponibilidad, durante un despliegue)
   - ¿Qué factores externos podrían influir en la respuesta? (ej. región geográfica, estado de la red)

5. **Respuesta:**
   - ¿Qué acciones debe tomar el sistema para manejar el estímulo? (ej. enviar alerta a Slack, escalar pods de Kubernetes)
   - ¿Qué información debe registrarse para análisis posterior?

6. **Medida:**
   - ¿Cómo se cuantifica el éxito de la respuesta? (ej. tiempo de detección, número de falsos positivos)
   - ¿Qué métricas se utilizan para validar que el sistema cumple con el ASR?

---

## Ejemplo de Escenario Completado (Referencia)

| ID | Fuente | Estímulo | Artefacto | Entorno | Respuesta | Medida |
|----|--------|----------|-----------|---------|-----------|--------|
| ASR-01 | Servicio de monitoreo (CloudWatch) | Aumento repentino de latencia en el servicio de pagos (p99 > 150ms durante 3 minutos) | Servicio de detección de anomalías basado en IA | Hora pico (50,000 TPS), despliegue multi-región | El servicio de IA analiza patrones históricos y envía una alerta prioritaria al equipo de operaciones con contexto del incidente | Precisión de la alerta ≥ 95% (falsos positivos < 5%) |

---

## Priorización de Atributos de Calidad
Los ASRs deben priorizarse según su impacto en el negocio y su viabilidad técnica. Completa la siguiente matriz de priorización:

| ASR | Impacto en el Negocio (1-5) | Viabilidad Técnica (1-5) | Prioridad (Impacto × Viabilidad) |
|-----|-----------------------------|--------------------------|-----------------------------------|
| ASR-01 |                             |                          |                                   |
| ASR-02 |                             |                          |                                   |
| ASR-03 |                             |                          |                                   |
| ASR-04 |                             |                          |                                   |
| ASR-05 |                             |                          |                                   |
| ASR-06 |                             |                          |                                   |

### Preguntas Guía para Priorización
1. **Impacto en el Negocio:**
   - ¿Qué consecuencias tiene no cumplir con este ASR? (ej. pérdida de ingresos, degradación de UX)
   - ¿Qué equipos o procesos se ven afectados? (ej. operaciones, desarrollo, seguridad)
2. **Viabilidad Técnica:**
   - ¿Qué desafíos técnicos existen para implementar este ASR? (ej. integración con sistemas legacy, costos)
   - ¿Existen soluciones disponibles en el mercado que cumplan con este ASR?
3. **Prioridad:**
   - ¿Qué ASRs deben implementarse primero para maximizar el valor entregado?
   - ¿Qué ASRs pueden abordarse en fases posteriores?

---