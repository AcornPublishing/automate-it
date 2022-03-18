from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h3[@class="   pricing-card-name display-heading-3"]/text()')
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("Plans:", plans, "\nPricing:", pricing)
