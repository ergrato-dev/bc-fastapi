"""
Security Headers Middleware

Middleware personalizado para añadir headers de seguridad a cada respuesta.
"""

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


# ============================================
# PASO 2: Security Headers Middleware
# ============================================
print("--- Middleware: Security Headers ---")


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware que añade headers de seguridad a todas las respuestas.
    
    Headers incluidos:
    - X-Content-Type-Options: Previene MIME type sniffing
    - X-Frame-Options: Previene clickjacking
    - X-XSS-Protection: Filtro XSS del navegador
    - Referrer-Policy: Controla información en Referer header
    - Permissions-Policy: Controla features del navegador
    """
    
    async def dispatch(self, request: Request, call_next) -> Response:
        # Procesar el request
        response = await call_next(request)
        
        # ============================================
        # PASO 2.1: Headers Básicos de Seguridad
        # ============================================
        # Descomenta las siguientes líneas:
        
        # Previene que el navegador intente adivinar el Content-Type
        # response.headers["X-Content-Type-Options"] = "nosniff"
        
        # Previene que la página sea embebida en iframes (clickjacking)
        # response.headers["X-Frame-Options"] = "DENY"
        
        # Activa el filtro XSS del navegador (legacy pero útil)
        # response.headers["X-XSS-Protection"] = "1; mode=block"
        
        # Controla qué información se envía en el header Referer
        # response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        # ============================================
        # PASO 3: Permissions Policy
        # ============================================
        # Descomenta las siguientes líneas:
        
        # Deshabilita features del navegador que no necesitas
        # response.headers["Permissions-Policy"] = (
        #     "geolocation=(), "
        #     "microphone=(), "
        #     "camera=(), "
        #     "payment=(), "
        #     "usb=()"
        # )
        
        # ============================================
        # PASO 4: HSTS (Solo con HTTPS)
        # ============================================
        # Descomenta las siguientes líneas:
        
        # Solo añadir HSTS si la conexión es HTTPS
        # if request.url.scheme == "https":
        #     response.headers["Strict-Transport-Security"] = (
        #         "max-age=31536000; includeSubDomains; preload"
        #     )
        
        # ============================================
        # PASO 5: Content Security Policy (CSP)
        # ============================================
        # Descomenta las siguientes líneas:
        
        # CSP controla qué recursos puede cargar el navegador
        # Ajusta según las necesidades de tu aplicación
        # csp_directives = [
        #     "default-src 'self'",           # Por defecto, solo mismo origen
        #     "script-src 'self'",            # Scripts solo del mismo origen
        #     "style-src 'self' 'unsafe-inline'",  # Estilos (inline para desarrollo)
        #     "img-src 'self' data: https:",  # Imágenes de mismo origen, data URIs, HTTPS
        #     "font-src 'self'",              # Fuentes del mismo origen
        #     "connect-src 'self'",           # Conexiones (fetch, XHR) al mismo origen
        #     "frame-ancestors 'none'",       # No permitir iframes
        #     "base-uri 'self'",              # Restringir <base> tag
        #     "form-action 'self'",           # Forms solo al mismo origen
        # ]
        # response.headers["Content-Security-Policy"] = "; ".join(csp_directives)
        
        # ============================================
        # PASO 6: Cache Control para datos sensibles
        # ============================================
        # Descomenta las siguientes líneas:
        
        # Para endpoints con datos sensibles, prevenir caching
        # if "/api/" in request.url.path:
        #     response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate"
        #     response.headers["Pragma"] = "no-cache"
        #     response.headers["Expires"] = "0"
        
        return response


# ============================================
# Versión alternativa usando la librería 'secure'
# ============================================
# Si prefieres usar la librería secure:
# 
# uv add secure
#
# import secure
# 
# secure_headers = secure.Secure(
#     csp=secure.ContentSecurityPolicy()
#         .default_src("'self'")
#         .script_src("'self'"),
#     hsts=secure.StrictTransportSecurity()
#         .max_age(31536000)
#         .include_subdomains(),
#     referrer=secure.ReferrerPolicy().no_referrer_when_downgrade(),
#     cache=secure.CacheControl().no_store(),
# )
#
# class SecureHeadersMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next) -> Response:
#         response = await call_next(request)
#         secure_headers.framework.fastapi(response)
#         return response
