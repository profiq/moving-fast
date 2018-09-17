from django.db import close_old_connections


class JwtAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        print(scope)
        close_old_connections()

        return self.inner(scope)
