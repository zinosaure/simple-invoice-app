from typing import Any
from flex import Flexmeta, Flexobject, Flexselect, pl
from datetime import date
from enum import Enum


class Table(Flexobject):
    pass


class Contact(Table):
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
    flexmeta: Flexmeta = Flexmeta("providers", schema={"contact": pl.Object})

    def __init__(self):
        super().__init__()
        self.name: str = "???"
        self.siren: str = ""
        self.contact: Contact = Contact()


class Recipient(Table):
    flexmeta: Flexmeta = Flexmeta("recipients", schema={"contact": pl.Object})

    def __init__(self):
        super().__init__()
        self.contract: str = ""
        self.name: str = "???"
        self.siren: str = ""
        self.contact: Contact = Contact()


class IBAN(Table):
    flexmeta: Flexmeta = Flexmeta("ibans")

    def __init__(self):
        super().__init__()
        self.label: str = "???"
        self.account_number: str = "FR76 ???? ???? ???? ???? ????"
        self.bic_swift: str = "???"


class Product(Table):
    flexmeta: Flexmeta = Flexmeta("products", schema={"price_unit_ht": pl.Float32})

    def __init__(self):
        super().__init__()
        self.label: str = "???"
        self.description: str = "???"
        self.price_unit_ht: float = 0.0
        self.tax_rate: float = 0.0


class Invoice(Table):
    flexmeta: Flexmeta = Flexmeta("invoices")

    def __init__(self):
        super().__init__()
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

    def set_items(self, items: list["Invoice.Item"]):
        self.items = items

    def update(self, item: dict[str, Any]) -> "Flexobject":
        super().update(item)

        for name, value in self.__dict__.items():
            if value and name in ["date", "paiment_date"] and isinstance(value, str):
                self.__setitem__(name, date(*[int(v) for v in value.split("-")]))

            if name == "items" and isinstance(value, list):
                self.__dict__[name] = []

                for i, v in enumerate(value):
                    self.__dict__[name].append(Invoice.Item.clone(v))

        return self

    def takeout(self, extract_all: bool = True) -> dict[str, Any]:
        items = super().takeout(extract_all)

        for name, value in items.items():
            if value and name in ["date", "paiment_date"] and isinstance(value, date):
                items[name] = str(value)

            if name == "items" and isinstance(value, list):
                items[name] = [v.takeout() for v in value]

        return items

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

    class Item(Table):
        def __init__(self):
            self.quantity: int = 0
            self.product: Product = Product()
            self.tax_rate: float = self.product.tax_rate
            self.total_price_ht: float = 0.0
