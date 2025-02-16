from decimal import Decimal
from enum import Enum as BaseEnum
from typing import Optional

from pydantic import BaseModel, ConfigDict
from xsdata.models.datatype import XmlDate, XmlDateTime
from xsdata_pydantic.fields import field

__NAMESPACE__ = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"


class Enum(BaseEnum):
    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class ArbgetSubscriptionListOrderFieldEnum(Enum):
    ID = "id"
    NAME = "name"
    STATUS = "status"
    CREATE_TIME_STAMP_UTC = "createTimeStampUTC"
    LAST_NAME = "lastName"
    FIRST_NAME = "firstName"
    ACCOUNT_NUMBER = "accountNumber"
    AMOUNT = "amount"
    PAST_OCCURRENCES = "pastOccurrences"


class ArbgetSubscriptionListSearchTypeEnum(Enum):
    CARD_EXPIRING_THIS_MONTH = "cardExpiringThisMonth"
    SUBSCRIPTION_ACTIVE = "subscriptionActive"
    SUBSCRIPTION_EXPIRING_THIS_MONTH = "subscriptionExpiringThisMonth"
    SUBSCRIPTION_INACTIVE = "subscriptionInactive"


class ArbsubscriptionStatusEnum(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    SUSPENDED = "suspended"
    CANCELED = "canceled"
    TERMINATED = "terminated"


class ArbsubscriptionUnitEnum(Enum):
    DAYS = "days"
    MONTHS = "months"


class AujobTypeEnum(Enum):
    ALL = "all"
    UPDATES = "updates"
    DELETES = "deletes"


class ArrayOfCardType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    card_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "cardType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_occurs": 30,
            "nillable": True,
        },
    )


class ArrayOfCurrencyCode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    currency: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 3,
            "max_length": 3,
        },
    )


class ArrayOfFraudFilterType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    fraud_filter: list[str] = field(
        default_factory=list,
        metadata={
            "name": "fraudFilter",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_occurs": 1,
            "max_occurs": 1000,
        },
    )


class ArrayOfLong(BaseModel):
    model_config = ConfigDict(defer_build=True)
    long: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfMarketType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    market_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "marketType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )


class ArrayOfNumericString(BaseModel):
    model_config = ConfigDict(defer_build=True)
    numeric_string: list[str] = field(
        default_factory=list,
        metadata={
            "name": "numericString",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class ArrayOfProductCode(BaseModel):
    model_config = ConfigDict(defer_build=True)
    product_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "productCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 3,
        },
    )


class ArrayOfString(BaseModel):
    model_config = ConfigDict(defer_build=True)
    string: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ContactDetailType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )


class CustomerPaymentProfileOrderFieldEnum(Enum):
    ID = "id"


class CustomerPaymentProfileSearchTypeEnum(Enum):
    CARDS_EXPIRING_IN_MONTH = "cardsExpiringInMonth"


class EncodingType(Enum):
    BASE64 = "Base64"
    HEX = "Hex"


class EncryptionAlgorithmType(Enum):
    TDES = "TDES"
    AES = "AES"
    RSA = "RSA"


class FdsfilterActionEnum(Enum):
    REJECT = "reject"
    DECLINE = "decline"
    HOLD = "hold"
    AUTH_AND_HOLD = "authAndHold"
    REPORT = "report"


class FdsfilterType(BaseModel):
    class Meta:
        name = "FDSFilterType"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    action: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class OperationType(Enum):
    DECRYPT = "DECRYPT"


class Paging(BaseModel):
    model_config = ConfigDict(defer_build=True)
    limit: int = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1000,
        }
    )
    offset: int = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 100000,
        }
    )


class SubscriptionIdList(BaseModel):
    model_config = ConfigDict(defer_build=True)
    subscription_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class TransactionGroupStatusEnum(Enum):
    ANY = "any"
    PENDING_APPROVAL = "pendingApproval"


class TransactionListOrderFieldEnum(Enum):
    ID = "id"
    SUBMIT_TIME_UTC = "submitTimeUTC"


class AccountTypeEnum(Enum):
    VISA = "Visa"
    MASTER_CARD = "MasterCard"
    AMERICAN_EXPRESS = "AmericanExpress"
    DISCOVER = "Discover"
    JCB = "JCB"
    DINERS_CLUB = "DinersClub"
    E_CHECK = "eCheck"


class AfdsTransactionEnum(Enum):
    APPROVE = "approve"
    DECLINE = "decline"


class ArbTransaction(BaseModel):
    class Meta:
        name = "arbTransaction"

    model_config = ConfigDict(defer_build=True)
    trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    submit_time_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "submitTimeUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    pay_num: Optional[int] = field(
        default=None,
        metadata={
            "name": "payNum",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    attempt_num: Optional[int] = field(
        default=None,
        metadata={
            "name": "attemptNum",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class AuDetailsType(BaseModel):
    class Meta:
        name = "auDetailsType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: int = field(
        metadata={
            "name": "customerProfileID",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer_payment_profile_id: int = field(
        metadata={
            "name": "customerPaymentProfileID",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    update_time_utc: str = field(
        metadata={
            "name": "updateTimeUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    au_reason_code: str = field(
        metadata={
            "name": "auReasonCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    reason_description: str = field(
        metadata={
            "name": "reasonDescription",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class AuResponseType(BaseModel):
    class Meta:
        name = "auResponseType"

    model_config = ConfigDict(defer_build=True)
    au_reason_code: str = field(
        metadata={
            "name": "auReasonCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    profile_count: int = field(
        metadata={
            "name": "profileCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    reason_description: str = field(
        metadata={
            "name": "reasonDescription",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class AuthIndicatorEnum(Enum):
    PRE = "pre"
    FINAL = "final"


class BankAccountTypeEnum(Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    BUSINESS_CHECKING = "businessChecking"


class BatchStatisticType(BaseModel):
    class Meta:
        name = "batchStatisticType"

    model_config = ConfigDict(defer_build=True)
    account_type: str = field(
        metadata={
            "name": "accountType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    charge_amount: Decimal = field(
        metadata={
            "name": "chargeAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    charge_count: int = field(
        metadata={
            "name": "chargeCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    refund_amount: Decimal = field(
        metadata={
            "name": "refundAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    refund_count: int = field(
        metadata={
            "name": "refundCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    void_count: int = field(
        metadata={
            "name": "voidCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    decline_count: int = field(
        metadata={
            "name": "declineCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    error_count: int = field(
        metadata={
            "name": "errorCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    returned_item_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "returnedItemAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    returned_item_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "returnedItemCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    chargeback_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "chargebackAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    chargeback_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "chargebackCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    correction_notice_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "correctionNoticeCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    charge_charge_back_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "chargeChargeBackAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    charge_charge_back_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "chargeChargeBackCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    refund_charge_back_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "refundChargeBackAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    refund_charge_back_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "refundChargeBackCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    charge_returned_items_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "chargeReturnedItemsAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    charge_returned_items_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "chargeReturnedItemsCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    refund_returned_items_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "refundReturnedItemsAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    refund_returned_items_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "refundReturnedItemsCount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CardArt(BaseModel):
    class Meta:
        name = "cardArt"

    model_config = ConfigDict(defer_build=True)
    card_brand: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardBrand",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_image_height: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardImageHeight",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_image_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardImageUrl",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_image_width: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardImageWidth",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CardTypeEnum(Enum):
    VISA = "Visa"
    MASTER_CARD = "MasterCard"
    AMERICAN_EXPRESS = "AmericanExpress"
    DISCOVER = "Discover"
    JCB = "JCB"
    DINERS_CLUB = "DinersClub"


class CcAuthenticationType(BaseModel):
    class Meta:
        name = "ccAuthenticationType"

    model_config = ConfigDict(defer_build=True)
    authentication_indicator: str = field(
        metadata={
            "name": "authenticationIndicator",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    cardholder_authentication_value: str = field(
        metadata={
            "name": "cardholderAuthenticationValue",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class CreditCardSimpleType(BaseModel):
    class Meta:
        name = "creditCardSimpleType"

    model_config = ConfigDict(defer_build=True)
    card_number: str = field(
        metadata={
            "name": "cardNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 16,
        }
    )
    expiration_date: str = field(
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )


class CreditCardTrackType(BaseModel):
    class Meta:
        name = "creditCardTrackType"

    model_config = ConfigDict(defer_build=True)
    track1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    track2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerProfileBaseType(BaseModel):
    class Meta:
        name = "customerProfileBaseType"

    model_config = ConfigDict(defer_build=True)
    merchant_customer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantCustomerId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )


class CustomerProfileIdType(BaseModel):
    class Meta:
        name = "customerProfileIdType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class CustomerProfileSummaryType(BaseModel):
    class Meta:
        name = "customerProfileSummaryType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_customer_id: str = field(
        metadata={
            "name": "merchantCustomerId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    created_date: XmlDateTime = field(
        metadata={
            "name": "createdDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class CustomerProfileTypeEnum(Enum):
    REGULAR = "regular"
    GUEST = "guest"


class CustomerTypeEnum(Enum):
    INDIVIDUAL = "individual"
    BUSINESS = "business"


class DeviceActivationEnum(Enum):
    ACTIVATE = "Activate"
    DISABLE = "Disable"


class DriversLicenseMaskedType(BaseModel):
    class Meta:
        name = "driversLicenseMaskedType"

    model_config = ConfigDict(defer_build=True)
    number: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "length": 8,
        }
    )
    state: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        }
    )
    date_of_birth: str = field(
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 8,
            "max_length": 10,
        }
    )


class DriversLicenseType(BaseModel):
    class Meta:
        name = "driversLicenseType"

    model_config = ConfigDict(defer_build=True)
    number: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 5,
            "max_length": 20,
        }
    )
    state: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 2,
            "max_length": 2,
        }
    )
    date_of_birth: str = field(
        metadata={
            "name": "dateOfBirth",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 8,
            "max_length": 10,
        }
    )


class EcheckTypeEnum(Enum):
    PPD = "PPD"
    WEB = "WEB"
    CCD = "CCD"
    TEL = "TEL"
    ARC = "ARC"
    BOC = "BOC"


class EmvTag(BaseModel):
    class Meta:
        name = "emvTag"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    formatted: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ExtendedAmountType(BaseModel):
    class Meta:
        name = "extendedAmountType"

    model_config = ConfigDict(defer_build=True)
    amount: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 31,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )


class FingerPrintType(BaseModel):
    class Meta:
        name = "fingerPrintType"

    model_config = ConfigDict(defer_build=True)
    hash_value: str = field(
        metadata={
            "name": "hashValue",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    timestamp: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ImpersonationAuthenticationType(BaseModel):
    class Meta:
        name = "impersonationAuthenticationType"

    model_config = ConfigDict(defer_build=True)
    partner_login_id: str = field(
        metadata={
            "name": "partnerLoginId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 25,
        }
    )
    partner_transaction_key: str = field(
        metadata={
            "name": "partnerTransactionKey",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 16,
        }
    )


class IsAliveRequest(BaseModel):
    class Meta:
        name = "isAliveRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refId",
            "type": "Element",
            "max_length": 20,
        },
    )


class LineItemType(BaseModel):
    class Meta:
        name = "lineItemType"

    model_config = ConfigDict(defer_build=True)
    item_id: str = field(
        metadata={
            "name": "itemId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 31,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 31,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    quantity: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    unit_price: Decimal = field(
        metadata={
            "name": "unitPrice",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    taxable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    unit_of_measure: Optional[str] = field(
        default=None,
        metadata={
            "name": "unitOfMeasure",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 12,
        },
    )
    type_of_supply: Optional[str] = field(
        default=None,
        metadata={
            "name": "typeOfSupply",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 2,
        },
    )
    tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "taxRate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
    tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "taxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    national_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "nationalTax",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    local_tax: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "localTax",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    vat_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatRate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
    alternate_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternateTaxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    alternate_tax_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternateTaxType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 4,
        },
    )
    alternate_tax_type_applied: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternateTaxTypeApplied",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 4,
        },
    )
    alternate_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "alternateTaxRate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
    alternate_tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "alternateTaxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    total_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "totalAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    commodity_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "commodityCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 15,
        },
    )
    product_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "productCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 30,
        },
    )
    product_sku: Optional[str] = field(
        default=None,
        metadata={
            "name": "productSKU",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 30,
        },
    )
    discount_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "discountRate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
    discount_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "discountAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_included_in_total: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxIncludedInTotal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_is_after_discount: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxIsAfterDiscount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class MerchantContactType(BaseModel):
    class Meta:
        name = "merchantContactType"

    model_config = ConfigDict(defer_build=True)
    merchant_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantAddress",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantCity",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_state: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantState",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_zip: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantZip",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantPhone",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )


class MerchantInitTransReasonEnum(Enum):
    RESUBMISSION = "resubmission"
    DELAYED_CHARGE = "delayedCharge"
    REAUTHORIZATION = "reauthorization"
    NO_SHOW = "noShow"


class MessageTypeEnum(Enum):
    OK = "Ok"
    ERROR = "Error"


class NameAndAddressType(BaseModel):
    class Meta:
        name = "nameAndAddressType"

    model_config = ConfigDict(defer_build=True)
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    company: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 60,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    zip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 60,
        },
    )


class OpaqueDataType(BaseModel):
    class Meta:
        name = "opaqueDataType"

    model_config = ConfigDict(defer_build=True)
    data_descriptor: str = field(
        metadata={
            "name": "dataDescriptor",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    data_value: str = field(
        metadata={
            "name": "dataValue",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    data_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataKey",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    expiration_time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "expirationTimeStamp",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class OrderType(BaseModel):
    class Meta:
        name = "orderType"

    model_config = ConfigDict(defer_build=True)
    invoice_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    discount_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "discountAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_is_after_discount: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxIsAfterDiscount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    total_tax_type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "totalTaxTypeCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 3,
        },
    )
    purchaser_vatregistration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "purchaserVATRegistrationNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 21,
        },
    )
    merchant_vatregistration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantVATRegistrationNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 21,
        },
    )
    vat_invoice_reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "vatInvoiceReferenceNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 15,
        },
    )
    purchaser_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "purchaserCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 17,
        },
    )
    summary_commodity_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "summaryCommodityCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 4,
        },
    )
    purchase_order_date_utc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "purchaseOrderDateUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    supplier_order_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "supplierOrderReference",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    authorized_contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "authorizedContactName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 36,
        },
    )
    card_acceptor_ref_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardAcceptorRefNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    amex_data_taa1: Optional[str] = field(
        default=None,
        metadata={
            "name": "amexDataTAA1",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    amex_data_taa2: Optional[str] = field(
        default=None,
        metadata={
            "name": "amexDataTAA2",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    amex_data_taa3: Optional[str] = field(
        default=None,
        metadata={
            "name": "amexDataTAA3",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    amex_data_taa4: Optional[str] = field(
        default=None,
        metadata={
            "name": "amexDataTAA4",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )


class OtherTaxType(BaseModel):
    class Meta:
        name = "otherTaxType"

    model_config = ConfigDict(defer_build=True)
    national_tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "nationalTaxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    local_tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "localTaxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    alternate_tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "alternateTaxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    alternate_tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "alternateTaxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 15,
        },
    )
    vat_tax_rate: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatTaxRate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
    vat_tax_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "vatTaxAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class PayPalType(BaseModel):
    class Meta:
        name = "payPalType"

    model_config = ConfigDict(defer_build=True)
    success_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "successUrl",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 2048,
        },
    )
    cancel_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "cancelUrl",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 2048,
        },
    )
    paypal_lc: Optional[str] = field(
        default=None,
        metadata={
            "name": "paypalLc",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 2,
        },
    )
    paypal_hdr_img: Optional[str] = field(
        default=None,
        metadata={
            "name": "paypalHdrImg",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 127,
        },
    )
    paypal_payflowcolor: Optional[str] = field(
        default=None,
        metadata={
            "name": "paypalPayflowcolor",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 6,
        },
    )
    payer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "payerID",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )


class PaymentDetails(BaseModel):
    class Meta:
        name = "paymentDetails"

    model_config = ConfigDict(defer_build=True)
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    promo_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "promoCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    misc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    gift_wrap: Optional[str] = field(
        default=None,
        metadata={
            "name": "giftWrap",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    discount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping_handling: Optional[str] = field(
        default=None,
        metadata={
            "name": "shippingHandling",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    sub_total: Optional[str] = field(
        default=None,
        metadata={
            "name": "subTotal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    order_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "orderID",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    amount: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class PaymentEmvType(BaseModel):
    class Meta:
        name = "paymentEmvType"

    model_config = ConfigDict(defer_build=True)
    emv_data: Optional[object] = field(
        default=None,
        metadata={
            "name": "emvData",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    emv_descriptor: Optional[object] = field(
        default=None,
        metadata={
            "name": "emvDescriptor",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    emv_version: Optional[object] = field(
        default=None,
        metadata={
            "name": "emvVersion",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class PaymentMethodEnum(Enum):
    CREDIT_CARD = "creditCard"
    E_CHECK = "eCheck"
    PAY_PAL = "payPal"


class PaymentMethodsTypeEnum(Enum):
    VISA = "Visa"
    MASTER_CARD = "MasterCard"
    DISCOVER = "Discover"
    AMERICAN_EXPRESS = "AmericanExpress"
    DINERS_CLUB = "DinersClub"
    JCB = "JCB"
    EN_ROUTE = "EnRoute"
    ECHECK = "Echeck"
    PAYPAL = "Paypal"
    VISA_CHECKOUT = "VisaCheckout"
    APPLE_PAY = "ApplePay"
    ANDROID_PAY = "AndroidPay"
    GOOGLE_PAY = "GooglePay"


class PaymentProfile(BaseModel):
    class Meta:
        name = "paymentProfile"

    model_config = ConfigDict(defer_build=True)
    payment_profile_id: str = field(
        metadata={
            "name": "paymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    card_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 3,
            "max_length": 4,
            "pattern": r"[0-9]+",
        },
    )


class PermissionType(BaseModel):
    class Meta:
        name = "permissionType"

    model_config = ConfigDict(defer_build=True)
    permission_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "permissionName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class PermissionsEnum(Enum):
    API_MERCHANT_BASIC_REPORTING = "API_Merchant_BasicReporting"
    SUBMIT_CHARGE = "Submit_Charge"
    SUBMIT_REFUND = "Submit_Refund"
    SUBMIT_UPDATE = "Submit_Update"
    MOBILE_ADMIN = "Mobile_Admin"


class ProcessingOptions(BaseModel):
    class Meta:
        name = "processingOptions"

    model_config = ConfigDict(defer_build=True)
    is_first_recurring_payment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFirstRecurringPayment",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    is_first_subsequent_auth: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFirstSubsequentAuth",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    is_subsequent_auth: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isSubsequentAuth",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    is_stored_credentials: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isStoredCredentials",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ProfileTransVoidType(BaseModel):
    class Meta:
        name = "profileTransVoidType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_shipping_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class ReturnedItemType(BaseModel):
    class Meta:
        name = "returnedItemType"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    date_utc: XmlDateTime = field(
        metadata={
            "name": "dateUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    date_local: XmlDateTime = field(
        metadata={
            "name": "dateLocal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    code: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class SecurePaymentContainerErrorType(BaseModel):
    class Meta:
        name = "securePaymentContainerErrorType"

    model_config = ConfigDict(defer_build=True)
    code: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class SettingNameEnum(Enum):
    """
    :cvar EMAIL_CUSTOMER: true/false. Used by createTransaction method.
    :cvar MERCHANT_EMAIL: string. Used by createTransaction method.
    :cvar ALLOW_PARTIAL_AUTH: true/false. Used by createTransaction
        method.
    :cvar HEADER_EMAIL_RECEIPT: string. Used by createTransaction
        method.
    :cvar FOOTER_EMAIL_RECEIPT: string. Used by createTransaction
        method.
    :cvar RECURRING_BILLING: true/false. Used by createTransaction
        method.
    :cvar DUPLICATE_WINDOW: number. Used by createTransaction method.
    :cvar TEST_REQUEST: true/false. Used by createTransaction method.
    :cvar HOSTED_PROFILE_RETURN_URL: string. Used by
        getHostedProfilePage method.
    :cvar HOSTED_PROFILE_RETURN_URL_TEXT: string. Used by
        getHostedProfilePage method.
    :cvar HOSTED_PROFILE_PAGE_BORDER_VISIBLE: true/false. Used by
        getHostedProfilePage method.
    :cvar HOSTED_PROFILE_IFRAME_COMMUNICATOR_URL: string. Used by
        getHostedProfilePage method.
    :cvar HOSTED_PROFILE_HEADING_BG_COLOR: #e0e0e0. Used by
        getHostedProfilePage method.
    :cvar HOSTED_PROFILE_VALIDATION_MODE: liveMode/testMode liveMode:
        generates a transaction to the processor in the amount of 0.01
        or 0.00. is immediately voided, if successful. testMode:
        performs field validation only, all fields are validated except
        unrestricted field definitions (viz. telephone number) do not
        generate errors. If a validation transaction is unsuccessful,
        the profile is not created, and the merchant receives an error.
    :cvar HOSTED_PROFILE_BILLING_ADDRESS_REQUIRED: true/false. If true,
        sets First Name, Last Name, Address, City, State, and Zip Code
        as required fields in order for a payment profile to be created
        or updated within a hosted CIM form.
    :cvar HOSTED_PROFILE_CARD_CODE_REQUIRED: true/false. If true, sets
        the Card Code field as required in order for a payment profile
        to be created or updated within a hosted CIM form.
    :cvar HOSTED_PROFILE_BILLING_ADDRESS_OPTIONS:
        showBillingAddress/showNone showBillingAddress: Allow merchant
        to show billing address. showNone : Hide billing address and
        billing name.
    :cvar HOSTED_PROFILE_MANAGE_OPTIONS:
        showAll/showPayment/ShowShipping showAll: Shipping and Payment
        profiles are shown on the manage page, this is the default.
        showPayment : Only Payment profiles are shown on the manage
        page. showShipping : Only Shippiung profiles are shown on the
        manage page.
    :cvar HOSTED_PAYMENT_IFRAME_COMMUNICATOR_URL: JSON string. Used by
        getHostedPaymentPage method.
    :cvar HOSTED_PAYMENT_BUTTON_OPTIONS: JSON string. Used by
        getHostedPaymentPage method.
    :cvar HOSTED_PAYMENT_RETURN_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_ORDER_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_PAYMENT_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_BILLING_ADDRESS_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_SHIPPING_ADDRESS_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_SECURITY_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_CUSTOMER_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar HOSTED_PAYMENT_STYLE_OPTIONS: JSON string. Used by
        getHostedPaymentPage method
    :cvar TYPE_EMAIL_RECEIPT: JSON string. Used by
        sendCustomerTransactionReceipt method
    :cvar HOSTED_PROFILE_PAYMENT_OPTIONS:
        showAll/showCreditCard/showBankAccount showAll: both CreditCard
        and BankAccount sections will be shown on Add payment page, this
        is the default. showCreditCard :only CreditCard payment form
        will be shown on Add payment page. showBankAccount :only
        BankAccount payment form will be shown on Add payment page.
    :cvar HOSTED_PROFILE_SAVE_BUTTON_TEXT: string. Used by
        getHostedProfilePage method to accept button text configuration.
    :cvar HOSTED_PAYMENT_VISA_CHECKOUT_OPTIONS: string. Used by
        getHostedPaymentPage method to accept VisaCheckout
        configuration.
    """

    EMAIL_CUSTOMER = "emailCustomer"
    MERCHANT_EMAIL = "merchantEmail"
    ALLOW_PARTIAL_AUTH = "allowPartialAuth"
    HEADER_EMAIL_RECEIPT = "headerEmailReceipt"
    FOOTER_EMAIL_RECEIPT = "footerEmailReceipt"
    RECURRING_BILLING = "recurringBilling"
    DUPLICATE_WINDOW = "duplicateWindow"
    TEST_REQUEST = "testRequest"
    HOSTED_PROFILE_RETURN_URL = "hostedProfileReturnUrl"
    HOSTED_PROFILE_RETURN_URL_TEXT = "hostedProfileReturnUrlText"
    HOSTED_PROFILE_PAGE_BORDER_VISIBLE = "hostedProfilePageBorderVisible"
    HOSTED_PROFILE_IFRAME_COMMUNICATOR_URL = "hostedProfileIFrameCommunicatorUrl"
    HOSTED_PROFILE_HEADING_BG_COLOR = "hostedProfileHeadingBgColor"
    HOSTED_PROFILE_VALIDATION_MODE = "hostedProfileValidationMode"
    HOSTED_PROFILE_BILLING_ADDRESS_REQUIRED = "hostedProfileBillingAddressRequired"
    HOSTED_PROFILE_CARD_CODE_REQUIRED = "hostedProfileCardCodeRequired"
    HOSTED_PROFILE_BILLING_ADDRESS_OPTIONS = "hostedProfileBillingAddressOptions"
    HOSTED_PROFILE_MANAGE_OPTIONS = "hostedProfileManageOptions"
    HOSTED_PAYMENT_IFRAME_COMMUNICATOR_URL = "hostedPaymentIFrameCommunicatorUrl"
    HOSTED_PAYMENT_BUTTON_OPTIONS = "hostedPaymentButtonOptions"
    HOSTED_PAYMENT_RETURN_OPTIONS = "hostedPaymentReturnOptions"
    HOSTED_PAYMENT_ORDER_OPTIONS = "hostedPaymentOrderOptions"
    HOSTED_PAYMENT_PAYMENT_OPTIONS = "hostedPaymentPaymentOptions"
    HOSTED_PAYMENT_BILLING_ADDRESS_OPTIONS = "hostedPaymentBillingAddressOptions"
    HOSTED_PAYMENT_SHIPPING_ADDRESS_OPTIONS = "hostedPaymentShippingAddressOptions"
    HOSTED_PAYMENT_SECURITY_OPTIONS = "hostedPaymentSecurityOptions"
    HOSTED_PAYMENT_CUSTOMER_OPTIONS = "hostedPaymentCustomerOptions"
    HOSTED_PAYMENT_STYLE_OPTIONS = "hostedPaymentStyleOptions"
    TYPE_EMAIL_RECEIPT = "typeEmailReceipt"
    HOSTED_PROFILE_PAYMENT_OPTIONS = "hostedProfilePaymentOptions"
    HOSTED_PROFILE_SAVE_BUTTON_TEXT = "hostedProfileSaveButtonText"
    HOSTED_PAYMENT_VISA_CHECKOUT_OPTIONS = "hostedPaymentVisaCheckoutOptions"


class SettingType(BaseModel):
    class Meta:
        name = "settingType"

    model_config = ConfigDict(defer_build=True)
    setting_name: Optional[SettingNameEnum] = field(
        default=None,
        metadata={
            "name": "settingName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    setting_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "settingValue",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class SettlementStateEnum(Enum):
    SETTLED_SUCCESSFULLY = "settledSuccessfully"
    SETTLEMENT_ERROR = "settlementError"
    PENDING_SETTLEMENT = "pendingSettlement"


class SolutionType(BaseModel):
    class Meta:
        name = "solutionType"

    model_config = ConfigDict(defer_build=True)
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    vendor_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "vendorName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class SplitTenderStatusEnum(Enum):
    COMPLETED = "completed"
    HELD = "held"
    VOIDED = "voided"


class SubMerchantType(BaseModel):
    class Meta:
        name = "subMerchantType"

    model_config = ConfigDict(defer_build=True)
    identifier: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 40,
        }
    )
    doing_business_as: Optional[str] = field(
        default=None,
        metadata={
            "name": "doingBusinessAs",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    payment_service_provider_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "paymentServiceProviderName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    payment_service_facilitator: Optional[str] = field(
        default=None,
        metadata={
            "name": "paymentServiceFacilitator",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    street_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "streetAddress",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postalCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 30,
        },
    )
    region_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "regionCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 10,
        },
    )
    country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 10,
        },
    )


class SubscriptionPaymentType(BaseModel):
    class Meta:
        name = "subscriptionPaymentType"

    model_config = ConfigDict(defer_build=True)
    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": 0,
        }
    )
    pay_num: int = field(
        metadata={
            "name": "payNum",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": 0,
        }
    )


class TokenMaskedType(BaseModel):
    class Meta:
        name = "tokenMaskedType"

    model_config = ConfigDict(defer_build=True)
    token_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenSource",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    token_number: str = field(
        metadata={
            "name": "tokenNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    expiration_date: str = field(
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )
    token_requestor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenRequestorId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class TransRetailInfoType(BaseModel):
    class Meta:
        name = "transRetailInfoType"

    model_config = ConfigDict(defer_build=True)
    market_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    device_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "deviceType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerSignature",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    terminal_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "terminalNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class TransactionStatusEnum(Enum):
    AUTHORIZED_PENDING_CAPTURE = "authorizedPendingCapture"
    CAPTURED_PENDING_SETTLEMENT = "capturedPendingSettlement"
    COMMUNICATION_ERROR = "communicationError"
    REFUND_SETTLED_SUCCESSFULLY = "refundSettledSuccessfully"
    REFUND_PENDING_SETTLEMENT = "refundPendingSettlement"
    APPROVED_REVIEW = "approvedReview"
    DECLINED = "declined"
    COULD_NOT_VOID = "couldNotVoid"
    EXPIRED = "expired"
    GENERAL_ERROR = "generalError"
    PENDING_FINAL_SETTLEMENT = "pendingFinalSettlement"
    PENDING_SETTLEMENT = "pendingSettlement"
    FAILED_REVIEW = "failedReview"
    SETTLED_SUCCESSFULLY = "settledSuccessfully"
    SETTLEMENT_ERROR = "settlementError"
    UNDER_REVIEW = "underReview"
    UPDATING_SETTLEMENT = "updatingSettlement"
    VOIDED = "voided"
    FDSPENDING_REVIEW = "FDSPendingReview"
    FDSAUTHORIZED_PENDING_REVIEW = "FDSAuthorizedPendingReview"
    RETURNED_ITEM = "returnedItem"
    CHARGEBACK = "chargeback"
    CHARGEBACK_REVERSAL = "chargebackReversal"
    AUTHORIZED_PENDING_RELEASE = "authorizedPendingRelease"


class TransactionTypeEnum(Enum):
    AUTH_ONLY_TRANSACTION = "authOnlyTransaction"
    AUTH_CAPTURE_TRANSACTION = "authCaptureTransaction"
    CAPTURE_ONLY_TRANSACTION = "captureOnlyTransaction"
    REFUND_TRANSACTION = "refundTransaction"
    PRIOR_AUTH_CAPTURE_TRANSACTION = "priorAuthCaptureTransaction"
    VOID_TRANSACTION = "voidTransaction"
    GET_DETAILS_TRANSACTION = "getDetailsTransaction"
    AUTH_ONLY_CONTINUE_TRANSACTION = "authOnlyContinueTransaction"
    AUTH_CAPTURE_CONTINUE_TRANSACTION = "authCaptureContinueTransaction"


class UserField(BaseModel):
    class Meta:
        name = "userField"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ValidationModeEnum(Enum):
    NONE = "none"
    TEST_MODE = "testMode"
    LIVE_MODE = "liveMode"
    OLD_LIVE_MODE = "oldLiveMode"


class WebCheckOutDataTypeToken(BaseModel):
    class Meta:
        name = "webCheckOutDataTypeToken"

    model_config = ConfigDict(defer_build=True)
    card_number: str = field(
        metadata={
            "name": "cardNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 16,
        }
    )
    expiration_date: str = field(
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )
    card_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 3,
            "max_length": 4,
            "pattern": r"[0-9]+",
        },
    )
    zip: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )
    full_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fullName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 1,
            "max_length": 64,
        },
    )


class WebCheckOutTypeEnum(Enum):
    PAN = "PAN"
    TOKEN = "TOKEN"


class ArbgetSubscriptionListSorting(BaseModel):
    class Meta:
        name = "ARBGetSubscriptionListSorting"

    model_config = ConfigDict(defer_build=True)
    order_by: ArbgetSubscriptionListOrderFieldEnum = field(
        metadata={
            "name": "orderBy",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    order_descending: bool = field(
        metadata={
            "name": "orderDescending",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class ArbtransactionList(BaseModel):
    class Meta:
        name = "ARBTransactionList"

    model_config = ConfigDict(defer_build=True)
    arb_transaction: list[ArbTransaction] = field(
        default_factory=list,
        metadata={
            "name": "arbTransaction",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfAuresponseType(BaseModel):
    class Meta:
        name = "ArrayOfAUResponseType"

    model_config = ConfigDict(defer_build=True)
    au_response: list[AuResponseType] = field(
        default_factory=list,
        metadata={
            "name": "auResponse",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfBatchStatisticType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    statistic: list[BatchStatisticType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfContactDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    contact_detail: list[ContactDetailType] = field(
        default_factory=list,
        metadata={
            "name": "contactDetail",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfFdsfilter(BaseModel):
    class Meta:
        name = "ArrayOfFDSFilter"

    model_config = ConfigDict(defer_build=True)
    fdsfilter: list[FdsfilterType] = field(
        default_factory=list,
        metadata={
            "name": "FDSFilter",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfLineItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    line_item: list[LineItemType] = field(
        default_factory=list,
        metadata={
            "name": "lineItem",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfPaymentMethod(BaseModel):
    model_config = ConfigDict(defer_build=True)
    payment_method: list[PaymentMethodsTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentMethod",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "nillable": True,
        },
    )


class ArrayOfPermissionType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    permission: list[PermissionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfReturnedItem(BaseModel):
    model_config = ConfigDict(defer_build=True)
    returned_item: list[ReturnedItemType] = field(
        default_factory=list,
        metadata={
            "name": "returnedItem",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfSetting(BaseModel):
    model_config = ConfigDict(defer_build=True)
    setting: list[SettingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerPaymentProfileSorting(BaseModel):
    model_config = ConfigDict(defer_build=True)
    order_by: CustomerPaymentProfileOrderFieldEnum = field(
        metadata={
            "name": "orderBy",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    order_descending: bool = field(
        metadata={
            "name": "orderDescending",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class KeyManagementScheme(BaseModel):
    model_config = ConfigDict(defer_build=True)
    dukpt: "KeyManagementScheme.Dukpt" = field(
        metadata={
            "name": "DUKPT",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )

    class Dukpt(BaseModel):
        model_config = ConfigDict(defer_build=True)
        operation: OperationType = field(
            metadata={
                "name": "Operation",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )
        mode: "KeyManagementScheme.Dukpt.Mode" = field(
            metadata={
                "name": "Mode",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )
        device_info: "KeyManagementScheme.Dukpt.DeviceInfo" = field(
            metadata={
                "name": "DeviceInfo",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )
        encrypted_data: "KeyManagementScheme.Dukpt.EncryptedData" = field(
            metadata={
                "name": "EncryptedData",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )

        class Mode(BaseModel):
            model_config = ConfigDict(defer_build=True)
            pin: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PIN",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            data: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Data",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )

        class DeviceInfo(BaseModel):
            model_config = ConfigDict(defer_build=True)
            description: str = field(
                metadata={
                    "name": "Description",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                    "required": True,
                }
            )

        class EncryptedData(BaseModel):
            model_config = ConfigDict(defer_build=True)
            value: str = field(
                metadata={
                    "name": "Value",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                    "required": True,
                }
            )


class SubscriptionDetail(BaseModel):
    model_config = ConfigDict(defer_build=True)
    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    status: ArbsubscriptionStatusEnum = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    create_time_stamp_utc: XmlDateTime = field(
        metadata={
            "name": "createTimeStampUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    total_occurrences: int = field(
        metadata={
            "name": "totalOccurrences",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    past_occurrences: int = field(
        metadata={
            "name": "pastOccurrences",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    payment_method: PaymentMethodEnum = field(
        metadata={
            "name": "paymentMethod",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "accountNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    invoice: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    amount: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_profile_id: int = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer_payment_profile_id: int = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer_shipping_profile_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "customerShippingProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class TransactionListSorting(BaseModel):
    model_config = ConfigDict(defer_build=True)
    order_by: TransactionListOrderFieldEnum = field(
        metadata={
            "name": "orderBy",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    order_descending: bool = field(
        metadata={
            "name": "orderDescending",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class AuthorizationIndicatorType(BaseModel):
    class Meta:
        name = "authorizationIndicatorType"

    model_config = ConfigDict(defer_build=True)
    authorization_indicator: Optional[AuthIndicatorEnum] = field(
        default=None,
        metadata={
            "name": "authorizationIndicator",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class BankAccountMaskedType(BaseModel):
    class Meta:
        name = "bankAccountMaskedType"

    model_config = ConfigDict(defer_build=True)
    account_type: Optional[BankAccountTypeEnum] = field(
        default=None,
        metadata={
            "name": "accountType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    routing_number: str = field(
        metadata={
            "name": "routingNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "length": 8,
        }
    )
    account_number: str = field(
        metadata={
            "name": "accountNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "length": 8,
        }
    )
    name_on_account: str = field(
        metadata={
            "name": "nameOnAccount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 22,
        }
    )
    echeck_type: Optional[EcheckTypeEnum] = field(
        default=None,
        metadata={
            "name": "echeckType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )


class BankAccountType(BaseModel):
    class Meta:
        name = "bankAccountType"

    model_config = ConfigDict(defer_build=True)
    account_type: Optional[BankAccountTypeEnum] = field(
        default=None,
        metadata={
            "name": "accountType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    routing_number: str = field(
        metadata={
            "name": "routingNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 9,
        }
    )
    account_number: str = field(
        metadata={
            "name": "accountNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 17,
        }
    )
    name_on_account: str = field(
        metadata={
            "name": "nameOnAccount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 22,
        }
    )
    echeck_type: Optional[EcheckTypeEnum] = field(
        default=None,
        metadata={
            "name": "echeckType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    check_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "checkNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 15,
        },
    )


class CreditCardMaskedType(BaseModel):
    class Meta:
        name = "creditCardMaskedType"

    model_config = ConfigDict(defer_build=True)
    card_number: str = field(
        metadata={
            "name": "cardNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "length": 8,
        }
    )
    expiration_date: str = field(
        metadata={
            "name": "expirationDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )
    card_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_art: Optional[CardArt] = field(
        default=None,
        metadata={
            "name": "cardArt",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    issuer_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "issuerNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "length": 6,
        },
    )
    is_payment_token: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPaymentToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CreditCardType(CreditCardSimpleType):
    class Meta:
        name = "creditCardType"

    model_config = ConfigDict(defer_build=True)
    card_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 3,
            "max_length": 4,
            "pattern": r"[0-9]+",
        },
    )
    is_payment_token: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isPaymentToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    cryptogram: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    token_requestor_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenRequestorName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    token_requestor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenRequestorId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    token_requestor_eci: Optional[str] = field(
        default=None,
        metadata={
            "name": "tokenRequestorEci",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerAddressType(NameAndAddressType):
    class Meta:
        name = "customerAddressType"

    model_config = ConfigDict(defer_build=True)
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "faxNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerDataType(BaseModel):
    class Meta:
        name = "customerDataType"

    model_config = ConfigDict(defer_build=True)
    type_value: Optional[CustomerTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    drivers_license: Optional[DriversLicenseType] = field(
        default=None,
        metadata={
            "name": "driversLicense",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 8,
            "max_length": 9,
        },
    )


class CustomerProfileExType(CustomerProfileBaseType):
    class Meta:
        name = "customerProfileExType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class CustomerProfilePaymentType(BaseModel):
    class Meta:
        name = "customerProfilePaymentType"

    model_config = ConfigDict(defer_build=True)
    create_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "createProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    payment_profile: Optional[PaymentProfile] = field(
        default=None,
        metadata={
            "name": "paymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "shippingProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class CustomerType(BaseModel):
    class Meta:
        name = "customerType"

    model_config = ConfigDict(defer_build=True)
    type_value: Optional[CustomerTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "faxNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    drivers_license: Optional[DriversLicenseType] = field(
        default=None,
        metadata={
            "name": "driversLicense",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 9,
            "max_length": 9,
            "pattern": r"[0-9]+",
        },
    )


class FraudInformationType(BaseModel):
    class Meta:
        name = "fraudInformationType"

    model_config = ConfigDict(defer_build=True)
    fraud_filter_list: ArrayOfFraudFilterType = field(
        metadata={
            "name": "fraudFilterList",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    fraud_action: str = field(
        metadata={
            "name": "fraudAction",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class HeldTransactionRequestType(BaseModel):
    class Meta:
        name = "heldTransactionRequestType"

    model_config = ConfigDict(defer_build=True)
    action: AfdsTransactionEnum = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    ref_trans_id: str = field(
        metadata={
            "name": "refTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class MerchantAuthenticationType(BaseModel):
    class Meta:
        name = "merchantAuthenticationType"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )
    transaction_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "transactionKey",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 16,
        },
    )
    session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    password: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 40,
        },
    )
    impersonation_authentication: Optional[ImpersonationAuthenticationType] = field(
        default=None,
        metadata={
            "name": "impersonationAuthentication",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    finger_print: Optional[FingerPrintType] = field(
        default=None,
        metadata={
            "name": "fingerPrint",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    client_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientKey",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    access_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    mobile_device_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "mobileDeviceId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 60,
        },
    )


class MessagesType(BaseModel):
    class Meta:
        name = "messagesType"

    model_config = ConfigDict(defer_build=True)
    result_code: MessageTypeEnum = field(
        metadata={
            "name": "resultCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    message: list["MessagesType.Message"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_occurs": 1,
        },
    )

    class Message(BaseModel):
        model_config = ConfigDict(defer_build=True)
        code: str = field(
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )
        text: str = field(
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )


class MobileDeviceType(BaseModel):
    class Meta:
        name = "mobileDeviceType"

    model_config = ConfigDict(defer_build=True)
    mobile_device_id: str = field(
        metadata={
            "name": "mobileDeviceId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 60,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 60,
        },
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "phoneNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )
    device_platform: Optional[str] = field(
        default=None,
        metadata={
            "name": "devicePlatform",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
        },
    )
    device_activation: Optional[DeviceActivationEnum] = field(
        default=None,
        metadata={
            "name": "deviceActivation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class OrderExType(OrderType):
    class Meta:
        name = "orderExType"

    model_config = ConfigDict(defer_build=True)
    purchase_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "purchaseOrderNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 25,
        },
    )


class PaymentScheduleType(BaseModel):
    class Meta:
        name = "paymentScheduleType"

    model_config = ConfigDict(defer_build=True)
    interval: Optional["PaymentScheduleType.Interval"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "startDate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    total_occurrences: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalOccurrences",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": 1,
            "max_inclusive": 32000,
        },
    )
    trial_occurrences: Optional[int] = field(
        default=None,
        metadata={
            "name": "trialOccurrences",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": 0,
            "max_inclusive": 32000,
        },
    )

    class Interval(BaseModel):
        model_config = ConfigDict(defer_build=True)
        length: int = field(
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 32000,
            }
        )
        unit: ArbsubscriptionUnitEnum = field(
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "required": True,
            }
        )


class ProcessorType(BaseModel):
    class Meta:
        name = "processorType"

    model_config = ConfigDict(defer_build=True)
    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 255,
        }
    )
    id: int = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    card_types: Optional[ArrayOfCardType] = field(
        default=None,
        metadata={
            "name": "cardTypes",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ProfileTransAmountType(BaseModel):
    class Meta:
        name = "profileTransAmountType"

    model_config = ConfigDict(defer_build=True)
    amount: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.01"),
            "fraction_digits": 4,
        }
    )
    tax: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    duty: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    line_items: list[LineItemType] = field(
        default_factory=list,
        metadata={
            "name": "lineItems",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_occurs": 30,
        },
    )


class SubsequentAuthInformation(BaseModel):
    class Meta:
        name = "subsequentAuthInformation"

    model_config = ConfigDict(defer_build=True)
    original_network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalNetworkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )
    original_auth_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "originalAuthAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    reason: Optional[MerchantInitTransReasonEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class TransactionResponse(BaseModel):
    class Meta:
        name = "transactionResponse"

    model_config = ConfigDict(defer_build=True)
    response_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "responseCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    raw_response_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rawResponseCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    auth_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    avs_result_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "avsResultCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    cvv_result_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cvvResultCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    cavv_result_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cavvResultCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ref_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refTransID",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    trans_hash: Optional[str] = field(
        default=None,
        metadata={
            "name": "transHash",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    test_request: Optional[str] = field(
        default=None,
        metadata={
            "name": "testRequest",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "accountNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    entry_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "entryMode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    account_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "accountType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    split_tender_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "splitTenderId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    pre_paid_card: Optional["TransactionResponse.PrePaidCard"] = field(
        default=None,
        metadata={
            "name": "prePaidCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    message: Optional["TransactionResponse.Messages.Message"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    messages: Optional["TransactionResponse.Messages"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    errors: Optional["TransactionResponse.Errors"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    split_tender_payments: Optional["TransactionResponse.SplitTenderPayments"] = field(
        default=None,
        metadata={
            "name": "splitTenderPayments",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    user_fields: Optional["TransactionResponse.UserFields"] = field(
        default=None,
        metadata={
            "name": "userFields",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    secure_acceptance: Optional["TransactionResponse.SecureAcceptance"] = field(
        default=None,
        metadata={
            "name": "secureAcceptance",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    emv_response: Optional["TransactionResponse.EmvResponse"] = field(
        default=None,
        metadata={
            "name": "emvResponse",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    trans_hash_sha2: Optional[str] = field(
        default=None,
        metadata={
            "name": "transHashSha2",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "networkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )

    class PrePaidCard(BaseModel):
        model_config = ConfigDict(defer_build=True)
        requested_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "requestedAmount",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )
        approved_amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "approvedAmount",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )
        balance_on_card: Optional[str] = field(
            default=None,
            metadata={
                "name": "balanceOnCard",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

    class Messages(BaseModel):
        model_config = ConfigDict(defer_build=True)
        message: list["TransactionResponse.Messages.Message"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

        class Message(BaseModel):
            model_config = ConfigDict(defer_build=True)
            code: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )

    class Errors(BaseModel):
        model_config = ConfigDict(defer_build=True)
        error: list["TransactionResponse.Errors.Error"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

        class Error(BaseModel):
            model_config = ConfigDict(defer_build=True)
            error_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "errorCode",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            error_text: Optional[str] = field(
                default=None,
                metadata={
                    "name": "errorText",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )

    class SplitTenderPayments(BaseModel):
        model_config = ConfigDict(defer_build=True)
        split_tender_payment: list["TransactionResponse.SplitTenderPayments.SplitTenderPayment"] = field(
            default_factory=list,
            metadata={
                "name": "splitTenderPayment",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

        class SplitTenderPayment(BaseModel):
            model_config = ConfigDict(defer_build=True)
            trans_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "transId",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            response_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "responseCode",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            response_to_customer: Optional[str] = field(
                default=None,
                metadata={
                    "name": "responseToCustomer",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            auth_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "authCode",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            account_number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "accountNumber",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            account_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "accountType",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            requested_amount: Optional[str] = field(
                default=None,
                metadata={
                    "name": "requestedAmount",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            approved_amount: Optional[str] = field(
                default=None,
                metadata={
                    "name": "approvedAmount",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )
            balance_on_card: Optional[str] = field(
                default=None,
                metadata={
                    "name": "balanceOnCard",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                },
            )

    class UserFields(BaseModel):
        model_config = ConfigDict(defer_build=True)
        user_field: list[UserField] = field(
            default_factory=list,
            metadata={
                "name": "userField",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "max_occurs": 20,
            },
        )

    class SecureAcceptance(BaseModel):
        model_config = ConfigDict(defer_build=True)
        secure_acceptance_url: Optional[str] = field(
            default=None,
            metadata={
                "name": "SecureAcceptanceUrl",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )
        payer_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "PayerID",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )
        payer_email: Optional[str] = field(
            default=None,
            metadata={
                "name": "PayerEmail",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

    class EmvResponse(BaseModel):
        model_config = ConfigDict(defer_build=True)
        tlv_data: Optional[str] = field(
            default=None,
            metadata={
                "name": "tlvData",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )
        tags: Optional["TransactionResponse.EmvResponse.Tags"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            },
        )

        class Tags(BaseModel):
            model_config = ConfigDict(defer_build=True)
            tag: list[EmvTag] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                    "min_occurs": 1,
                },
            )


class AnetApiRequest(BaseModel):
    class Meta:
        name = "ANetApiRequest"

    model_config = ConfigDict(defer_build=True)
    # This is actually required. Only set to optional so that the client can inject it.
    merchant_authentication: MerchantAuthenticationType = field(
        default=None,
        metadata={
            "name": "merchantAuthentication",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        },
    )
    client_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 30,
        },
    )
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 20,
        },
    )


class AnetApiResponse(BaseModel):
    class Meta:
        name = "ANetApiResponse"

    model_config = ConfigDict(defer_build=True)
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    messages: MessagesType = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    session_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "sessionToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfProcessorType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    processor: list[ProcessorType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "nillable": True,
        },
    )


class ArrayOfSubscription(BaseModel):
    model_config = ConfigDict(defer_build=True)
    subscription_detail: list[SubscriptionDetail] = field(
        default_factory=list,
        metadata={
            "name": "subscriptionDetail",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "nillable": True,
        },
    )


class KeyValue(BaseModel):
    model_config = ConfigDict(defer_build=True)
    encoding: EncodingType = field(
        metadata={
            "name": "Encoding",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    encryption_algorithm: EncryptionAlgorithmType = field(
        metadata={
            "name": "EncryptionAlgorithm",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    scheme: KeyManagementScheme = field(
        metadata={
            "name": "Scheme",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class AuDeleteType(AuDetailsType):
    class Meta:
        name = "auDeleteType"

    model_config = ConfigDict(defer_build=True)
    credit_card: CreditCardMaskedType = field(
        metadata={
            "name": "creditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class AuUpdateType(AuDetailsType):
    class Meta:
        name = "auUpdateType"

    model_config = ConfigDict(defer_build=True)
    new_credit_card: CreditCardMaskedType = field(
        metadata={
            "name": "newCreditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    old_credit_card: CreditCardMaskedType = field(
        metadata={
            "name": "oldCreditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class BatchDetailsType(BaseModel):
    class Meta:
        name = "batchDetailsType"

    model_config = ConfigDict(defer_build=True)
    batch_id: str = field(
        metadata={
            "name": "batchId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    settlement_time_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "settlementTimeUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    settlement_time_local: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "settlementTimeLocal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    settlement_state: str = field(
        metadata={
            "name": "settlementState",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    payment_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "paymentMethod",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    market_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    product: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    statistics: Optional[ArrayOfBatchStatisticType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CreateProfileResponse(BaseModel):
    class Meta:
        name = "createProfileResponse"

    model_config = ConfigDict(defer_build=True)
    messages: MessagesType = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id_list: Optional[ArrayOfNumericString] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileIdList",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_shipping_address_id_list: Optional[ArrayOfNumericString] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressIdList",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerAddressExType(CustomerAddressType):
    class Meta:
        name = "customerAddressExType"

    model_config = ConfigDict(defer_build=True)
    customer_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class CustomerPaymentProfileBaseType(BaseModel):
    class Meta:
        name = "customerPaymentProfileBaseType"

    model_config = ConfigDict(defer_build=True)
    customer_type: Optional[CustomerTypeEnum] = field(
        default=None,
        metadata={
            "name": "customerType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bill_to: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerProfileInfoExType(CustomerProfileExType):
    class Meta:
        name = "customerProfileInfoExType"

    model_config = ConfigDict(defer_build=True)
    profile_type: Optional[CustomerProfileTypeEnum] = field(
        default=None,
        metadata={
            "name": "profileType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class EmailSettingsType(ArrayOfSetting):
    """Allowed values for settingName are: headerEmailReceipt and footerEmailReceipt"""

    class Meta:
        name = "emailSettingsType"

    model_config = ConfigDict(defer_build=True)
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PaymentMaskedType(BaseModel):
    class Meta:
        name = "paymentMaskedType"

    model_config = ConfigDict(defer_build=True)
    credit_card: Optional[CreditCardMaskedType] = field(
        default=None,
        metadata={
            "name": "creditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_account: Optional[BankAccountMaskedType] = field(
        default=None,
        metadata={
            "name": "bankAccount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    token_information: Optional[TokenMaskedType] = field(
        default=None,
        metadata={
            "name": "tokenInformation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class PaymentSimpleType(BaseModel):
    class Meta:
        name = "paymentSimpleType"

    model_config = ConfigDict(defer_build=True)
    credit_card: Optional[CreditCardSimpleType] = field(
        default=None,
        metadata={
            "name": "creditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_account: Optional[BankAccountType] = field(
        default=None,
        metadata={
            "name": "bankAccount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ProfileTransOrderType(ProfileTransAmountType):
    class Meta:
        name = "profileTransOrderType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: str = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_shipping_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    order: Optional[OrderExType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_exempt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxExempt",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    recurring_billing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "recurringBilling",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    card_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 3,
            "max_length": 4,
            "pattern": r"[0-9]+",
        },
    )
    split_tender_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "splitTenderId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    processing_options: Optional[ProcessingOptions] = field(
        default=None,
        metadata={
            "name": "processingOptions",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    subsequent_auth_information: Optional[SubsequentAuthInformation] = field(
        default=None,
        metadata={
            "name": "subsequentAuthInformation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    authorization_indicator_type: Optional[AuthorizationIndicatorType] = field(
        default=None,
        metadata={
            "name": "authorizationIndicatorType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ProfileTransPriorAuthCaptureType(ProfileTransAmountType):
    class Meta:
        name = "profileTransPriorAuthCaptureType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_shipping_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class ProfileTransRefundType(ProfileTransAmountType):
    class Meta:
        name = "profileTransRefundType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_shipping_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    credit_card_number_masked: Optional[str] = field(
        default=None,
        metadata={
            "name": "creditCardNumberMasked",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 8,
            "max_length": 8,
        },
    )
    bank_routing_number_masked: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankRoutingNumberMasked",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 8,
            "max_length": 8,
        },
    )
    bank_account_number_masked: Optional[str] = field(
        default=None,
        metadata={
            "name": "bankAccountNumberMasked",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 8,
            "max_length": 8,
        },
    )
    order: Optional[OrderExType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class TransactionSummaryType(BaseModel):
    class Meta:
        name = "transactionSummaryType"

    model_config = ConfigDict(defer_build=True)
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    submit_time_utc: XmlDateTime = field(
        metadata={
            "name": "submitTimeUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    submit_time_local: XmlDateTime = field(
        metadata={
            "name": "submitTimeLocal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    transaction_status: str = field(
        metadata={
            "name": "transactionStatus",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    invoice_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "invoiceNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "firstName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastName",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    account_type: str = field(
        metadata={
            "name": "accountType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    account_number: str = field(
        metadata={
            "name": "accountNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    settle_amount: Decimal = field(
        metadata={
            "name": "settleAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    market_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    product: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    mobile_device_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "mobileDeviceId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    subscription: Optional[SubscriptionPaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    has_returned_items: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasReturnedItems",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    fraud_information: Optional[FraudInformationType] = field(
        default=None,
        metadata={
            "name": "fraudInformation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class WebCheckOutDataType(BaseModel):
    class Meta:
        name = "webCheckOutDataType"

    model_config = ConfigDict(defer_build=True)
    type_value: WebCheckOutTypeEnum = field(
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        }
    )
    token: Optional[WebCheckOutDataTypeToken] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_token: Optional[BankAccountType] = field(
        default=None,
        metadata={
            "name": "bankToken",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArbcancelSubscriptionRequest(AnetApiRequest):
    class Meta:
        name = "ARBCancelSubscriptionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription_id: str = field(
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class ArbcancelSubscriptionResponse(AnetApiResponse):
    class Meta:
        name = "ARBCancelSubscriptionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class ArbcreateSubscriptionResponse(AnetApiResponse):
    class Meta:
        name = "ARBCreateSubscriptionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ArbgetSubscriptionListRequest(AnetApiRequest):
    class Meta:
        name = "ARBGetSubscriptionListRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    search_type: ArbgetSubscriptionListSearchTypeEnum = field(
        metadata={
            "name": "searchType",
            "type": "Element",
            "required": True,
        }
    )
    sorting: Optional[ArbgetSubscriptionListSorting] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ArbgetSubscriptionListResponse(AnetApiResponse):
    class Meta:
        name = "ARBGetSubscriptionListResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    total_num_in_result_set: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumInResultSet",
            "type": "Element",
        },
    )
    subscription_details: Optional[ArrayOfSubscription] = field(
        default=None,
        metadata={
            "name": "subscriptionDetails",
            "type": "Element",
        },
    )


class ArbgetSubscriptionRequest(AnetApiRequest):
    class Meta:
        name = "ARBGetSubscriptionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription_id: str = field(
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    include_transactions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "includeTransactions",
            "type": "Element",
        },
    )


class ArbgetSubscriptionStatusRequest(AnetApiRequest):
    class Meta:
        name = "ARBGetSubscriptionStatusRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription_id: str = field(
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class ArbgetSubscriptionStatusResponse(AnetApiResponse):
    class Meta:
        name = "ARBGetSubscriptionStatusResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    status: Optional[ArbsubscriptionStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ArbupdateSubscriptionResponse(AnetApiResponse):
    class Meta:
        name = "ARBUpdateSubscriptionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class ArrayOfBatchDetailsType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    batch: list[BatchDetailsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArrayOfTransactionSummaryType(BaseModel):
    model_config = ConfigDict(defer_build=True)
    transaction: list[TransactionSummaryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class EnumCollection(BaseModel):
    class Meta:
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_summary_type: CustomerProfileSummaryType = field(
        metadata={
            "name": "customerProfileSummaryType",
            "type": "Element",
            "required": True,
        }
    )
    payment_simple_type: PaymentSimpleType = field(
        metadata={
            "name": "paymentSimpleType",
            "type": "Element",
            "required": True,
        }
    )
    account_type_enum: AccountTypeEnum = field(
        metadata={
            "name": "accountTypeEnum",
            "type": "Element",
            "required": True,
        }
    )
    card_type_enum: CardTypeEnum = field(
        metadata={
            "name": "cardTypeEnum",
            "type": "Element",
            "required": True,
        }
    )
    fdsfilter_action_enum: FdsfilterActionEnum = field(
        metadata={
            "name": "FDSFilterActionEnum",
            "type": "Element",
            "required": True,
        }
    )
    permissions_enum: PermissionsEnum = field(
        metadata={
            "name": "permissionsEnum",
            "type": "Element",
            "required": True,
        }
    )
    setting_name_enum: SettingNameEnum = field(
        metadata={
            "name": "settingNameEnum",
            "type": "Element",
            "required": True,
        }
    )
    settlement_state_enum: SettlementStateEnum = field(
        metadata={
            "name": "settlementStateEnum",
            "type": "Element",
            "required": True,
        }
    )
    transaction_status_enum: TransactionStatusEnum = field(
        metadata={
            "name": "transactionStatusEnum",
            "type": "Element",
            "required": True,
        }
    )
    transaction_type_enum: TransactionTypeEnum = field(
        metadata={
            "name": "transactionTypeEnum",
            "type": "Element",
            "required": True,
        }
    )


class ErrorResponse(AnetApiResponse):
    class Meta:
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class KeyBlock(BaseModel):
    model_config = ConfigDict(defer_build=True)
    value: KeyValue = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class ListOfAudetailsType(BaseModel):
    class Meta:
        name = "ListOfAUDetailsType"

    model_config = ConfigDict(defer_build=True)
    au_update: list[AuUpdateType] = field(
        default_factory=list,
        metadata={
            "name": "auUpdate",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    au_delete: list[AuDeleteType] = field(
        default_factory=list,
        metadata={
            "name": "auDelete",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class AuthenticateTestRequest(AnetApiRequest):
    class Meta:
        name = "authenticateTestRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class AuthenticateTestResponse(AnetApiResponse):
    class Meta:
        name = "authenticateTestResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class CreateCustomerPaymentProfileResponse(AnetApiResponse):
    class Meta:
        name = "createCustomerPaymentProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    validation_direct_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "validationDirectResponse",
            "type": "Element",
            "max_length": 2048,
        },
    )


class CreateCustomerProfileFromTransactionRequest(AnetApiRequest):
    class Meta:
        name = "createCustomerProfileFromTransactionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer: Optional[CustomerProfileBaseType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    default_payment_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultPaymentProfile",
            "type": "Element",
        },
    )
    default_shipping_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultShippingAddress",
            "type": "Element",
        },
    )
    profile_type: Optional[CustomerProfileTypeEnum] = field(
        default=None,
        metadata={
            "name": "profileType",
            "type": "Element",
        },
    )


class CreateCustomerProfileResponse(AnetApiResponse):
    class Meta:
        name = "createCustomerProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id_list: ArrayOfNumericString = field(
        metadata={
            "name": "customerPaymentProfileIdList",
            "type": "Element",
            "required": True,
        }
    )
    customer_shipping_address_id_list: ArrayOfNumericString = field(
        metadata={
            "name": "customerShippingAddressIdList",
            "type": "Element",
            "required": True,
        }
    )
    validation_direct_response_list: ArrayOfString = field(
        metadata={
            "name": "validationDirectResponseList",
            "type": "Element",
            "required": True,
        }
    )


class CreateCustomerProfileTransactionResponse(AnetApiResponse):
    class Meta:
        name = "createCustomerProfileTransactionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction_response: Optional[TransactionResponse] = field(
        default=None,
        metadata={
            "name": "transactionResponse",
            "type": "Element",
        },
    )
    direct_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "directResponse",
            "type": "Element",
            "max_length": 2048,
        },
    )


class CreateCustomerShippingAddressRequest(AnetApiRequest):
    class Meta:
        name = "createCustomerShippingAddressRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    address: CustomerAddressType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    default_shipping_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultShippingAddress",
            "type": "Element",
        },
    )


class CreateCustomerShippingAddressResponse(AnetApiResponse):
    class Meta:
        name = "createCustomerShippingAddressResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    customer_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAddressId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )


class CreateTransactionResponse(AnetApiResponse):
    class Meta:
        name = "createTransactionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction_response: TransactionResponse = field(
        metadata={
            "name": "transactionResponse",
            "type": "Element",
            "required": True,
        }
    )
    profile_response: Optional[CreateProfileResponse] = field(
        default=None,
        metadata={
            "name": "profileResponse",
            "type": "Element",
        },
    )


class CustomerPaymentProfileListItemType(BaseModel):
    class Meta:
        name = "customerPaymentProfileListItemType"

    model_config = ConfigDict(defer_build=True)
    default_payment_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultPaymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_payment_profile_id: int = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer_profile_id: int = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    bill_to: CustomerAddressType = field(
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    payment: PaymentMaskedType = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    original_network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalNetworkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )
    original_auth_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "originalAuthAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    exclude_from_account_updater: Optional[bool] = field(
        default=None,
        metadata={
            "name": "excludeFromAccountUpdater",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerPaymentProfileMaskedType(CustomerPaymentProfileBaseType):
    class Meta:
        name = "customerPaymentProfileMaskedType"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    customer_payment_profile_id: str = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    default_payment_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultPaymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    payment: Optional[PaymentMaskedType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    drivers_license: Optional[DriversLicenseMaskedType] = field(
        default=None,
        metadata={
            "name": "driversLicense",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "length": 8,
        },
    )
    subscription_ids: Optional[SubscriptionIdList] = field(
        default=None,
        metadata={
            "name": "subscriptionIds",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    original_network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalNetworkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )
    original_auth_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "originalAuthAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    exclude_from_account_updater: Optional[bool] = field(
        default=None,
        metadata={
            "name": "excludeFromAccountUpdater",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class DecryptPaymentDataRequest(AnetApiRequest):
    class Meta:
        name = "decryptPaymentDataRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    opaque_data: OpaqueDataType = field(
        metadata={
            "name": "opaqueData",
            "type": "Element",
            "required": True,
        }
    )
    call_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "callId",
            "type": "Element",
        },
    )


class DecryptPaymentDataResponse(AnetApiResponse):
    class Meta:
        name = "decryptPaymentDataResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    shipping_info: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "shippingInfo",
            "type": "Element",
        },
    )
    billing_info: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "billingInfo",
            "type": "Element",
        },
    )
    card_info: Optional[CreditCardMaskedType] = field(
        default=None,
        metadata={
            "name": "cardInfo",
            "type": "Element",
        },
    )
    payment_details: Optional[PaymentDetails] = field(
        default=None,
        metadata={
            "name": "paymentDetails",
            "type": "Element",
        },
    )


class DeleteCustomerPaymentProfileRequest(AnetApiRequest):
    class Meta:
        name = "deleteCustomerPaymentProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: str = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class DeleteCustomerPaymentProfileResponse(AnetApiResponse):
    class Meta:
        name = "deleteCustomerPaymentProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class DeleteCustomerProfileRequest(AnetApiRequest):
    class Meta:
        name = "deleteCustomerProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class DeleteCustomerProfileResponse(AnetApiResponse):
    class Meta:
        name = "deleteCustomerProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class DeleteCustomerShippingAddressRequest(AnetApiRequest):
    class Meta:
        name = "deleteCustomerShippingAddressRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_address_id: str = field(
        metadata={
            "name": "customerAddressId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class DeleteCustomerShippingAddressResponse(AnetApiResponse):
    class Meta:
        name = "deleteCustomerShippingAddressResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class GetAujobDetailsRequest(AnetApiRequest):
    class Meta:
        name = "getAUJobDetailsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    month: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )
    modified_type_filter: Optional[AujobTypeEnum] = field(
        default=None,
        metadata={
            "name": "modifiedTypeFilter",
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class GetAujobSummaryRequest(AnetApiRequest):
    class Meta:
        name = "getAUJobSummaryRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    month: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )


class GetAujobSummaryResponse(AnetApiResponse):
    class Meta:
        name = "getAUJobSummaryResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    au_summary: Optional[ArrayOfAuresponseType] = field(
        default=None,
        metadata={
            "name": "auSummary",
            "type": "Element",
        },
    )


class GetBatchStatisticsRequest(AnetApiRequest):
    class Meta:
        name = "getBatchStatisticsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    batch_id: str = field(
        metadata={
            "name": "batchId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class GetBatchStatisticsResponse(AnetApiResponse):
    class Meta:
        name = "getBatchStatisticsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    batch: Optional[BatchDetailsType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class GetCustomerPaymentProfileListRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerPaymentProfileListRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    search_type: CustomerPaymentProfileSearchTypeEnum = field(
        metadata={
            "name": "searchType",
            "type": "Element",
            "required": True,
        }
    )
    month: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 4,
            "max_length": 7,
        }
    )
    sorting: Optional[CustomerPaymentProfileSorting] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class GetCustomerPaymentProfileNonceRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerPaymentProfileNonceRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    connected_access_token: str = field(
        metadata={
            "name": "connectedAccessToken",
            "type": "Element",
            "required": True,
        }
    )
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: str = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class GetCustomerPaymentProfileNonceResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerPaymentProfileNonceResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    opaque_data: Optional[OpaqueDataType] = field(
        default=None,
        metadata={
            "name": "opaqueData",
            "type": "Element",
        },
    )


class GetCustomerPaymentProfileRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerPaymentProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    unmask_expiration_date: Optional[bool] = field(
        default=None,
        metadata={
            "name": "unmaskExpirationDate",
            "type": "Element",
        },
    )
    include_issuer_info: Optional[bool] = field(
        default=None,
        metadata={
            "name": "includeIssuerInfo",
            "type": "Element",
        },
    )


class GetCustomerProfileIdsRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerProfileIdsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class GetCustomerProfileIdsResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerProfileIdsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    ids: ArrayOfNumericString = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class GetCustomerProfileRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    merchant_customer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantCustomerId",
            "type": "Element",
            "max_length": 20,
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    unmask_expiration_date: Optional[bool] = field(
        default=None,
        metadata={
            "name": "unmaskExpirationDate",
            "type": "Element",
        },
    )
    include_issuer_info: Optional[bool] = field(
        default=None,
        metadata={
            "name": "includeIssuerInfo",
            "type": "Element",
        },
    )


class GetCustomerShippingAddressRequest(AnetApiRequest):
    class Meta:
        name = "getCustomerShippingAddressRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerAddressId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )


class GetCustomerShippingAddressResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerShippingAddressResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    default_shipping_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultShippingAddress",
            "type": "Element",
        },
    )
    address: Optional[CustomerAddressExType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subscription_ids: Optional[SubscriptionIdList] = field(
        default=None,
        metadata={
            "name": "subscriptionIds",
            "type": "Element",
        },
    )


class GetHostedPaymentPageResponse(AnetApiResponse):
    class Meta:
        name = "getHostedPaymentPageResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    token: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class GetHostedProfilePageRequest(AnetApiRequest):
    """
    :ivar customer_profile_id:
    :ivar hosted_profile_settings: Allowed values for settingName are:
        hostedProfileReturnUrl, hostedProfileReturnUrlText,
        hostedProfilePageBorderVisible,
        hostedProfileIFrameCommunicatorUrl, hostedProfileHeadingBgColor,
        hostedProfileBillingAddressRequired,
        hostedProfileCardCodeRequired,
        hostedProfileBillingAddressOptions, hostedProfileManageOptions,
        hostedProfilePaymentOptions, hostedProfileSaveButtonText.
    """

    class Meta:
        name = "getHostedProfilePageRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    hosted_profile_settings: Optional[ArrayOfSetting] = field(
        default=None,
        metadata={
            "name": "hostedProfileSettings",
            "type": "Element",
        },
    )


class GetHostedProfilePageResponse(AnetApiResponse):
    class Meta:
        name = "getHostedProfilePageResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    token: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class GetMerchantDetailsRequest(AnetApiRequest):
    class Meta:
        name = "getMerchantDetailsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class GetMerchantDetailsResponse(AnetApiResponse):
    class Meta:
        name = "getMerchantDetailsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    is_test_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isTestMode",
            "type": "Element",
        },
    )
    processors: ArrayOfProcessorType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    merchant_name: str = field(
        metadata={
            "name": "merchantName",
            "type": "Element",
            "required": True,
        }
    )
    gateway_id: str = field(
        metadata={
            "name": "gatewayId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    market_types: ArrayOfMarketType = field(
        metadata={
            "name": "marketTypes",
            "type": "Element",
            "required": True,
        }
    )
    product_codes: ArrayOfProductCode = field(
        metadata={
            "name": "productCodes",
            "type": "Element",
            "required": True,
        }
    )
    payment_methods: ArrayOfPaymentMethod = field(
        metadata={
            "name": "paymentMethods",
            "type": "Element",
            "required": True,
        }
    )
    currencies: ArrayOfCurrencyCode = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    public_client_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "publicClientKey",
            "type": "Element",
        },
    )
    business_information: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "businessInformation",
            "type": "Element",
        },
    )
    merchant_time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantTimeZone",
            "type": "Element",
            "max_length": 100,
        },
    )
    contact_details: Optional[ArrayOfContactDetail] = field(
        default=None,
        metadata={
            "name": "contactDetails",
            "type": "Element",
        },
    )


class GetSettledBatchListRequest(AnetApiRequest):
    class Meta:
        name = "getSettledBatchListRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    include_statistics: Optional[bool] = field(
        default=None,
        metadata={
            "name": "includeStatistics",
            "type": "Element",
        },
    )
    first_settlement_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "firstSettlementDate",
            "type": "Element",
        },
    )
    last_settlement_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastSettlementDate",
            "type": "Element",
        },
    )


class GetTransactionDetailsRequest(AnetApiRequest):
    class Meta:
        name = "getTransactionDetailsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )


class GetTransactionListForCustomerRequest(AnetApiRequest):
    class Meta:
        name = "getTransactionListForCustomerRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    sorting: Optional[TransactionListSorting] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class GetTransactionListRequest(AnetApiRequest):
    class Meta:
        name = "getTransactionListRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    batch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "batchId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    sorting: Optional[TransactionListSorting] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class GetUnsettledTransactionListRequest(AnetApiRequest):
    class Meta:
        name = "getUnsettledTransactionListRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    status: Optional[TransactionGroupStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sorting: Optional[TransactionListSorting] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    paging: Optional[Paging] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class IsAliveResponse(AnetApiResponse):
    class Meta:
        name = "isAliveResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class LogoutRequest(AnetApiRequest):
    class Meta:
        name = "logoutRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class LogoutResponse(AnetApiResponse):
    class Meta:
        name = "logoutResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class MobileDeviceLoginRequest(AnetApiRequest):
    class Meta:
        name = "mobileDeviceLoginRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class MobileDeviceLoginResponse(AnetApiResponse):
    class Meta:
        name = "mobileDeviceLoginResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    merchant_contact: MerchantContactType = field(
        metadata={
            "name": "merchantContact",
            "type": "Element",
            "required": True,
        }
    )
    user_permissions: ArrayOfPermissionType = field(
        metadata={
            "name": "userPermissions",
            "type": "Element",
            "required": True,
        }
    )
    merchant_account: Optional[TransRetailInfoType] = field(
        default=None,
        metadata={
            "name": "merchantAccount",
            "type": "Element",
        },
    )


class MobileDeviceRegistrationRequest(AnetApiRequest):
    class Meta:
        name = "mobileDeviceRegistrationRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    mobile_device: MobileDeviceType = field(
        metadata={
            "name": "mobileDevice",
            "type": "Element",
            "required": True,
        }
    )


class MobileDeviceRegistrationResponse(AnetApiResponse):
    class Meta:
        name = "mobileDeviceRegistrationResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class ProfileTransAuthCaptureType(ProfileTransOrderType):
    class Meta:
        name = "profileTransAuthCaptureType"

    model_config = ConfigDict(defer_build=True)


class ProfileTransAuthOnlyType(ProfileTransOrderType):
    class Meta:
        name = "profileTransAuthOnlyType"

    model_config = ConfigDict(defer_build=True)


class ProfileTransCaptureOnlyType(ProfileTransOrderType):
    class Meta:
        name = "profileTransCaptureOnlyType"

    model_config = ConfigDict(defer_build=True)
    approval_code: str = field(
        metadata={
            "name": "approvalCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "max_length": 6,
        }
    )


class SecurePaymentContainerRequest(AnetApiRequest):
    class Meta:
        name = "securePaymentContainerRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    data: WebCheckOutDataType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class SecurePaymentContainerResponse(AnetApiResponse):
    class Meta:
        name = "securePaymentContainerResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    opaque_data: OpaqueDataType = field(
        metadata={
            "name": "opaqueData",
            "type": "Element",
            "required": True,
        }
    )


class SendCustomerTransactionReceiptRequest(AnetApiRequest):
    class Meta:
        name = "sendCustomerTransactionReceiptRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_email: str = field(
        metadata={
            "name": "customerEmail",
            "type": "Element",
            "required": True,
        }
    )
    email_settings: Optional[EmailSettingsType] = field(
        default=None,
        metadata={
            "name": "emailSettings",
            "type": "Element",
        },
    )


class SendCustomerTransactionReceiptResponse(AnetApiResponse):
    class Meta:
        name = "sendCustomerTransactionReceiptResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class TransactionDetailsType(BaseModel):
    class Meta:
        name = "transactionDetailsType"

    model_config = ConfigDict(defer_build=True)
    trans_id: str = field(
        metadata={
            "name": "transId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    ref_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    split_tender_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "splitTenderId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )
    submit_time_utc: XmlDateTime = field(
        metadata={
            "name": "submitTimeUTC",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    submit_time_local: XmlDateTime = field(
        metadata={
            "name": "submitTimeLocal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    transaction_type: TransactionTypeEnum = field(
        metadata={
            "name": "transactionType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    transaction_status: str = field(
        metadata={
            "name": "transactionStatus",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    response_code: int = field(
        metadata={
            "name": "responseCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    response_reason_code: int = field(
        metadata={
            "name": "responseReasonCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    subscription: Optional[SubscriptionPaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    response_reason_description: str = field(
        metadata={
            "name": "responseReasonDescription",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    auth_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 6,
        },
    )
    avsresponse: Optional[str] = field(
        default=None,
        metadata={
            "name": "AVSResponse",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 1,
        },
    )
    card_code_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCodeResponse",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 1,
        },
    )
    cavvresponse: Optional[str] = field(
        default=None,
        metadata={
            "name": "CAVVResponse",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 1,
        },
    )
    fdsfilter_action: Optional[str] = field(
        default=None,
        metadata={
            "name": "FDSFilterAction",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    fdsfilters: Optional[ArrayOfFdsfilter] = field(
        default=None,
        metadata={
            "name": "FDSFilters",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    batch: Optional[BatchDetailsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    order: Optional[OrderExType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    requested_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "requestedAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    auth_amount: Decimal = field(
        metadata={
            "name": "authAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    settle_amount: Decimal = field(
        metadata={
            "name": "settleAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        }
    )
    tax: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    duty: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    line_items: Optional[ArrayOfLineItem] = field(
        default=None,
        metadata={
            "name": "lineItems",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    prepaid_balance_remaining: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "prepaidBalanceRemaining",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "fraction_digits": 4,
        },
    )
    tax_exempt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxExempt",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    payment: PaymentMaskedType = field(
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    customer: Optional[CustomerDataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bill_to: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    recurring_billing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "recurringBilling",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_ip: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerIP",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    product: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    entry_mode: Optional[str] = field(
        default=None,
        metadata={
            "name": "entryMode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    market_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "marketType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    mobile_device_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "mobileDeviceId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_signature: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerSignature",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    returned_items: Optional[ArrayOfReturnedItem] = field(
        default=None,
        metadata={
            "name": "returnedItems",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    solution: Optional[SolutionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    emv_details: Optional["TransactionDetailsType.EmvDetails"] = field(
        default=None,
        metadata={
            "name": "emvDetails",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    surcharge: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    employee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "employeeId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tip: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    other_tax: Optional[OtherTaxType] = field(
        default=None,
        metadata={
            "name": "otherTax",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_from: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipFrom",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "networkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )
    original_network_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "originalNetworkTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 255,
            "pattern": r"[0-9a-zA-Z\s]+",
        },
    )
    original_auth_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "originalAuthAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    authorization_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "authorizationIndicator",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )

    class EmvDetails(BaseModel):
        model_config = ConfigDict(defer_build=True)
        tag: list["TransactionDetailsType.EmvDetails.Tag"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "min_occurs": 1,
            },
        )

        class Tag(BaseModel):
            model_config = ConfigDict(defer_build=True)
            tag_id: str = field(
                metadata={
                    "name": "tagId",
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                    "required": True,
                }
            )
            data: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                    "required": True,
                }
            )


class UpdateCustomerPaymentProfileResponse(AnetApiResponse):
    class Meta:
        name = "updateCustomerPaymentProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    validation_direct_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "validationDirectResponse",
            "type": "Element",
            "max_length": 2048,
        },
    )


class UpdateCustomerProfileRequest(AnetApiRequest):
    class Meta:
        name = "updateCustomerProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    profile: CustomerProfileInfoExType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class UpdateCustomerProfileResponse(AnetApiResponse):
    class Meta:
        name = "updateCustomerProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class UpdateCustomerShippingAddressRequest(AnetApiRequest):
    class Meta:
        name = "updateCustomerShippingAddressRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    address: CustomerAddressExType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    default_shipping_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultShippingAddress",
            "type": "Element",
        },
    )


class UpdateCustomerShippingAddressResponse(AnetApiResponse):
    class Meta:
        name = "updateCustomerShippingAddressResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class UpdateHeldTransactionRequest(AnetApiRequest):
    class Meta:
        name = "updateHeldTransactionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    held_transaction_request: HeldTransactionRequestType = field(
        metadata={
            "name": "heldTransactionRequest",
            "type": "Element",
            "required": True,
        }
    )


class UpdateHeldTransactionResponse(AnetApiResponse):
    class Meta:
        name = "updateHeldTransactionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction_response: Optional[TransactionResponse] = field(
        default=None,
        metadata={
            "name": "transactionResponse",
            "type": "Element",
        },
    )


class UpdateMerchantDetailsRequest(AnetApiRequest):
    class Meta:
        name = "updateMerchantDetailsRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    is_test_mode: bool = field(
        metadata={
            "name": "isTestMode",
            "type": "Element",
            "required": True,
        }
    )


class UpdateMerchantDetailsResponse(AnetApiResponse):
    class Meta:
        name = "updateMerchantDetailsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class UpdateSplitTenderGroupRequest(AnetApiRequest):
    class Meta:
        name = "updateSplitTenderGroupRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    split_tender_id: str = field(
        metadata={
            "name": "splitTenderId",
            "type": "Element",
            "required": True,
        }
    )
    split_tender_status: SplitTenderStatusEnum = field(
        metadata={
            "name": "splitTenderStatus",
            "type": "Element",
            "required": True,
        }
    )


class UpdateSplitTenderGroupResponse(AnetApiResponse):
    class Meta:
        name = "updateSplitTenderGroupResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)


class ValidateCustomerPaymentProfileRequest(AnetApiRequest):
    class Meta:
        name = "validateCustomerPaymentProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_payment_profile_id: str = field(
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    customer_shipping_address_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerShippingAddressId",
            "type": "Element",
            "pattern": r"[0-9]+",
        },
    )
    card_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "cardCode",
            "type": "Element",
            "min_length": 3,
            "max_length": 4,
            "pattern": r"[0-9]+",
        },
    )
    validation_mode: ValidationModeEnum = field(
        metadata={
            "name": "validationMode",
            "type": "Element",
            "required": True,
        }
    )


class ValidateCustomerPaymentProfileResponse(AnetApiResponse):
    class Meta:
        name = "validateCustomerPaymentProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    direct_response: Optional[str] = field(
        default=None,
        metadata={
            "name": "directResponse",
            "type": "Element",
            "max_length": 2048,
        },
    )


class ArrayOfCustomerPaymentProfileListItemType(BaseModel):
    class Meta:
        name = "arrayOfCustomerPaymentProfileListItemType"

    model_config = ConfigDict(defer_build=True)
    payment_profile: list[CustomerPaymentProfileListItemType] = field(
        default_factory=list,
        metadata={
            "name": "paymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "nillable": True,
        },
    )


class CustomerProfileMaskedType(CustomerProfileExType):
    class Meta:
        name = "customerProfileMaskedType"

    model_config = ConfigDict(defer_build=True)
    payment_profiles: list[CustomerPaymentProfileMaskedType] = field(
        default_factory=list,
        metadata={
            "name": "paymentProfiles",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to_list: list[CustomerAddressExType] = field(
        default_factory=list,
        metadata={
            "name": "shipToList",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_type: Optional[CustomerProfileTypeEnum] = field(
        default=None,
        metadata={
            "name": "profileType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class EncryptedTrackDataType(BaseModel):
    class Meta:
        name = "encryptedTrackDataType"

    model_config = ConfigDict(defer_build=True)
    form_of_payment: KeyBlock = field(
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )


class GetAujobDetailsResponse(AnetApiResponse):
    class Meta:
        name = "getAUJobDetailsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    total_num_in_result_set: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumInResultSet",
            "type": "Element",
        },
    )
    au_details: Optional[ListOfAudetailsType] = field(
        default=None,
        metadata={
            "name": "auDetails",
            "type": "Element",
        },
    )


class GetCustomerPaymentProfileResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerPaymentProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    payment_profile: Optional[CustomerPaymentProfileMaskedType] = field(
        default=None,
        metadata={
            "name": "paymentProfile",
            "type": "Element",
        },
    )


class GetSettledBatchListResponse(AnetApiResponse):
    class Meta:
        name = "getSettledBatchListResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    batch_list: Optional[ArrayOfBatchDetailsType] = field(
        default=None,
        metadata={
            "name": "batchList",
            "type": "Element",
        },
    )


class GetTransactionDetailsResponse(AnetApiResponse):
    class Meta:
        name = "getTransactionDetailsResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction: TransactionDetailsType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    client_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientId",
            "type": "Element",
            "max_length": 30,
        },
    )
    transref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "transrefId",
            "type": "Element",
            "max_length": 20,
        },
    )


class GetTransactionListResponse(AnetApiResponse):
    class Meta:
        name = "getTransactionListResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transactions: Optional[ArrayOfTransactionSummaryType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    total_num_in_result_set: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumInResultSet",
            "type": "Element",
        },
    )


class GetUnsettledTransactionListResponse(AnetApiResponse):
    class Meta:
        name = "getUnsettledTransactionListResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transactions: Optional[ArrayOfTransactionSummaryType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    total_num_in_result_set: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalNumInResultSet",
            "type": "Element",
        },
    )


class ProfileTransactionType(BaseModel):
    class Meta:
        name = "profileTransactionType"

    model_config = ConfigDict(defer_build=True)
    profile_trans_auth_capture: Optional[ProfileTransAuthCaptureType] = field(
        default=None,
        metadata={
            "name": "profileTransAuthCapture",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_trans_auth_only: Optional[ProfileTransAuthOnlyType] = field(
        default=None,
        metadata={
            "name": "profileTransAuthOnly",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_trans_prior_auth_capture: Optional[ProfileTransPriorAuthCaptureType] = field(
        default=None,
        metadata={
            "name": "profileTransPriorAuthCapture",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_trans_capture_only: Optional[ProfileTransCaptureOnlyType] = field(
        default=None,
        metadata={
            "name": "profileTransCaptureOnly",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_trans_refund: Optional[ProfileTransRefundType] = field(
        default=None,
        metadata={
            "name": "profileTransRefund",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_trans_void: Optional[ProfileTransVoidType] = field(
        default=None,
        metadata={
            "name": "profileTransVoid",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class SubscriptionCustomerProfileType(CustomerProfileExType):
    class Meta:
        name = "subscriptionCustomerProfileType"

    model_config = ConfigDict(defer_build=True)
    payment_profile: Optional[CustomerPaymentProfileMaskedType] = field(
        default=None,
        metadata={
            "name": "paymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping_profile: Optional[CustomerAddressExType] = field(
        default=None,
        metadata={
            "name": "shippingProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArbsubscriptionMaskedType(BaseModel):
    class Meta:
        name = "ARBSubscriptionMaskedType"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    payment_schedule: Optional[PaymentScheduleType] = field(
        default=None,
        metadata={
            "name": "paymentSchedule",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.01"),
            "fraction_digits": 4,
        },
    )
    trial_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "trialAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    status: Optional[ArbsubscriptionStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[SubscriptionCustomerProfileType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    order: Optional[OrderType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    arb_transactions: Optional[ArbtransactionList] = field(
        default=None,
        metadata={
            "name": "arbTransactions",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CreateCustomerProfileTransactionRequest(AnetApiRequest):
    class Meta:
        name = "createCustomerProfileTransactionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction: ProfileTransactionType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    extra_options: Optional[str] = field(
        default=None,
        metadata={
            "name": "extraOptions",
            "type": "Element",
            "max_length": 1024,
        },
    )


class GetCustomerPaymentProfileListResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerPaymentProfileListResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    total_num_in_result_set: int = field(
        metadata={
            "name": "totalNumInResultSet",
            "type": "Element",
            "required": True,
        }
    )
    payment_profiles: Optional[ArrayOfCustomerPaymentProfileListItemType] = field(
        default=None,
        metadata={
            "name": "paymentProfiles",
            "type": "Element",
        },
    )


class GetCustomerProfileResponse(AnetApiResponse):
    class Meta:
        name = "getCustomerProfileResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    profile: Optional[CustomerProfileMaskedType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    subscription_ids: Optional[SubscriptionIdList] = field(
        default=None,
        metadata={
            "name": "subscriptionIds",
            "type": "Element",
        },
    )


class PaymentType(BaseModel):
    class Meta:
        name = "paymentType"

    model_config = ConfigDict(defer_build=True)
    credit_card: Optional[CreditCardType] = field(
        default=None,
        metadata={
            "name": "creditCard",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bank_account: Optional[BankAccountType] = field(
        default=None,
        metadata={
            "name": "bankAccount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    track_data: Optional[CreditCardTrackType] = field(
        default=None,
        metadata={
            "name": "trackData",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    encrypted_track_data: Optional[EncryptedTrackDataType] = field(
        default=None,
        metadata={
            "name": "encryptedTrackData",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    pay_pal: Optional[PayPalType] = field(
        default=None,
        metadata={
            "name": "payPal",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    opaque_data: Optional[OpaqueDataType] = field(
        default=None,
        metadata={
            "name": "opaqueData",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    emv: Optional[PaymentEmvType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    data_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class ArbgetSubscriptionResponse(AnetApiResponse):
    class Meta:
        name = "ARBGetSubscriptionResponse"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription: ArbsubscriptionMaskedType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class ArbsubscriptionType(BaseModel):
    class Meta:
        name = "ARBSubscriptionType"

    model_config = ConfigDict(defer_build=True)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "max_length": 50,
        },
    )
    payment_schedule: Optional[PaymentScheduleType] = field(
        default=None,
        metadata={
            "name": "paymentSchedule",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.01"),
            "fraction_digits": 4,
        },
    )
    trial_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "trialAmount",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_inclusive": Decimal("0.00"),
            "fraction_digits": 4,
        },
    )
    payment: Optional[PaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    order: Optional[OrderType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer: Optional[CustomerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bill_to: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[CustomerProfileIdType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class CustomerPaymentProfileType(CustomerPaymentProfileBaseType):
    class Meta:
        name = "customerPaymentProfileType"

    model_config = ConfigDict(defer_build=True)
    payment: Optional[PaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    drivers_license: Optional[DriversLicenseType] = field(
        default=None,
        metadata={
            "name": "driversLicense",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "taxId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "min_length": 8,
            "max_length": 9,
        },
    )
    default_payment_profile: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultPaymentProfile",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    subsequent_auth_information: Optional[SubsequentAuthInformation] = field(
        default=None,
        metadata={
            "name": "subsequentAuthInformation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    exclude_from_account_updater: Optional[bool] = field(
        default=None,
        metadata={
            "name": "excludeFromAccountUpdater",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class TransactionRequestType(BaseModel):
    """
    :ivar transaction_type:
    :ivar amount:
    :ivar currency_code:
    :ivar payment:
    :ivar profile:
    :ivar solution:
    :ivar call_id:
    :ivar terminal_number:
    :ivar auth_code:
    :ivar ref_trans_id:
    :ivar split_tender_id:
    :ivar order:
    :ivar line_items:
    :ivar tax:
    :ivar duty:
    :ivar shipping:
    :ivar tax_exempt:
    :ivar po_number:
    :ivar customer:
    :ivar bill_to:
    :ivar ship_to:
    :ivar customer_ip:
    :ivar cardholder_authentication:
    :ivar retail:
    :ivar employee_id:
    :ivar transaction_settings: Allowed values for settingName are:
        emailCustomer, merchantEmail, allowPartialAuth,
        headerEmailReceipt, footerEmailReceipt, recurringBilling,
        duplicateWindow, testRequest.
    :ivar user_fields:
    :ivar surcharge:
    :ivar merchant_descriptor:
    :ivar sub_merchant:
    :ivar tip:
    :ivar processing_options:
    :ivar subsequent_auth_information:
    :ivar other_tax:
    :ivar ship_from:
    :ivar authorization_indicator_type:
    """

    class Meta:
        name = "transactionRequestType"

    model_config = ConfigDict(defer_build=True)
    transaction_type: TransactionTypeEnum = field(
        metadata={
            "name": "transactionType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "required": True,
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "currencyCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    payment: Optional[PaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile: Optional[CustomerProfilePaymentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    solution: Optional[SolutionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    call_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "callId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    terminal_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "terminalNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    auth_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "authCode",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ref_trans_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "refTransId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    split_tender_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "splitTenderId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    order: Optional[OrderType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    line_items: Optional[ArrayOfLineItem] = field(
        default=None,
        metadata={
            "name": "lineItems",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    duty: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    shipping: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tax_exempt: Optional[bool] = field(
        default=None,
        metadata={
            "name": "taxExempt",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    po_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "poNumber",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer: Optional[CustomerDataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    bill_to: Optional[CustomerAddressType] = field(
        default=None,
        metadata={
            "name": "billTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipTo",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    customer_ip: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerIP",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    cardholder_authentication: Optional[CcAuthenticationType] = field(
        default=None,
        metadata={
            "name": "cardholderAuthentication",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    retail: Optional[TransRetailInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    employee_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "employeeId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    transaction_settings: Optional[ArrayOfSetting] = field(
        default=None,
        metadata={
            "name": "transactionSettings",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    user_fields: Optional["TransactionRequestType.UserFields"] = field(
        default=None,
        metadata={
            "name": "userFields",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    surcharge: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    merchant_descriptor: Optional[str] = field(
        default=None,
        metadata={
            "name": "merchantDescriptor",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    sub_merchant: Optional[SubMerchantType] = field(
        default=None,
        metadata={
            "name": "subMerchant",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    tip: Optional[ExtendedAmountType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    processing_options: Optional[ProcessingOptions] = field(
        default=None,
        metadata={
            "name": "processingOptions",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    subsequent_auth_information: Optional[SubsequentAuthInformation] = field(
        default=None,
        metadata={
            "name": "subsequentAuthInformation",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    other_tax: Optional[OtherTaxType] = field(
        default=None,
        metadata={
            "name": "otherTax",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_from: Optional[NameAndAddressType] = field(
        default=None,
        metadata={
            "name": "shipFrom",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    authorization_indicator_type: Optional[AuthorizationIndicatorType] = field(
        default=None,
        metadata={
            "name": "authorizationIndicatorType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )

    class UserFields(BaseModel):
        model_config = ConfigDict(defer_build=True)
        user_field: list[UserField] = field(
            default_factory=list,
            metadata={
                "name": "userField",
                "type": "Element",
                "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
                "max_occurs": 20,
            },
        )


class ArbcreateSubscriptionRequest(AnetApiRequest):
    class Meta:
        name = "ARBCreateSubscriptionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription: ArbsubscriptionType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class ArbupdateSubscriptionRequest(AnetApiRequest):
    class Meta:
        name = "ARBUpdateSubscriptionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    subscription_id: str = field(
        metadata={
            "name": "subscriptionId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    subscription: ArbsubscriptionType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


class CreateCustomerPaymentProfileRequest(AnetApiRequest):
    class Meta:
        name = "createCustomerPaymentProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    payment_profile: CustomerPaymentProfileType = field(
        metadata={
            "name": "paymentProfile",
            "type": "Element",
            "required": True,
        }
    )
    validation_mode: Optional[ValidationModeEnum] = field(
        default=None,
        metadata={
            "name": "validationMode",
            "type": "Element",
        },
    )


class CreateTransactionRequest(AnetApiRequest):
    class Meta:
        name = "createTransactionRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction_request: TransactionRequestType = field(
        metadata={
            "name": "transactionRequest",
            "type": "Element",
            "required": True,
        }
    )


class CustomerPaymentProfileExType(CustomerPaymentProfileType):
    class Meta:
        name = "customerPaymentProfileExType"

    model_config = ConfigDict(defer_build=True)
    customer_payment_profile_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "customerPaymentProfileId",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
            "pattern": r"[0-9]+",
        },
    )


class CustomerProfileType(CustomerProfileBaseType):
    class Meta:
        name = "customerProfileType"

    model_config = ConfigDict(defer_build=True)
    payment_profiles: list[CustomerPaymentProfileType] = field(
        default_factory=list,
        metadata={
            "name": "paymentProfiles",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    ship_to_list: list[CustomerAddressType] = field(
        default_factory=list,
        metadata={
            "name": "shipToList",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )
    profile_type: Optional[CustomerProfileTypeEnum] = field(
        default=None,
        metadata={
            "name": "profileType",
            "type": "Element",
            "namespace": "AnetApi/xml/v1/schema/AnetApiSchema.xsd",
        },
    )


class GetHostedPaymentPageRequest(AnetApiRequest):
    """
    :ivar transaction_request:
    :ivar hosted_payment_settings: Allowed values for settingName are:
        hostedPaymentIFrameCommunicatorUrl, hostedPaymentButtonOptions,
        hostedPaymentReturnOptions, hostedPaymentOrderOptions,
        hostedPaymentPaymentOptions, hostedPaymentBillingAddressOptions,
        hostedPaymentShippingAddressOptions,
        hostedPaymentSecurityOptions, hostedPaymentCustomerOptions,
        hostedPaymentStyleOptions
    """

    class Meta:
        name = "getHostedPaymentPageRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    transaction_request: TransactionRequestType = field(
        metadata={
            "name": "transactionRequest",
            "type": "Element",
            "required": True,
        }
    )
    hosted_payment_settings: Optional[ArrayOfSetting] = field(
        default=None,
        metadata={
            "name": "hostedPaymentSettings",
            "type": "Element",
        },
    )


class CreateCustomerProfileRequest(AnetApiRequest):
    class Meta:
        name = "createCustomerProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    profile: CustomerProfileType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    validation_mode: Optional[ValidationModeEnum] = field(
        default=None,
        metadata={
            "name": "validationMode",
            "type": "Element",
        },
    )


class UpdateCustomerPaymentProfileRequest(AnetApiRequest):
    class Meta:
        name = "updateCustomerPaymentProfileRequest"
        namespace = "AnetApi/xml/v1/schema/AnetApiSchema.xsd"

    model_config = ConfigDict(defer_build=True)
    customer_profile_id: str = field(
        metadata={
            "name": "customerProfileId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]+",
        }
    )
    payment_profile: CustomerPaymentProfileExType = field(
        metadata={
            "name": "paymentProfile",
            "type": "Element",
            "required": True,
        }
    )
    validation_mode: Optional[ValidationModeEnum] = field(
        default=None,
        metadata={
            "name": "validationMode",
            "type": "Element",
        },
    )
