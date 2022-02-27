from main.models import Index, IndexInfluence, PopularIndex


def clean_min(min):
    new_min = min.replace(",", "")
    return float(new_min)


def clean_max(max):
    new_max = max.replace(",", "")
    return float(new_max)


def clean_final_price(final_price):
    new_final_price = final_price.replace(",", "")
    return float(new_final_price)


def clean_influence(influence):
    influence = influence.replace(",", "")
    influence = influence.replace("(", "")
    new_influence = influence.replace(")", "")
    return float(new_influence)


def clean_final_deal(final_deal):
    final_deal = final_deal.replace(",", "")
    final_deal = final_deal.replace("(", "")
    new_final_deal = final_deal.replace(")", "")
    return float(new_final_deal)


def clean_value(value):
    value = value.replace(",", "")
    value = value.replace(" M", "")
    new_value = value.replace(" B", "")
    return float(new_value)


def clean_volume(volume):
    volume = volume.replace(",", "")
    volume = volume.replace(" M", "")
    new_volume = volume.replace(" B", "")
    return float(new_volume)


def clean_count(count):
    new_count = count.replace(",", "")
    return int(new_count)


def clean_price(price):
    price = price.replace(",", "")
    price = price.replace("(", "")
    new_price = price.replace(")", "")
    return float(new_price)


def clean_percentage(percentage):
    percentage = percentage.replace(",", "")
    percentage = percentage.replace(")", "")
    new_percentage = percentage.replace("(", "")
    return float(new_percentage)


def clean_change(change):
    change = change.replace(",", "")
    change = change.replace(")", "")
    new_change = change.replace("(", "")
    return float(new_change)


def clean_last_value(last_value):
    new_last_value = last_value.replace(",", "")
    return float(new_last_value)


class CrawlingPipelineMain(object):
    def process_item(self, item, spider):
        name = item['name']
        percentage = clean_percentage(item['percentage'])
        change = clean_change(item['change'])
        publish = item['publish']
        last_value = clean_last_value(item['last_value'])
        max = clean_max(item['max'])
        min = clean_max(item['min'])
        Index.objects.create(
            name=name,
            last_value=last_value,
            percentage=percentage,
            min=min,
            max=max,
            publish=publish,
            change=change,
        )

        return item


class CrawlingPipelinePopular(object):
    def process_item(self, item, spider):
        name = item['name']
        symbol = item['symbol']
        yesterday_price = clean_price(item['yesterday_price'])
        final_price = clean_price(item['final_price'])
        max_price = clean_price(item['max_price'])
        min_price = clean_price(item['max_price'])
        count = clean_count(item['count'])
        volume = clean_volume(item['volume'])
        value = clean_value(item['value'])
        final_deal = clean_final_deal(item['final_deal'])

        PopularIndex.objects.create(
            name=name,
            symbol=symbol,
            yesterday_price=yesterday_price,
            final_price=final_price,
            max_price=max_price,
            min_price=min_price,
            count=count,
            volume=volume,
            final_deal=final_deal,
            value=value
        )

        return item


class InfluenceCrawlingPipeline(object):
    def process_item(self, item, spider):
        name = item['name']
        symbol = item['symbol']
        final_price = clean_final_price(item['final_price'])
        influence = clean_influence(item['influence'])

        IndexInfluence.objects.create(
            name=name,
            symbol=symbol,
            final_price=final_price,
            influence=influence
        )

        return item
