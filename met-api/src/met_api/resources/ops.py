# Copyright © 2021 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Operational endpoints for health and readiness checks."""

from flask_restx import Namespace, Resource, cors
from sqlalchemy import exc, text

from met_api.models import db

API = Namespace('', description='MET API operational endpoints')

SQL = text('select 1')


@API.route('/healthz')
class Health(Resource):
    """Determines if the service process is alive."""

    @staticmethod
    @cors.crossdomain(origin='*')
    def get():
        """Return a healthy response for liveness probes."""
        try:
            db.session.execute(SQL)
        except exc.SQLAlchemyError as err:
            API.logger.error('Health check failed: %s', err)
            return {'message': 'api is unhealthy'}, 500
        return {'message': 'api is healthy'}, 200


@API.route('/readyz')
class Ready(Resource):
    """Determines if the service is ready to receive traffic."""

    @staticmethod
    @cors.crossdomain(origin='*')
    def get():
        """Return a ready response for readiness probes."""
        return {'message': 'api is ready'}, 200
