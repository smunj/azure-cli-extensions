# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DataFlowDebugSessionOperations(object):
    """DataFlowDebugSessionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datafactory.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _create_initial(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        compute_type=None,  # type: Optional[str]
        core_count=None,  # type: Optional[int]
        time_to_live=None,  # type: Optional[int]
        name=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.IntegrationRuntime"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CreateDataFlowDebugSessionResponse"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CreateDataFlowDebugSessionResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _request = models.CreateDataFlowDebugSessionRequest(compute_type=compute_type, core_count=core_count, time_to_live=time_to_live, name=name, properties=properties)
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'CreateDataFlowDebugSessionRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('CreateDataFlowDebugSessionResponse', pipeline_response)

        if response.status_code == 202:
            response_headers['location']=self._deserialize('str', response.headers.get('location'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/createDataFlowDebugSession'}

    def begin_create(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        compute_type=None,  # type: Optional[str]
        core_count=None,  # type: Optional[int]
        time_to_live=None,  # type: Optional[int]
        name=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.IntegrationRuntime"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.CreateDataFlowDebugSessionResponse"
        """Creates a data flow debug session.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param compute_type: Compute type of the cluster. The value will be overwritten by the same
     setting in integration runtime if provided.
        :type compute_type: str
        :param core_count: Core count of the cluster. The value will be overwritten by the same setting
     in integration runtime if provided.
        :type core_count: int
        :param time_to_live: Time to live setting of the cluster in minutes.
        :type time_to_live: int
        :param name: The resource name.
        :type name: str
        :param properties: Integration runtime properties.
        :type properties: ~azure.mgmt.datafactory.models.IntegrationRuntime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns CreateDataFlowDebugSessionResponse
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.datafactory.models.CreateDataFlowDebugSessionResponse]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CreateDataFlowDebugSessionResponse"]
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            compute_type=compute_type,
            core_count=core_count,
            time_to_live=time_to_live,
            name=name,
            properties=properties,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('CreateDataFlowDebugSessionResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/createDataFlowDebugSession'}

    def query_by_factory(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.QueryDataFlowDebugSessionsResponse"
        """Query all active data flow debug sessions.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QueryDataFlowDebugSessionsResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.QueryDataFlowDebugSessionsResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.QueryDataFlowDebugSessionsResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-06-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.query_by_factory.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.post(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('QueryDataFlowDebugSessionsResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    query_by_factory.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryDataFlowDebugSessions'}

    def add_data_flow(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        session_id=None,  # type: Optional[str]
        datasets=None,  # type: Optional[List["DatasetDebugResource"]]
        linked_services=None,  # type: Optional[List["LinkedServiceDebugResource"]]
        source_settings=None,  # type: Optional[List["DataFlowSourceSetting"]]
        parameters=None,  # type: Optional[Dict[str, object]]
        dataset_parameters=None,  # type: Optional[object]
        folder_path=None,  # type: Optional[str]
        reference_name=None,  # type: Optional[str]
        parameter_value_specification_parameters=None,  # type: Optional[Dict[str, object]]
        name=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.DataFlow"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.AddDataFlowToDebugSessionResponse"
        """Add a data flow into debug session.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param session_id: The ID of data flow debug session.
        :type session_id: str
        :param datasets: List of datasets.
        :type datasets: list[~azure.mgmt.datafactory.models.DatasetDebugResource]
        :param linked_services: List of linked services.
        :type linked_services: list[~azure.mgmt.datafactory.models.LinkedServiceDebugResource]
        :param source_settings: Source setting for data flow debug.
        :type source_settings: list[~azure.mgmt.datafactory.models.DataFlowSourceSetting]
        :param parameters: Data flow parameters.
        :type parameters: dict[str, object]
        :param dataset_parameters: Parameters for dataset.
        :type dataset_parameters: object
        :param folder_path: Folder path for staging blob.
        :type folder_path: str
        :param reference_name: Reference LinkedService name.
        :type reference_name: str
        :param parameter_value_specification_parameters: Arguments for LinkedService.
        :type parameter_value_specification_parameters: dict[str, object]
        :param name: The resource name.
        :type name: str
        :param properties: Data flow properties.
        :type properties: ~azure.mgmt.datafactory.models.DataFlow
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AddDataFlowToDebugSessionResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.AddDataFlowToDebugSessionResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.AddDataFlowToDebugSessionResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _request = models.DataFlowDebugPackage(session_id=session_id, datasets=datasets, linked_services=linked_services, source_settings=source_settings, parameters_debug_settings_parameters=parameters, dataset_parameters=dataset_parameters, folder_path=folder_path, reference_name=reference_name, parameters_staging_linked_service_parameters=parameter_value_specification_parameters, name=name, properties=properties)
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.add_data_flow.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'DataFlowDebugPackage')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AddDataFlowToDebugSessionResponse', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    add_data_flow.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/addDataFlowToDebugSession'}

    def delete(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        session_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a data flow debug session.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param session_id: The ID of data flow debug session.
        :type session_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _request = models.DeleteDataFlowDebugSessionRequest(session_id=session_id)
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'DeleteDataFlowDebugSessionRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/deleteDataFlowDebugSession'}

    def _execute_command_initial(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        session_id=None,  # type: Optional[str]
        command=None,  # type: Optional[Union[str, "models.DataFlowDebugCommandType"]]
        command_payload=None,  # type: Optional["models.DataFlowDebugCommandPayload"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DataFlowDebugCommandResponse"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DataFlowDebugCommandResponse"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _request = models.DataFlowDebugCommandRequest(session_id=session_id, command=command, command_payload=command_payload)
        api_version = "2018-06-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._execute_command_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'factoryName': self._serialize.url("factory_name", factory_name, 'str', max_length=63, min_length=3, pattern=r'^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_request, 'DataFlowDebugCommandRequest')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DataFlowDebugCommandResponse', pipeline_response)

        if response.status_code == 202:
            response_headers['location']=self._deserialize('str', response.headers.get('location'))

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _execute_command_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/executeDataFlowDebugCommand'}

    def begin_execute_command(
        self,
        resource_group_name,  # type: str
        factory_name,  # type: str
        session_id=None,  # type: Optional[str]
        command=None,  # type: Optional[Union[str, "models.DataFlowDebugCommandType"]]
        command_payload=None,  # type: Optional["models.DataFlowDebugCommandPayload"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DataFlowDebugCommandResponse"
        """Execute a data flow debug command.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param session_id: The ID of data flow debug session.
        :type session_id: str
        :param command: The command type.
        :type command: str or ~azure.mgmt.datafactory.models.DataFlowDebugCommandType
        :param command_payload: The command payload object.
        :type command_payload: ~azure.mgmt.datafactory.models.DataFlowDebugCommandPayload
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns DataFlowDebugCommandResponse
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.datafactory.models.DataFlowDebugCommandResponse]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DataFlowDebugCommandResponse"]
        raw_result = self._execute_command_initial(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            session_id=session_id,
            command=command,
            command_payload=command_payload,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('DataFlowDebugCommandResponse', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_execute_command.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/executeDataFlowDebugCommand'}
