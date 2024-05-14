# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tinkoff.invest.grpc import users_pb2 as tinkoff_dot_invest_dot_grpc_dot_users__pb2


class UsersServiceStub(object):
    """С помощью сервиса можно получить: </br> 1.
    список счетов пользователя; </br> 2. маржинальные показатели по счёту.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAccounts = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsResponse.FromString,
                )
        self.GetMarginAttributes = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetMarginAttributes',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.FromString,
                )
        self.GetUserTariff = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetUserTariff',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffResponse.FromString,
                )
        self.GetInfo = channel.unary_unary(
                '/tinkoff.public.invest.api.contract.v1.UsersService/GetInfo',
                request_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoResponse.FromString,
                )


class UsersServiceServicer(object):
    """С помощью сервиса можно получить: </br> 1.
    список счетов пользователя; </br> 2. маржинальные показатели по счёту.
    """

    def GetAccounts(self, request, context):
        """Получить счета пользователя.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMarginAttributes(self, request, context):
        """Рассчитать маржинальные показатели по счёту.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserTariff(self, request, context):
        """Запросить тариф пользователя.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInfo(self, request, context):
        """Получить информацию о пользователе.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UsersServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAccounts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccounts,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsResponse.SerializeToString,
            ),
            'GetMarginAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMarginAttributes,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.SerializeToString,
            ),
            'GetUserTariff': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserTariff,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffResponse.SerializeToString,
            ),
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoRequest.FromString,
                    response_serializer=tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tinkoff.public.invest.api.contract.v1.UsersService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UsersService(object):
    """С помощью сервиса можно получить: </br> 1.
    список счетов пользователя; </br> 2. маржинальные показатели по счёту.
    """

    @staticmethod
    def GetAccounts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts',
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetAccountsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMarginAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.UsersService/GetMarginAttributes',
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetMarginAttributesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserTariff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.UsersService/GetUserTariff',
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetUserTariffResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tinkoff.public.invest.api.contract.v1.UsersService/GetInfo',
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoRequest.SerializeToString,
            tinkoff_dot_invest_dot_grpc_dot_users__pb2.GetInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
