# (C) Copyright 2015 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_config import cfg


service_available_group = cfg.OptGroup(name='service_available',
                                       title='Available OpenStack Services')
ServiceAvailableGroup = [
    cfg.BoolOpt('logs',
                default=True,
                help=('Whether or not Monasca-Log-Api '
                      'is expected to be available')),
    cfg.BoolOpt('logs-search',
                default=True,
                help=('Whether or not Monasca-Log-Api search engine '
                      '(ElasticSearch) is expected to be available')),
    cfg.BoolOpt("monasca",
                default=True,
                help="Whether or not Monasca is expected to be "
                     "available")]

monitoring_group = cfg.OptGroup(name="monitoring",
                                title="Monitoring Service Options")

MonitoringGroup = [
    cfg.StrOpt("region",
               default="",
               help="The monitoring region name to use. If empty, the value "
                    "of identity.region is used instead. If no such region "
                    "is found in the service catalog, the first found one is "
                    "used."),
    cfg.StrOpt("catalog_type",
               default="monitoring",
               help="Keystone catalog service type of the monitoring service."),
    cfg.StrOpt('catalog_type_logs',
               default='logs',
               help='Keystone catalog service type of the logging service.'),
    cfg.StrOpt('catalog_type_log_query',
               default='logs-search',
               help='Keystone catalog service type of the log query service.'),
    cfg.StrOpt('log_query_message_field',
               default='message',
               help='The field under which the log message is stored.'),
    cfg.StrOpt('log_uri_path',
               default='/logs',
               help='Path used to form Log API URI.'),
    cfg.ListOpt('log_project_id_path',
                default=['_source', 'tenant'],
                help='Series of keys to access the Project ID field in a persisted'
                'log file.'),
    cfg.StrOpt('endpoint_type',
               default='publicURL',
               choices=['public', 'admin', 'internal',
                        'publicURL', 'adminURL', 'internalURL'],
               help="The endpoint type to use for the monitoring service."),
    cfg.StrOpt('api_version',
               default='v2.0',
               help='monasca-log-api API version'),
    cfg.StrOpt('kibana_version',
               default='7.3.0',
               help='Kibana version'),
    cfg.IntOpt('log_api_max_log_size',
               default=1024 * 1024,
               help=('Refers to payload/envelope size. This should be set '
                     'to the same value as "[service]max_log_size" in the '
                     'monasca-log-api configuration'))
]
