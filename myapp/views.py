from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup
from .serializers import CountryInfoSerializer
def scrape_wikipedia_infobox(url):
    # Send a GET request to the Wikipedia page
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the infobox table
    infobox = soup.find('table', class_='infobox')

    # Extract the information from the infobox
    flag_img = infobox.find('img')
    flag_link = flag_img['src']
    # capital = infobox.find('td', text='Capital').find_next_sibling('td').text.strip()
    capital_td = infobox.find('td', text='Capital')
    if capital_td:
        capital = capital_td.find_next_sibling('td').text.strip()
    else:
        capital = None
    largest_city_td = infobox.find('td', text='Largest city')
    if largest_city_td:
        largest_city = largest_city_td.find_next_sibling('td').text.strip()
    else:
        largest_city = None
    official_languages_td = infobox.find('td', text='Official languages')
    if official_languages_td:
        official_languages = [language.strip() for language in official_languages_td.find_next_sibling('td').text.split(',')]
    else:
        official_languages = None
    area_total_td = infobox.find('td', text='Area')
    if area_total_td:
        area_total = area_total_td.find_next_sibling('td').text.strip()
    else:
        area_total = None
    population_td = infobox.find('td', text='Population')
    if population_td:
        population = population_td.find_next_sibling('td').text.strip()
    else:
        population = None
    gdp_nominal_td = infobox.find('td', text='GDP (nominal)')
    if gdp_nominal_td:
        gdp_nominal = gdp_nominal_td.find_next_sibling('td').text.strip()
    else:
        gdp_nominal = None

    # Store the information in a dictionary
    data = {
        'flag_link': flag_link,
        'capital': capital,
        'largest_city': largest_city,
        'official_languages': official_languages,
        'area_total': area_total,
        'population': population,
        'gdp_nominal': gdp_nominal
    }

    return data



@api_view(['GET'])
def country_info(request, country_name):
    # Scrape the information from the Wikipedia page
    url = f"https://en.wikipedia.org/wiki/{country_name}"
    """response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('h1').text
    capital = soup.find(class_='fn org').text
    population = soup.find(class_='nowrap').text
    area = soup.find(class_='nowrap').find_next_sibling('td').text"""
    
    # Create a dictionary with the scraped information
    data = scrape_wikipedia_infobox(url)
    
    # Return the JSON response
    serializer = CountryInfoSerializer(data)
    return Response(serializer.data)
