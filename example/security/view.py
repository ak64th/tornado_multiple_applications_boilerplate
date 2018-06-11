import jwt
from tornado.web import RequestHandler, HTTPError
from werkzeug.utils import cached_property

from example import settings
from example.exceptions import APIError


class AuthRequestHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    @cached_property
    def token(self):
        auth_header_value = self.request.headers.get('Authorization', None)
        auth_header_prefix = settings.JWT_AUTH_HEADER_PREFIX

        if not auth_header_value:
            return

        parts = auth_header_value.split()

        if parts[0].lower() != auth_header_prefix.lower():
            raise APIError('Unsupported authorization type', 401)
        elif len(parts) == 1:
            raise APIError('Token missing', 401)
        elif len(parts) > 2:
            raise APIError('Token contains spaces', 401)

        return parts[1]

    @cached_property
    def auth(self):
        if not self.token:
            return

        secret = settings.JWT_SECRET_KEY
        algorithm = settings.JWT_ALGORITHM
        leeway = settings.JWT_LEEWAY
        verify_claims = settings.JWT_VERIFY_CLAIMS
        required_claims = settings.JWT_REQUIRED_CLAIMS
        try:
            options = {'verify_' + claim: True for claim in verify_claims}
            options.update({'require_' + claim: True for claim in required_claims})
            payload = jwt.decode(self.token, secret, options=options, algorithms=[algorithm], leeway=leeway)
        except jwt.InvalidTokenError as e:
            raise APIError('Invalid token: {}'.format(e), status_code=403)
        return payload

    @cached_property
    def identity(self):
        return self.auth['identity'] if self.auth else None

    def write_error(self, status_code, **kwargs):
        if 'exc_info' in kwargs:
            exc = kwargs['exc_info'][1]
            if isinstance(exc, APIError):
                self.set_status(exc.status_code)
                self.write(exc.to_dict())
                self.finish()
            elif isinstance(exc, HTTPError):
                self.set_status(exc.status_code)
                self.write({'message': self._reason})
                self.finish()
        if not self._finished:
            super(AuthRequestHandler, self).write_error(status_code, **kwargs)
