import datetime
import configuration

login_endpoints = {
    1: 'https://pv.inteless.com/oauth/token',
    2: 'https://api.sunsynk.net/oauth/token',
    3: 'https://www.solarkcloud.com/oauth/token'
}

plants_endpoints = {
    1: 'https://pv.inteless.com/api/v1/plants?page=1&limit=10&name=&status=',
    2: 'https://api.sunsynk.net/api/v1/plants?page=1&limit=10&name=&status=',
    3: 'https://www.solarkcloud.com/api/v1/plants?page=1&limit=10&name=&status='
}

energy_base_urls = {
    1: 'https://pv.inteless.com/api/v1/plant/energy/',
    2: 'https://api.sunsynk.net/api/v1/plant/energy/',
    3: 'https://www.solarkcloud.com/api/v1/plant/energy/'
}

flow_chart_endpoint = "flow"
day_readings_endpoint = "day?lan=en"
month_readings_endpoint = "month?lan=en"

def get_base_url():
    return energy_base_urls.get(configuration.REGION, energy_base_urls[1])

def get_flow_chart_endpoint(plant_id, date: datetime.date):
    energy_base_url = get_base_url()
    return f'{energy_base_url}{plant_id}/{flow_chart_endpoint}?date={date.strftime("%Y-%m-%d")}'

def get_day_readings_endpoint(plant_id, date: datetime.date):
    energy_base_url = get_base_url()
    return f'{energy_base_url}{plant_id}/{day_readings_endpoint}&date={date.strftime("%Y-%m-%d")}'

def get_month_readings_endpoint(plant_id, date):
    energy_base_url = get_base_url()
    return f'{energy_base_url}{plant_id}/{month_readings_endpoint}&date={date.strftime("%Y-%m")}&id={plant_id}'

def get_login_endpoint():
    return login_endpoints.get(configuration.REGION, login_endpoints[1])

def get_plants_endpoint():
    return plants_endpoints.get(configuration.REGION, plants_endpoints[1])
