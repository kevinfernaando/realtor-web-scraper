import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import warnings
import math
import undetected_chromedriver as uc

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

warnings.filterwarnings("ignore")


def generate_url(
    location="",
    page=1,
    property_type=None,
    min_price=None,
    max_price=None,
    min_bed=None,
    max_bed=None,
    min_bath=None,
    max_bath=None,
    keyword=None,
):
    location = "_".join(location.replace(",", "").split())
    base_url = f"https://www.realtor.com/realestateandhomes-search/{location}/pg-{page}"

    if property_type is not None:
        property_type = f"/type-{property_type}"
        base_url += property_type

    if min_price is not None:
        if max_price is not None:
            price = f"/price-{min_price}-{max_price}"
        else:
            price = f"/price-{min_price}-na"
        base_url += price

    if min_bed is not None:
        if max_bed is not None:
            bed = f"/beds-{min_bed}-{max_bed}"
        else:
            bed = f"/beds-{min_bed}-na"
        base_url += bed

    if min_bath is not None:
        if max_bath is not None:
            bath = f"/baths-{min_bath}-{max_bath}"
        else:
            bath = f"/baths-{min_bath}-na"

        base_url += bath

    if keyword is not None:
        keyword = f"/keyword-{keyword}"
        base_url += keyword

    return base_url


def scrape_data(params):
    page = 1
    params["page"] = page

    url = generate_url(**params)
    print(url)

    driver = uc.Chrome(use_subprocess=False, headless=True)
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source

    final_data = []
    soup = BeautifulSoup(page_source, "html.parser")

    try:
        total_items = int(
            soup.find("div", {"data-testid": "total-matching-properties"}).text.split()[
                1
            ]
        )
    except:
        total_items = 1
    total_page = math.ceil(total_items / 41)

    for page in range(1, total_page + 1):
        params["page"] = page
        url = generate_url(**params)
        print(params["page"])
        print(url)

        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")

        items = soup.find_all(
            "div", {"class": "BasePropertyCard_propertyCardWrap__J0xUj"}
        )
        for item in items:
            status = item.find(
                "div", "base__StyledType-rui__sc-108xfm0-0 kpUjhd message"
            ).text
            price = item.find(
                "div", "Pricestyles__StyledPrice-rui__btk3ge-0 bvgLFe card-price"
            ).text
            try:
                bed_parent = item.find(
                    "li",
                    "PropertyBedMetastyles__StyledPropertyBedMeta-rui__a4nnof-0 cHVLag",
                )
                bed = bed_parent.find("span", {"data-testid": "meta-value"}).text
            except:
                bed = np.nan

            try:
                bath_parent = item.find(
                    "li",
                    "PropertyBathMetastyles__StyledPropertyBathMeta-rui__sc-67m6bo-0 bSPXLm",
                )
                bath = bath_parent.find("span", {"data-testid": "meta-value"}).text
            except:
                bath = np.nan

            try:
                sqft_parent = item.find(
                    "li",
                    "PropertySqftMetastyles__StyledPropertySqftMeta-rui__sc-1gdau7i-0 fnhaOV",
                )
                sqft = sqft_parent.find("span", {"data-testid": "meta-value"}).text
            except:
                sqft = np.nan

            try:
                size_parent = item.find(
                    "li",
                    "PropertyLotSizeMetastyles__StyledPropertyLotSizeMeta-rui__sc-1cz4zco-0 cNMyen",
                )
                size = size_parent.find("span", {"data-testid": "meta-value"}).text
            except:
                size = np.nan

            try:
                address1 = item.find("div", {"data-testid": "card-address-1"}).text
            except:
                address1 = np.nan

            try:
                address2 = item.find("div", {"data-testid": "card-address-2"}).text
            except:
                address2 = np.nan

            try:
                product_link = item.find("a", "LinkComponent_anchor__2uAhr")["href"]
                product_link = "https://www.realtor.com" + product_link
            except:
                product_link = np.nan

            data = [
                product_link,
                status,
                price,
                bed,
                bath,
                sqft,
                size,
                address1,
                address2,
            ]

            final_data.append(data)

    driver.quit()

    cols = [
        "Product URL",
        "Status",
        "Price",
        "Bed",
        "Bath",
        "Sqft",
        "Acre Lot",
        "Address 1",
        "Address 2",
    ]
    df = pd.DataFrame(columns=cols, data=final_data)
    return df
