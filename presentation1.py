from zeep import Client

client = Client(wsdl='http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
country_iso_code = input('Enter Country code to get its capital')


print(client.service.CapitalCity(country_iso_code))