import requests
from bs4 import BeautifulSoup
product_list=[
    {
        "name":"samsung m31s",
        'URL':'https://www.amazon.in/Samsung-Galaxy-Mirage-128GB-Storage/dp/B07DJCJBB3/ref=sr_1_1?crid=3KDIINZUC2U1W&dchild=1&keywords=m31s&qid=1618145707&sprefix=m31s%2Caps%2C359&sr=8-1',
        'target_price':18499
    },
    {
        "name":"raelme7 pro",
        "URL":"https://www.amazon.in/Realme-Mirror-Silver-128GB-Storage/dp/B08J8KKHNG/ref=sr_1_1?dchild=1&keywords=realme+7+pro&qid=1618147534&sr=8-1",
        'target_price':18696
    },
    {
        "name":"OPPO F19 Pro+",
        "URL":"https://www.amazon.in/dp/B08LRDK8Z5/ref=gwdb_bmc_3_OPPO?pf_rd_s=merchandised-search-6&pf_rd_t=Gateway&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=EB2BPSH90NDR0ZMCMZ3Z&pf_rd_p=7ff22083-bfb0-4bd4-aaee-f7568734926a",
        'target_price':18499
    },
    {
        "name":"M51",
        "URL":"https://www.amazon.in/gp/product/B085J1J32G/ref=s9_acss_bw_cg_Budget_3b1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=4XNYESWSWNN2MVN6D8BQ&pf_rd_t=101&pf_rd_p=3921ea48-93c2-4bd3-b626-c5ded9dbcc10&pf_rd_i=1389401031",
        'target_price':22999
    },
    {
        "name":"OnePlus 8 Pro",
        "URL":"https://www.amazon.in/Test-Exclusive-750/dp/B07DJCYBVK/ref=gbph_img_m-5_9fa4_fd02262a?smid=A35FCS7U51TK3C&pf_rd_p=83dfc2bf-4d0a-42c0-804e-5b1f82eb9fa4&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=P4ZN4PBPPM1J0EP104JN",
        'target_price':45000
    }
]

def get_price(URL):
    headers = {
        'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="priceblock_dealprice")
    if product_price == None:
        product_price = soup.find(id="priceblock_ourprice")

    return product_price.getText()
result_page=open("price_page.txt","w")
try:
    for phones in product_list:
        product_price_returned = get_price(phones.get("URL"))
        print(phones.get("name") + "-" + product_price_returned)

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(",", "")
        my_product_price = int(float(my_product_price))
        if my_product_price <= phones.get("target_price"):
            print("Available at your price")
            result_page.write(phones.get("name") + "- \t" + "available at required price" + "current price - " + str(
                my_product_price) + "\n")
        else:
            print("price still at current price")
finally:
    result_page.close()
