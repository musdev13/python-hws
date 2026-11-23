import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from django.shortcuts import render


API_URL = 'https://countries.trevorblades.com/'
COUNTRY_FIELDS = '''
  code
  name
  native
  capital
  currency
  emoji
  continent { code name }
  languages { code name native }
'''


def graphql(query):
    body = json.dumps({'query': query}).encode('utf-8')
    request = Request(
        API_URL,
        data=body,
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'DjangoCountriesHomework/1.0',
        },
        method='POST',
    )
    try:
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode('utf-8'))
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        return None, f'Не вдалося отримати дані з API: {exc}'

    if payload.get('errors'):
        return None, payload['errors'][0].get('message', 'Помилка API')
    return payload.get('data', {}), None


def countries(request):
    data, error = graphql('{ countries { ' + COUNTRY_FIELDS + ' } }')
    items = sorted(data.get('countries', []), key=lambda item: item['name']) if data else []
    return render(request, 'countries/countries.html', {
        'countries': items,
        'error': error,
    })


def country_detail(request, code):
    data, error = graphql(
        '{ country(code: "' + code.upper() + '") { ' + COUNTRY_FIELDS + ' } }'
    )
    country = data.get('country') if data else None
    if country is None and error is None:
        error = 'Країну не знайдено.'
    return render(request, 'countries/country_detail.html', {
        'country': country,
        'error': error,
    })


def capital_detail(request, code):
    data, error = graphql(
        '{ country(code: "' + code.upper() + '") { code name capital emoji continent { name } } }'
    )
    country = data.get('country') if data else None
    if country is None and error is None:
        error = 'Інформацію про столицю не знайдено.'
    return render(request, 'countries/capital_detail.html', {
        'country': country,
        'error': error,
    })


def regions(request):
    data, error = graphql('{ continents { code name } }')
    items = sorted(data.get('continents', []), key=lambda item: item['name']) if data else []
    return render(request, 'countries/regions.html', {
        'regions': items,
        'error': error,
    })


def region_detail(request, code):
    query = '''
    { continent(code: "''' + code.upper() + '''") {
        code name
        countries { code name native capital emoji }
      }
    }
    '''
    data, error = graphql(query)
    region = data.get('continent') if data else None
    if region is not None:
        region['countries'] = sorted(region['countries'], key=lambda item: item['name'])
    if region is None and error is None:
        error = 'Регіон не знайдено.'
    return render(request, 'countries/region_detail.html', {
        'region': region,
        'error': error,
    })


def languages(request):
    data, error = graphql('{ languages { code name native } countries { code name capital emoji languages { code name } } }')
    if not data:
        data = {}

    language_list = sorted(data.get('languages', []), key=lambda item: item['name'])
    selected_code = request.GET.get('code', '')
    selected = next((item for item in language_list if item['code'] == selected_code), None)
    countries_by_language = []

    if selected is not None:
        countries_by_language = sorted(
            [
                item for item in data.get('countries', [])
                if any(language['code'] == selected_code for language in item['languages'])
            ],
            key=lambda item: item['name'],
        )

    return render(request, 'countries/languages.html', {
        'languages': language_list,
        'selected': selected,
        'countries': countries_by_language,
        'error': error,
    })
