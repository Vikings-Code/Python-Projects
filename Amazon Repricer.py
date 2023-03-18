import requests
import boto3
from datetime import datetime

# MWS API configuration
access_key = 'your_access_key'
secret_key = 'your_secret_key'
merchant_id = 'your_merchant_id'
marketplace_id = 'your_marketplace_id'
mws_endpoint = 'https://mws.amazonservices.com'
mws_version = '2011-10-01'

# Amazon Product Advertising API configuration
aws_access_key_id = 'your_aws_access_key_id'
aws_secret_access_key = 'your_aws_secret_access_key'
aws_associate_tag = 'your_aws_associate_tag'
amazon_endpoint = 'webservices.amazon.com'

# Retrieve list of ASINs and their prices from MWS API
def get_prices():
    pricing = {}
    client = boto3.client('mws',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          seller_id=merchant_id,
                          region_name='us-west-2')
    response = client.list_inventory_supply(
        MarketplaceId=marketplace_id,
        QueryStartDateTime=datetime.now(),
        ResponseGroup='Basic'
    )
    for item in response['InventorySupplyList']:
        if item['FulfillmentChannel'] == 'AMAZON_FBA':
            asin = item['ASIN']
            price = float(item['Price']['Amount']) / 100
            minimum_price = 0  # replace with your minimum price
            maximum_price = 0  # replace with your maximum price
            optimal_price = 0  # replace with your optimal price
            pricing[asin] = {'price': price, 'minimum_price': minimum_price,
                             'maximum_price': maximum_price, 'optimal_price': optimal_price}
    return pricing

# Retrieve buy box price and seller from Amazon Product Advertising API
def get_buy_box(asin):
    url = f'http://{amazon_endpoint}/onca/xml'
    params = {
        'Service': 'AWSECommerceService',
        'AWSAccessKeyId': aws_access_key_id,
        'AssociateTag': aws_associate_tag,
        'Operation': 'ItemLookup',
        'ItemId': asin,
        'ResponseGroup': 'OfferSummary',
        'Version': '2013-08-01'
    }
    response = requests.get(url, params=params)
    response_dict = xmltodict.parse(response.content)
    try:
        buy_box_price = float(response_dict['ItemLookupResponse']['Items']['Item']['OfferSummary']['LowestNewPrice']['Amount']) / 100
        buy_box_seller = response_dict['ItemLookupResponse']['Items']['Item']['OfferSummary']['LowestNewPrice']['FormattedPrice']
    except:
        buy_box_price = 0
        buy_box_seller = ''
    return buy_box_price, buy_box_seller

# Update price using MWS API
def update_price(asin, price):
    client = boto3.client('mws',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          seller_id=merchant_id,
                          region_name='us-west-2')
    response = client.update_pricing_for_sku(
        MarketplaceId=marketplace_id,
        PricingAction='Update',
        PriceType='LandedPrice',
        SKU=asin,
        Price=price,
        CurrencyCode='USD'
   
