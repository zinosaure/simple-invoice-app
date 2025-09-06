from pathlib import Path
from flex import Flexmeta, Flexobject, Flexselect, pl
from app.flexmodels.tables import (
    Provider,
    IBAN,
    Recipient,
    Product,
    Invoice,
)
from datetime import date

Flexmeta.setup(Path("./flexstore"))

# provider = Provider()
# provider.name = "Ethan Ross"
# provider.siren = "952 5211 344"
# provider.contact.email = "ethan.ross@example.mail"
# provider.contact.number = 30
# provider.contact.street = "Blvd. St Jean"
# provider.contact.zip_code = 95022
# provider.contact.city = "Cergy-Pontoise"
# provider.contact.state = "Ile-de-France"
# provider.contact.country = "France"
# provider.commit()

# recipient = Recipient()
# recipient.name = "Facebook SAS"
# recipient.siren = "753 2552 562"
# recipient.contract = "FR-022563"
# recipient.contact.email = "invoice@facebook.com"
# recipient.contact.number = 19
# recipient.contact.street = "Rue Jean Jaurès"
# recipient.contact.zip_code = 75001
# recipient.contact.city = "Paris"
# recipient.contact.state = "Ile-de-France"
# recipient.contact.country = "France"
# recipient.commit()

# recipient = Recipient()
# recipient.name = "Google Inc."
# recipient.siren = "750 0545 123"
# recipient.contract = "GG-963-58888"
# recipient.contact.email = "facture-prestation@france.google.com"
# recipient.contact.number = 58
# recipient.contact.street = "Avenue de Lyon"
# recipient.contact.zip_code = 75005
# recipient.contact.city = "Paris"
# recipient.contact.state = "Ile-de-France"
# recipient.contact.country = "France"
# recipient.commit()

# iban = IBAN()
# iban.label = "Revolut Pro."
# iban.account_number = "FR76 0000 1111 2222 3333 4444 555"
# iban.bic_swift = "BNKFCTF01"
# iban.commit()

# product = Product()
# product.label = "Prestations (TJM)"
# product.description = "du 01/08 au 29/08"
# product.price_unit_ht = 450.0
# product.tax_rate = 0
# product.commit()

# product = Product()
# product.label = "Frais paiement anticipé"
# product.description = "du 01/08 au 29/08"
# product.price_unit_ht = -13.5
# product.tax_rate = 0
# product.commit()

# items = []
# if product := Product.load(1):
#     item = Invoice.Item()
#     item.quantity = 20
#     item.product = product
#     item.tax_rate = product.tax_rate
#     item.total_price_ht = product.price_unit_ht * item.quantity
#     items.append(item)

# if product := Product.load(2):
#     item = Invoice.Item()
#     item.quantity = 20
#     item.product = product
#     item.tax_rate = product.tax_rate
#     item.total_price_ht = product.price_unit_ht * item.quantity
#     items.append(item)

# invoice = Invoice()
# invoice.type = Invoice.Type.INVOICE.value
# invoice.status = Invoice.Status.DRAFT.value
# invoice.paiment_status = Invoice.PaimentStatus.PENDING.value
# invoice.date = date.today()
# invoice.paiment_date = date.today()
# invoice.provider = Provider.load(1) or Provider()
# invoice.recipient = Recipient.load(2) or Recipient()
# invoice.payment_method = Invoice.PaymentMethod.BANK_TRANSFER.value
# invoice.currency = Invoice.Currency.EURO.value
# invoice.iban = IBAN.load(1) or IBAN()
# invoice.set_items(items)

# print(invoice)
# invoice.commit()

if invoice := Invoice.load(1):
    print(invoice.json())
