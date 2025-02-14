from typing import TYPE_CHECKING, Union

from .schema import (
    ArbcancelSubscriptionRequest,
    ArbcancelSubscriptionResponse,
    ArbcreateSubscriptionRequest,
    ArbcreateSubscriptionResponse,
    ArbgetSubscriptionListRequest,
    ArbgetSubscriptionListResponse,
    ArbgetSubscriptionRequest,
    ArbgetSubscriptionResponse,
    ArbgetSubscriptionStatusRequest,
    ArbgetSubscriptionStatusResponse,
    ArbupdateSubscriptionRequest,
    ArbupdateSubscriptionResponse,
    AuthenticateTestRequest,
    AuthenticateTestResponse,
    CreateCustomerPaymentProfileRequest,
    CreateCustomerPaymentProfileResponse,
    CreateCustomerProfileFromTransactionRequest,
    CreateCustomerProfileRequest,
    CreateCustomerProfileResponse,
    CreateCustomerProfileTransactionRequest,
    CreateCustomerProfileTransactionResponse,
    CreateCustomerShippingAddressRequest,
    CreateCustomerShippingAddressResponse,
    CreateTransactionRequest,
    CreateTransactionResponse,
    DecryptPaymentDataRequest,
    DecryptPaymentDataResponse,
    DeleteCustomerPaymentProfileRequest,
    DeleteCustomerPaymentProfileResponse,
    DeleteCustomerProfileRequest,
    DeleteCustomerProfileResponse,
    DeleteCustomerShippingAddressRequest,
    DeleteCustomerShippingAddressResponse,
    ErrorResponse,
    GetAujobDetailsRequest,
    GetAujobDetailsResponse,
    GetAujobSummaryRequest,
    GetAujobSummaryResponse,
    GetBatchStatisticsRequest,
    GetBatchStatisticsResponse,
    GetCustomerPaymentProfileListRequest,
    GetCustomerPaymentProfileListResponse,
    GetCustomerPaymentProfileNonceRequest,
    GetCustomerPaymentProfileNonceResponse,
    GetCustomerPaymentProfileRequest,
    GetCustomerPaymentProfileResponse,
    GetCustomerProfileIdsRequest,
    GetCustomerProfileIdsResponse,
    GetCustomerProfileRequest,
    GetCustomerProfileResponse,
    GetCustomerShippingAddressRequest,
    GetCustomerShippingAddressResponse,
    GetHostedPaymentPageRequest,
    GetHostedPaymentPageResponse,
    GetHostedProfilePageRequest,
    GetHostedProfilePageResponse,
    GetMerchantDetailsRequest,
    GetMerchantDetailsResponse,
    GetSettledBatchListRequest,
    GetSettledBatchListResponse,
    GetTransactionDetailsRequest,
    GetTransactionDetailsResponse,
    GetTransactionListForCustomerRequest,
    GetTransactionListRequest,
    GetTransactionListResponse,
    GetUnsettledTransactionListRequest,
    GetUnsettledTransactionListResponse,
    IsAliveRequest,
    IsAliveResponse,
    LogoutRequest,
    LogoutResponse,
    MobileDeviceLoginRequest,
    MobileDeviceLoginResponse,
    MobileDeviceRegistrationRequest,
    MobileDeviceRegistrationResponse,
    SecurePaymentContainerRequest,
    SecurePaymentContainerResponse,
    SendCustomerTransactionReceiptRequest,
    SendCustomerTransactionReceiptResponse,
    UpdateCustomerPaymentProfileRequest,
    UpdateCustomerPaymentProfileResponse,
    UpdateCustomerProfileRequest,
    UpdateCustomerProfileResponse,
    UpdateCustomerShippingAddressRequest,
    UpdateCustomerShippingAddressResponse,
    UpdateHeldTransactionRequest,
    UpdateHeldTransactionResponse,
    UpdateMerchantDetailsRequest,
    UpdateMerchantDetailsResponse,
    UpdateSplitTenderGroupRequest,
    UpdateSplitTenderGroupResponse,
    ValidateCustomerPaymentProfileRequest,
    ValidateCustomerPaymentProfileResponse,
)
from .typing import SyncAsync

if TYPE_CHECKING:
    from .client import BaseClient


class Operation:
    def __init__(self, parent: "BaseClient") -> None:
        self.parent = parent


class CustomerProfile(Operation):
    def create(
        self,
        request: CreateCustomerProfileRequest,
    ) -> SyncAsync[Union[CreateCustomerProfileResponse, ErrorResponse]]:
        """
        Use this method to create a new customer profile including any customer payment profiles and customer shipping
        addresses.
        """
        return self.parent.request(request, CreateCustomerProfileResponse)

    def create_from_transaction(
        self,
        request: CreateCustomerProfileFromTransactionRequest,
    ) -> SyncAsync[Union[CreateCustomerProfileResponse, ErrorResponse]]:
        """
        This request enables you to create a customer profile, payment profile, and shipping profile from an existing
        successful transaction.
        """
        return self.parent.request(request, CreateCustomerProfileResponse)

    def create_transaction(
        self,
        request: CreateCustomerProfileTransactionRequest,
    ) -> SyncAsync[Union[CreateCustomerProfileTransactionResponse, ErrorResponse]]:
        return self.parent.request(request, CreateCustomerProfileTransactionResponse)

    def delete(
        self,
        request: DeleteCustomerProfileRequest,
    ) -> SyncAsync[Union[DeleteCustomerProfileResponse, ErrorResponse]]:
        """
        Use this method to delete an existing customer profile along with all associated customer payment profiles and
        customer shipping addresses.
        """
        return self.parent.request(request, DeleteCustomerProfileResponse)

    def get(
        self,
        request: GetCustomerProfileRequest,
    ) -> SyncAsync[Union[GetCustomerProfileResponse, ErrorResponse]]:
        """
        Use this method to retrieve an existing customer profile along with all the associated payment profiles and
        shipping addresses.
        """
        return self.parent.request(request, GetCustomerProfileResponse)

    def get_ids(
        self,
        request: GetCustomerProfileIdsRequest,
    ) -> SyncAsync[Union[GetCustomerProfileIdsResponse, ErrorResponse]]:
        """
        Use this method to retrieve all existing customer profile IDs.
        """
        return self.parent.request(request, GetCustomerProfileIdsResponse)

    def update(
        self,
        request: UpdateCustomerProfileRequest,
    ) -> SyncAsync[Union[UpdateCustomerProfileResponse, ErrorResponse]]:
        """
        Use this method to update an existing customer profile.
        """
        return self.parent.request(request, UpdateCustomerProfileResponse)


class CustomerPaymentProfile(Operation):
    def create(
        self,
        request: CreateCustomerPaymentProfileRequest,
    ) -> SyncAsync[Union[CreateCustomerPaymentProfileResponse, ErrorResponse]]:
        """
        Use this method to create a new customer payment profile for an existing customer profile.
        """
        return self.parent.request(request, CreateCustomerPaymentProfileResponse)

    def delete(
        self,
        request: DeleteCustomerPaymentProfileRequest,
    ) -> SyncAsync[Union[DeleteCustomerPaymentProfileResponse, ErrorResponse]]:
        """
        Use this method to delete a customer payment profile from an existing customer profile.
        """
        return self.parent.request(request, DeleteCustomerPaymentProfileResponse)

    def get(
        self,
        request: GetCustomerPaymentProfileRequest,
    ) -> SyncAsync[Union[GetCustomerPaymentProfileResponse, ErrorResponse]]:
        """
        Use this method to retrieve the details of a customer payment profile associated with an existing customer
        profile.
        """
        return self.parent.request(request, GetCustomerPaymentProfileResponse)

    def get_nonce(
        self,
        request: GetCustomerPaymentProfileNonceRequest,
    ) -> SyncAsync[Union[GetCustomerPaymentProfileNonceResponse, ErrorResponse]]:
        return self.parent.request(request, GetCustomerPaymentProfileNonceResponse)

    def list(
        self,
        request: GetCustomerPaymentProfileListRequest,
    ) -> SyncAsync[Union[GetCustomerPaymentProfileListResponse, ErrorResponse]]:
        """
        Use this method to get list of all the payment profiles that match the submitted searchType. You can use this
        method to get the list of all cards expiring this month. The method will return up to 10 results in a
        single request. Paging options can be sent to limit the result set or to retrieve additional results beyond the
        10 item limit. You can add the sorting and paging options to customize the result set.
        """
        return self.parent.request(request, GetCustomerPaymentProfileListResponse)

    def update(
        self,
        request: UpdateCustomerPaymentProfileRequest,
    ) -> SyncAsync[Union[UpdateCustomerPaymentProfileResponse, ErrorResponse]]:
        """
        Use this method to update a payment profile for an existing customer profile.
        """
        return self.parent.request(request, UpdateCustomerPaymentProfileResponse)

    def validate(
        self,
        request: ValidateCustomerPaymentProfileRequest,
    ) -> SyncAsync[Union[ValidateCustomerPaymentProfileResponse, ErrorResponse]]:
        """
        Use this method to generate a test transaction that verifies an existing customer payment profile. No customer
        receipt emails are sent when this method is called.
        """
        return self.parent.request(request, ValidateCustomerPaymentProfileResponse)


class CustomerShippingAddress(Operation):
    def create(
        self,
        request: CreateCustomerShippingAddressRequest,
    ) -> SyncAsync[Union[CreateCustomerShippingAddressResponse, ErrorResponse]]:
        """
        Use this method to create a new customer shipping address for an existing customer profile.
        """
        return self.parent.request(request, CreateCustomerShippingAddressResponse)

    def delete(
        self,
        request: DeleteCustomerShippingAddressRequest,
    ) -> SyncAsync[Union[DeleteCustomerShippingAddressResponse, ErrorResponse]]:
        """
        Use this method to delete a customer shipping address from an existing customer profile.
        """
        return self.parent.request(request, DeleteCustomerShippingAddressResponse)

    def get(
        self,
        request: GetCustomerShippingAddressRequest,
    ) -> SyncAsync[Union[GetCustomerShippingAddressResponse, ErrorResponse]]:
        """
        Use this method to retrieve the details of a customer shipping address associated with an existing customer
        profile.
        """
        return self.parent.request(request, GetCustomerShippingAddressResponse)

    def update(
        self,
        request: UpdateCustomerShippingAddressRequest,
    ) -> SyncAsync[Union[UpdateCustomerShippingAddressResponse, ErrorResponse]]:
        """
        Use this method to update a shipping address for an existing customer profile.
        """
        return self.parent.request(request, UpdateCustomerShippingAddressResponse)


class Transaction(Operation):
    def create(
        self,
        request: CreateTransactionRequest,
    ) -> SyncAsync[Union[CreateTransactionResponse, ErrorResponse]]:
        return self.parent.request(request, CreateTransactionResponse)

    def get(
        self,
        request: GetTransactionDetailsRequest,
    ) -> SyncAsync[Union[GetTransactionDetailsResponse, ErrorResponse]]:
        """
        Use this method to get detailed information about a specific transaction.
        """
        return self.parent.request(request, GetTransactionDetailsResponse)

    def list(
        self,
        request: GetTransactionListRequest,
    ) -> SyncAsync[Union[GetTransactionListResponse, ErrorResponse]]:
        """
        Use this method to return data for all transactions in a specified batch. The function will return data for up
        to 1000 of the most recent transactions in a single request. Paging options can be sent to limit the result set
        or to retrieve additional transactions beyond the 1000 transaction limit. No input parameters are required other
        than the authentication information and a batch ID. However, you can add the sorting and paging options to
        customize the result set.
        """
        return self.parent.request(request, GetTransactionListResponse)

    def list_for_customer(
        self,
        request: GetTransactionListForCustomerRequest,
    ) -> SyncAsync[Union[GetTransactionListResponse, ErrorResponse]]:
        """
        Use this method to retrieve transactions for a specific customer profile or customer payment profile. The
        method will return data for up to 1000 of the most recent transactions in a single request. Paging options can
        be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction limit. If
        no customer payment profile is supplied then this function will return transactions for all customer payment
        profiles associated with the specified customer profile. This allows you to retrieve all transactions for that
        customer regardless of card type (such as Visa or Mastercard) or payment type (such as credit card or bank
        account). You can add the sorting and paging options to customize the result set.
        """
        return self.parent.request(request, GetTransactionListResponse)

    def list_unsettled(
        self,
        request: GetUnsettledTransactionListRequest,
    ) -> SyncAsync[Union[GetUnsettledTransactionListResponse, ErrorResponse]]:
        """
        Use this method to get data for unsettled transactions. The method will return data for up to 1000 of the most
        recent transactions in a single request. Paging options can be sent to limit the result set or to retrieve
        additional transactions beyond the 1000 transaction limit. No input parameters are required other than the
        authentication information. However, you can add the sorting and paging options to customize the result set.
        """
        return self.parent.request(request, GetUnsettledTransactionListResponse)

    def send_receipt(
        self,
        request: SendCustomerTransactionReceiptRequest,
    ) -> SyncAsync[Union[SendCustomerTransactionReceiptResponse, ErrorResponse]]:
        return self.parent.request(request, SendCustomerTransactionReceiptResponse)

    def update_held(
        self,
        request: UpdateHeldTransactionRequest,
    ) -> SyncAsync[Union[UpdateHeldTransactionResponse, ErrorResponse]]:
        """
        Approve or Decline a held Transaction.
        """
        return self.parent.request(request, UpdateHeldTransactionResponse)

    def update_split_tender_group(
        self,
        request: UpdateSplitTenderGroupRequest,
    ) -> SyncAsync[Union[UpdateSplitTenderGroupResponse, ErrorResponse]]:
        """
        Use this method to update the status of an existing order that contains multiple transactions with the same
        splitTenderId  value.
        """
        return self.parent.request(request, UpdateSplitTenderGroupResponse)


class AccountUpdaterJob(Operation):
    def get_details(
        self,
        request: GetAujobDetailsRequest,
    ) -> SyncAsync[Union[GetAujobDetailsResponse, ErrorResponse]]:
        """
        Use this method to get details of each card updated or deleted by the Account Updater process for a particular
        month. The method will return data for up to 1000 of the most recent transactions in a single request. Paging
        options can be sent to limit the result set or to retrieve additional transactions beyond the 1000 transaction
        limit. No input parameters are required other than the authentication information and a batch ID. However, you
        can add the sorting and paging options to customize the result set.
        """
        return self.parent.request(request, GetAujobDetailsResponse)

    def get_summary(
        self,
        request: GetAujobSummaryRequest,
    ) -> SyncAsync[Union[GetAujobSummaryResponse, ErrorResponse]]:
        """
        Use this method to get a summary of the results of the Account Updater process for a particular month.
        """
        return self.parent.request(request, GetAujobSummaryResponse)


class Batch(Operation):
    def get_statistics(
        self,
        request: GetBatchStatisticsRequest,
    ) -> SyncAsync[Union[GetBatchStatisticsResponse, ErrorResponse]]:
        """
        A call to getBatchStatisticsRequest returns statistics for a single batch, specified by the batch ID.
        """
        return self.parent.request(request, GetBatchStatisticsResponse)

    def list_settled(
        self,
        request: GetSettledBatchListRequest,
    ) -> SyncAsync[Union[GetSettledBatchListResponse, ErrorResponse]]:
        """
        This method returns Batch ID, Settlement Time, & Settlement State for all settled batches with a range of dates.
        If includeStatistics  is  true, you also receive batch statistics by payment type and batch totals. All input
        parameters other than merchant authentication are optional. If no dates are specified, then the default is the
        past 24 hours, ending at the time of the call to this method.
        """
        return self.parent.request(request, GetSettledBatchListResponse)


class HostedPage(Operation):
    def get_payment_page(
        self,
        request: GetHostedPaymentPageRequest,
    ) -> SyncAsync[Union[GetHostedPaymentPageResponse, ErrorResponse]]:
        """
        Use this method to retrieve a form token which can be used to request the Authorize.net Accept hosted payment
        page.
        """
        return self.parent.request(request, GetHostedPaymentPageResponse)

    def get_profile_page(
        self,
        request: GetHostedProfilePageRequest,
    ) -> SyncAsync[Union[GetHostedProfilePageResponse, ErrorResponse]]:
        """
        Use this method to initiate a request for direct access to the Authorize.net website.
        """
        return self.parent.request(request, GetHostedProfilePageResponse)


class Merchant(Operation):
    def get(
        self,
        request: GetMerchantDetailsRequest,
    ) -> SyncAsync[Union[GetMerchantDetailsResponse, ErrorResponse]]:
        """
        Call this method and supply your authentication information to receive merchant details in the response. The
        information that is returned is helpful for OAuth and Accept integrations. Generate a PublicClientKey only if
        one is not generated or is not active. Only the most recently generated active key is returned.
        """
        return self.parent.request(request, GetMerchantDetailsResponse)

    def update(
        self,
        request: UpdateMerchantDetailsRequest,
    ) -> SyncAsync[Union[UpdateMerchantDetailsResponse, ErrorResponse]]:
        return self.parent.request(request, UpdateMerchantDetailsResponse)


class MobileDevice(Operation):
    def login(
        self,
        request: MobileDeviceLoginRequest,
    ) -> SyncAsync[Union[MobileDeviceLoginResponse, ErrorResponse]]:
        return self.parent.request(request, MobileDeviceLoginResponse)

    def register(
        self,
        request: MobileDeviceRegistrationRequest,
    ) -> SyncAsync[Union[MobileDeviceRegistrationResponse, ErrorResponse]]:
        return self.parent.request(request, MobileDeviceRegistrationResponse)


class SecurePaymentContainer(Operation):
    def create(
        self,
        request: SecurePaymentContainerRequest,
    ) -> SyncAsync[Union[SecurePaymentContainerResponse, ErrorResponse]]:
        return self.parent.request(request, SecurePaymentContainerResponse)


class Subscription(Operation):
    def cancel(
        self,
        request: ArbcancelSubscriptionRequest,
    ) -> SyncAsync[Union[ArbcancelSubscriptionResponse, ErrorResponse]]:
        return self.parent.request(request, ArbcancelSubscriptionResponse)

    def create(
        self,
        request: ArbcreateSubscriptionRequest,
    ) -> SyncAsync[Union[ArbcreateSubscriptionResponse, ErrorResponse]]:
        return self.parent.request(request, ArbcreateSubscriptionResponse)

    def get(
        self,
        request: ArbgetSubscriptionRequest,
    ) -> SyncAsync[Union[ArbgetSubscriptionResponse, ErrorResponse]]:
        return self.parent.request(request, ArbgetSubscriptionResponse)

    def get_status(
        self,
        request: ArbgetSubscriptionStatusRequest,
    ) -> SyncAsync[Union[ArbgetSubscriptionStatusResponse, ErrorResponse]]:
        return self.parent.request(request, ArbgetSubscriptionStatusResponse)

    def list(
        self,
        request: ArbgetSubscriptionListRequest,
    ) -> SyncAsync[Union[ArbgetSubscriptionListResponse, ErrorResponse]]:
        return self.parent.request(request, ArbgetSubscriptionListResponse)

    def update(
        self,
        request: ArbupdateSubscriptionRequest,
    ) -> SyncAsync[Union[ArbupdateSubscriptionResponse, ErrorResponse]]:
        return self.parent.request(request, ArbupdateSubscriptionResponse)


class Misc(Operation):
    def decrypt_payment_data(
        self,
        request: DecryptPaymentDataRequest,
    ) -> SyncAsync[Union[DecryptPaymentDataResponse, ErrorResponse]]:
        return self.parent.request(request, DecryptPaymentDataResponse)

    def is_alive(
        self,
        request: IsAliveRequest,
    ) -> SyncAsync[Union[IsAliveResponse, ErrorResponse]]:
        return self.parent.request(request, IsAliveResponse)

    def logout(
        self,
        request: LogoutRequest,
    ) -> SyncAsync[Union[LogoutResponse, ErrorResponse]]:
        return self.parent.request(request, LogoutResponse)

    def test_authenticate(
        self,
        request: AuthenticateTestRequest,
    ) -> SyncAsync[Union[AuthenticateTestResponse, ErrorResponse]]:
        return self.parent.request(request, AuthenticateTestResponse)
