# ADR 002: Patrón de Integración para Servicios de IA en Observabilidad

Estado: Propuesto
Fecha: 2024-05-20

## Contexto

La plataforma de e-commerce requiere integrar un servicio de IA para observabilidad que:

- **Procesar datos en tiempo real**: métricas de rendimiento (latencia, errores) y logs deben analizarse con una latencia máxima de 2 segundos desde su generación.
- **Escalar horizontalmente**: el patrón debe soportar el crecimiento del tráfico (50,000 solicitudes/segundo) sin cuellos de botella.
- **Mantener consistencia eventual**: las alertas generadas deben reflejar el estado más reciente de los datos, incluso bajo alta carga.
- **Integración con herramientas existentes**: CloudWatch (logs), Prometheus (métricas) y Grafana (dashboards).

Actualmente, los datos se recolectan mediante agentes en cada servicio y se envían a CloudWatch y Prometheus. El servicio de IA debe consumir estos datos, analizarlos y generar alertas.

## Fuerzas

1. **Latencia vs. Consistencia**: Un patrón basado en colas (ej. SQS, Kafka) introduce latencia adicional (50-200ms) pero garantiza consistencia eventual. Un patrón síncrono (ej. sidecar) reduce la latencia (<10ms) pero puede saturar los servicios bajo alta carga.

2. **Escalabilidad vs. Complejidad**: Un pipeline de eventos (ej. Kinesis + Lambda) escala horizontalmente pero requiere configuración adicional para manejar fallos y reintentos. Un sidecar simplifica la arquitectura pero limita la escalabilidad a la capacidad de cada instancia.

3. **Costo Operativo**: Un pipeline de eventos requiere gestión de infraestructura (Kinesis, Lambda, SQS) y monitoreo adicional. Un sidecar reduce la infraestructura pero aumenta el consumo de recursos en cada instancia.

4. **Tolerancia a Fallos**: Un pipeline de eventos permite reintentos y manejo de fallos a nivel de infraestructura. Un sidecar depende de la disponibilidad del servicio de IA y de la instancia donde se ejecuta.

5. **Integración con Ecosistema**: La plataforma ya utiliza Kinesis para streaming de datos, lo que facilita la adopción de un pipeline de eventos. Un sidecar requeriría cambios en la arquitectura de despliegue.

## Opciones consideradas
> Preguntas guía:
> - ¿Qué patrones de integración evaluarías para este caso? Considera latencia, escalabilidad, tolerancia a fallos y costo.
> - ¿Cómo impacta cada patrón en los ASRs (latencia, escalabilidad, consistencia)?
> - ¿Qué pros y contras identificas en cada opción frente a los requisitos del caso?


## Decision
> Preguntas guía:
> - ¿Qué patrón elegirías y con qué criterios medibles?
> - ¿Cómo justificarías tu elección frente a los trade-offs identificados?


## Consecuencias
> Preguntas guía:
> - ¿Qué impacto tendrá tu decisión en los ASRs (latencia, escalabilidad, consistencia)?
> - ¿Qué riesgos identificas y cómo los mitigarías?
> - ¿Cómo validarías que el patrón cumple con los SLOs definidos?