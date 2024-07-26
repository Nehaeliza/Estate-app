# import frappe
# from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
# from pycoingecko import CoinGeckoAPI



# class SalesInvoiceCustom(SalesInvoice):
#     """
#         Inherit core sales invoice and extend it
#     """
#     pass

#     def get_crypto_prices(self):
#         """
#             Get grand total in BTC,ETH
#         """
#         cg = CoinGeckoAPI()
#         prices = frappe.as_dict(cg.get_price(ids=['bitcoin', 'etherum'], vs_currencies=self.currency))
#         print('GETTING PRICES, \n\n\n')

#         return{
#             'bitcoin' : self.grand_total/prices.bitcoin[self.currency.lower()],
#             'ethereum' : self.grand_total/prices.ethereum[self.currency.lower()]
#         }


import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from pycoingecko import CoinGeckoAPI

# class SalesInvoiceCustom(SalesInvoice):
#     pass

#     def get_crypto_prices(self):
#         cg=CoinGeckoAPI()
#         prices = frappe.as_dict(cg.get_price(ids=['bitcoin','ethereum'],vs_currencies=self.currency))
#         # data = {
#         #     "bitcoin":self.grandtotal/prices.bitcoin[self.currency.lower()],
#         #     "ethereum":self.grandtotal/prices.ethereum[self.currency.lower()],
#         # }
#         return {
#             "bitcoin":self.grandtotal/prices.bitcoin[self.currency.lower()],
#             "ethereum":self.grandtotal/prices.ethereum[self.currency.lower()],
#         }


class SalesInvoiceCustom(SalesInvoice):
    def get_crypto_prices(self):
        cg = CoinGeckoAPI()
        prices = cg.get_price(ids=['bitcoin', 'ethereum'], vs_currencies=self.currency)
        
        # Ensure that the response contains the expected data
        if 'bitcoin' in prices and self.currency.lower() in prices['bitcoin'] and \
           'ethereum' in prices and self.currency.lower() in prices['ethereum']:
            return {
                "bitcoin": self.grand_total / prices['bitcoin'][self.currency.lower()],
                "ethereum": self.grand_total / prices['ethereum'][self.currency.lower()],
            }
        else:
            frappe.throw(f"Could not fetch prices for the specified currency: {self.currency}")




        

       

        