# 📖 Glosario - Semana 14

## A

### API Gateway
Punto de entrada único para todas las solicitudes a una API. Maneja autenticación, rate limiting, logging y routing.

### ASVS (Application Security Verification Standard)
Estándar de OWASP que define requisitos de seguridad para aplicaciones web organizados en niveles.

---

## B

### Bucket (Rate Limiting)
Contenedor abstracto que almacena "tokens" en algoritmos de rate limiting. Cuando está vacío, las solicitudes se rechazan.

### Brute Force Attack
Ataque que intenta múltiples combinaciones de credenciales hasta encontrar la correcta. Se mitiga con rate limiting.

---

## C

### Cardinality (Metrics)
Número de combinaciones únicas de labels en una métrica. Alta cardinalidad puede causar problemas de rendimiento en Prometheus.

### Content Security Policy (CSP)
Header HTTP que define qué recursos puede cargar una página web, previniendo XSS y data injection.

### CORS (Cross-Origin Resource Sharing)
Mecanismo que permite a servidores indicar qué orígenes pueden acceder a sus recursos.

### Counter (Prometheus)
Tipo de métrica que solo puede incrementar. Ideal para contar eventos (requests, errores).

---

## D

### Degraded (Health Status)
Estado de salud que indica que el servicio funciona pero con capacidad reducida.

### DDoS (Distributed Denial of Service)
Ataque que intenta saturar un servicio con solicitudes desde múltiples fuentes.

---

## E

### Exponential Backoff
Estrategia donde el tiempo de espera entre reintentos aumenta exponencialmente.

---

## F

### Fixed Window (Rate Limiting)
Algoritmo que cuenta solicitudes en ventanas de tiempo fijas (ej: 00:00-00:59, 01:00-01:59).

---

## G

### Gauge (Prometheus)
Tipo de métrica que puede subir y bajar. Ideal para valores actuales (usuarios conectados, temperatura).

### Grafana
Plataforma de visualización que consume datos de Prometheus y otras fuentes para crear dashboards.

---

## H

### Health Check
Endpoint que verifica el estado de un servicio y sus dependencias.

### Histogram (Prometheus)
Tipo de métrica que mide distribución de valores en buckets predefinidos. Ideal para latencias.

### HSTS (HTTP Strict Transport Security)
Header que fuerza al navegador a usar HTTPS para todas las conexiones futuras.

---

## I

### Instrumentation
Proceso de añadir código para recolectar métricas, logs y traces de una aplicación.

---

## J

### JSON Logging
Formato de logs estructurado donde cada entrada es un objeto JSON, facilitando parsing y análisis.

---

## K

### Key Function (Rate Limiting)
Función que determina cómo identificar clientes para aplicar límites (IP, user ID, API key).

---

## L

### Leaky Bucket
Algoritmo de rate limiting que procesa solicitudes a tasa constante, como agua saliendo de un balde con agujero.

### Liveness Probe
Health check de Kubernetes que verifica si el contenedor está corriendo. Si falla, se reinicia.

### Log Level
Severidad de un mensaje de log: DEBUG, INFO, WARNING, ERROR, CRITICAL.

---

## M

### Metric
Valor numérico que representa el estado o comportamiento de un sistema en el tiempo.

### Middleware
Componente que procesa requests/responses entre el cliente y los handlers de la aplicación.

### Moving Window (Rate Limiting)
Algoritmo que usa ventana deslizante en lugar de fija, proporcionando límites más suaves.

---

## N

### nosniff (X-Content-Type-Options)
Valor del header que previene que navegadores adivinen el tipo MIME del contenido.

---

## O

### Observability
Capacidad de entender el estado interno de un sistema basándose en sus outputs (logs, metrics, traces).

### OWASP
Open Web Application Security Project - organización que produce guías y herramientas de seguridad.

---

## P

### Preflight Request
Solicitud OPTIONS que navegadores envían antes de requests cross-origin para verificar permisos CORS.

### Processor (structlog)
Función que transforma eventos de log antes de su output (añadir timestamp, formatear, etc.).

### PromQL
Lenguaje de consulta de Prometheus para seleccionar y agregar datos de series temporales.

---

## Q

### Quantile
Valor por debajo del cual cae un porcentaje dado de observaciones. P99 = valor por debajo del 99%.

---

## R

### Rate Limiting
Técnica para controlar la cantidad de solicitudes que un cliente puede hacer en un período de tiempo.

### Readiness Probe
Health check de Kubernetes que verifica si el servicio puede recibir tráfico.

### RED Method
Metodología de monitoreo: Rate (requests/s), Errors (rate de errores), Duration (latencia).

### Request ID
Identificador único asignado a cada request para trazabilidad a través de logs y servicios.

### Retry-After
Header HTTP que indica cuántos segundos esperar antes de reintentar tras un 429.

---

## S

### Scrape (Prometheus)
Proceso donde Prometheus recolecta métricas de endpoints /metrics de aplicaciones.

### Security Headers
Headers HTTP que mejoran la seguridad de aplicaciones web (CSP, HSTS, X-Frame-Options, etc.).

### Sliding Window
Ver "Moving Window".

### SLI (Service Level Indicator)
Métrica que mide un aspecto del nivel de servicio (latencia, disponibilidad, error rate).

### SLO (Service Level Objective)
Objetivo para un SLI (ej: 99.9% de requests con latencia < 200ms).

### Startup Probe
Health check de Kubernetes para aplicaciones con inicialización lenta.

### structlog
Biblioteca Python para logging estructurado con soporte para procesadores y diferentes outputs.

### Summary (Prometheus)
Tipo de métrica similar a Histogram pero calcula quantiles en el cliente.

---

## T

### Three Pillars of Observability
Logs, Metrics y Traces - las tres fuentes principales de datos de observabilidad.

### Throttling
Limitación activa de tasa de procesamiento. Similar a rate limiting pero enfocado en el servidor.

### Token Bucket
Algoritmo de rate limiting donde tokens se añaden a un bucket a tasa fija y cada request consume un token.

### Trace
Registro del camino de una solicitud a través de múltiples servicios.

---

## U

### USE Method
Metodología de monitoreo: Utilization, Saturation, Errors - para recursos del sistema.

---

## W

### Window (Rate Limiting)
Período de tiempo en el que se cuentan las solicitudes para aplicar límites.

---

## X

### X-Content-Type-Options
Header de seguridad que previene MIME-type sniffing.

### X-Frame-Options
Header que controla si la página puede mostrarse en iframes (previene clickjacking).

### X-RateLimit Headers
Headers que informan al cliente sobre límites de rate (Limit, Remaining, Reset).

### X-Request-ID
Header que contiene el identificador único del request para trazabilidad.

### X-XSS-Protection
Header que activa el filtro XSS del navegador (legacy, reemplazado por CSP).

---

## 📊 Referencia Rápida

| Término | Categoría | Definición Corta |
|---------|-----------|------------------|
| Counter | Metrics | Valor que solo sube |
| Gauge | Metrics | Valor que sube y baja |
| Histogram | Metrics | Distribución en buckets |
| Liveness | Health | ¿Está corriendo? |
| Readiness | Health | ¿Puede recibir tráfico? |
| Token Bucket | Rate Limit | Tokens a tasa fija |
| Fixed Window | Rate Limit | Ventanas de tiempo fijas |
| CSP | Security | Política de contenido |
| HSTS | Security | Forzar HTTPS |
