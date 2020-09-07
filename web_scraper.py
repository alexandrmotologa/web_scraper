from pyquery import PyQuery as pq

cat_target = 'https://999.md/ru/list/computers-and-office-equipment/laptops'

def scanOneAd999Page(target_url):
    document = pq(url=target_url)

    heading = document('h1').text()
    phone = document('.adPage__content__phone').find('a').text()
    image = document('#js-ad-photos').find('img').eq(0).attr('src')

    return {
        'title': heading,
        'image': image,
        'phone': phone
    }


def scanOneAdCategory999Page(target_url):
    prefix = 'https://999.md'
    document = pq(url=target_url)

    adds = []

    links_to_ads = document('.ads-list-photo-item').find('.ads-list-photo-item-title')

    for link in links_to_ads:
        try:
            url = pq(link).find('a').attr('href')
            adds.append(scanOneAd999Page(prefix+url))
        except :
            print('attribute error')

    return adds


adds = scanOneAdCategory999Page(cat_target)
print(adds)