from typing import Any, Optional, cast
from flex import Flex
from datetime import date
from enum import Enum


class Table(Flex.Flextable):
    pass


class Contact:
    def __init__(self):
        self.phone: str = ""
        self.cellphone: str = ""
        self.email: str = "???@example.com"
        self.number: int | str = 0
        self.street: str = ""
        self.zip_code: int | str = 95000
        self.city: str = ""
        self.state: str = ""
        self.country: str = ""


class Provider(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("providers", 1000))
        self.name: str = "???"
        self.siren: str = ""
        self.contact: Contact = Contact()

    @staticmethod
    def load(id: int) -> Optional["Provider"]:
        return cast(Provider, Flex.Flextable._load(Provider(), id))


class Recipient(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("recipients", 1000))
        self.contract: str = ""
        self.name: str = "???"
        self.siren: str = ""
        self.contact: Contact = Contact()

    @staticmethod
    def load(id: int) -> Optional["Recipient"]:
        return cast(Recipient, Flex.Flextable._load(Recipient(), id))


class IBAN(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("ibans", 1000))
        self.label: str = "???"
        self.account_number: str = "FR76 ???? ???? ???? ???? ????"
        self.bic_swift: str = "???"

    @staticmethod
    def load(id: int) -> Optional["IBAN"]:
        return cast(IBAN, Flex.Flextable._load(IBAN(), id))


class Product(Table):
    def __init__(self):
        super().__init__(
            Flex.Flexmeta("products", 1000, {"price_unit_ht": Flex.Pl.Float32})
        )
        self.label: str = "???"
        self.description: str = "???"
        self.price_unit_ht: float = 0.0
        self.tax_rate: float = 0.0

    @staticmethod
    def load(id: int) -> Optional["Product"]:
        return cast(Product, Flex.Flextable._load(Product(), id))


class Invoice(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("invoices", 0))
        self.type: str = Invoice.Type.INVOICE.value
        self.status: str = Invoice.Status.DRAFT.value
        self.paiment_status: str = Invoice.PaimentStatus.PENDING.value
        self.date: date = date.today()
        self.paiment_date: date = date.today()
        self.provider: Provider = Provider()
        self.recipient: Recipient = Recipient()
        self.payment_method: str = Invoice.PaymentMethod.BANK_TRANSFER.value
        self.currency: str = Invoice.Currency.EURO.value
        self.iban: IBAN = IBAN()
        self.items: list[Invoice.Item] = []
        self.total_price_ht: float = 0.0
        self.total_tva_price: float = 0.0
        self.total_price_ttc: float = 0.0
        self.text_condition: str = (
            "En cas de retard, une pénalité au taux annuel de 5% sera appliquée, "
            "à laquelle s'ajoutera une indemnité forfaitaire pour frais de recouvrement de 40 € TVA non applicable, "
            "art. 293B du CGI."
        )

    @staticmethod
    def load(id: int) -> Optional["Invoice"]:
        return cast(Invoice, Flex.Flextable._load(Invoice(), id))

    def on_compose(self, name: str, value: Any) -> Any:
        if value and name in ["date", "paiment_date"] and isinstance(value, str):
            return date(*[int(v) for v in value.split("-")])

        if value and name == "items" and isinstance(value, list):
            return [Invoice.Item.to_object(item) for item in value]

        return value

    def on_decompose(self, name: str, value: Any) -> Any:
        if value and name in ["date", "paiment_date"] and isinstance(value, date):
            return str(value)

        if value and name == "items" and isinstance(value, list):
            return [item.to_dict() for item in value]

        return super().on_decompose(name, value)

    class SelfEnum(str, Enum):
        pass

    class Type(SelfEnum):
        INVOICE = "Facture"
        NOTE_INVOICE = "Avoir"

    class Status(SelfEnum):
        DRAFT = "Brouillon"
        SAVED = "Sauvegardé"

    class PaimentStatus(SelfEnum):
        PENDING = "En attente"
        PAID = "Payé"
        CANCEL = "Annulé"

    class Currency(SelfEnum):
        EURO = "Euro (€)"
        DOLLAR = "Dollar ($)"

    class PaymentMethod(SelfEnum):
        CASH = "Cash"
        CHEQUE = "Chèque"
        BANK_TRANSFER = "Virement bancaire"

    class Item:
        def __init__(self):
            self.quantity: int = 0
            self.product: Product = Product()
            self.tax_rate: float = self.product.tax_rate
            self.total_price_ht: float = 0.0

        @staticmethod
        def to_object(data: dict[str, Any]) -> "Invoice.Item":
            item = Invoice.Item()
            item.quantity = data.get("quantity", 0)
            item.tax_rate = data.get("tax_rate", 0.0)
            item.total_price_ht = data.get("total_price_ht", 0.0)
            item.product = cast(Product, Product().clone(data.get("product", {})))

            return item

        def to_dict(self) -> dict[str, Any]:
            return {
                "quantity": self.quantity,
                "product": self.product.to_dict(),
                "tax_rate": self.tax_rate,
                "total_price_ht": self.total_price_ht,
            }
