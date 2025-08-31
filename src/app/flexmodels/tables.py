from flex import Flex
from datetime import date
from enum import Enum


class Table(Flex.Flextable):
    pass


class Provider(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("providers", 1000))
        self.name: str = "???"
        self.email: str = "???@example.com"
        self.street_number: int | str = 0
        self.street_name: str = ""
        self.zip_code: int | str = 95000
        self.city: str = ""
        self.state: str = ""
        self.country: str = ""
        self.siren: int = 0


class IBAN(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("ibans", 1000))
        self.label: str = "???"
        self.account_number: str = "FR76 ???? ???? ???? ???? ????"
        self.bic_swift: str = "???"


class Recipient(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("recipients", 1000))
        self.contract: str = ""
        self.name: str = "???"
        self.email: str = "???@example.com"
        self.street_number: int | str = 0
        self.street_name: str = ""
        self.zip_code: int | str = 95000
        self.city: str = ""
        self.state: str = ""
        self.country: str = ""
        self.siren: int = 0


class Product(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("products", 1000))
        self.label: str = "???"
        self.description: str = "???"
        self.price_unit_ht: float = 0.0
        self.tax_rate: float = 0.0


class InvoiceType(str, Enum):
    INVOICE = "Facture"
    NOTE_INVOICE = "Avoir"


class Currency(str, Enum):
    EURO = "Euro (€)"


class PaymentMethod(str, Enum):
    CASH = "Cash"
    CHEQUE = "Chèque"
    BANK_TRANSFER = "Virement bancaire"


class InvoiceItem:
    def __init__(self):
        self.quantity: int = 0
        self.product: Product = Product()
        self.tax_rate: float = self.product.tax_rate
        self.total_price_ht: float = 0.0


class Invoice(Table):
    def __init__(self):
        super().__init__(Flex.Flexmeta("invoices", 1000))
        self.type: InvoiceType = InvoiceType.INVOICE
        self.date: date = date.today()
        self.paiment_date: date = date.today()
        self.provider: Provider = Provider()
        self.recipient: Recipient = Recipient()
        self.payment_method: PaymentMethod = PaymentMethod.BANK_TRANSFER
        self.currency: Currency = Currency.EURO
        self.iban: IBAN = IBAN()
        self.items: list[InvoiceItem] = []
        self.total_price_ht: float = 0.0
        self.total_tva_price: float = 0.0
        self.total_price_ttc: float = 0.0
        self.text_condition: str = (
            "En cas de retard, une pénalité au taux annuel de 5% sera appliquée, "
            "à laquelle s'ajoutera une indemnité forfaitaire pour frais de recouvrement de 40 € TVA non applicable, "
            "art. 293B du CGI."
        )
