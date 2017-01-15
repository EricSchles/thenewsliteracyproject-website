from app.models import SiteVisits
from app import db
import json


def initialize_page(page_name):
    if SiteVisits.query.filter_by(page_name=page_name).count() == 0:
        page = SiteVisits(
            page_name,
            json.dumps({}), # from_page
            json.dumps({}), # to_page
            0, # overall_frequency
            0, # monday_frequency
            0, # tuesday_frequency
            0, # wednesday_frequency
            0, # thursday_frequency
            0, # friday_frequency
            0, # saturday_frequency
            0, # sunday_frequency
            0, # weekday_frequency
            0, # weekend_frequency
            0, # morning_frequency
            0, # midday_frequency
            0, # afterwork_frequency
            0, # latenight_frequency
            json.dumps({}) # frequency_from_other_pages
        )  

        db.session.add(page)
        db.session.commit()
        return "initialized"
    else:
        return "already initialized"

def get_domain(url):
    if "/" in url.split("//")[1]:
        return url.split("//")[1].split("/")[0]
    else:
        return url.split("//")[1]
    
def increment_page_frequency_count(page_name, timestamp):
    """
    This function updates analytics based on when they visited the page.
    
    input:
    @page_name - assumed to be a string passed in from the route
    @timestamp - when the page was visited, assumed to be a python datetime object
    
    output:
    Output is sent to the database and the database object is returned 
    for debugging purposes
    """

    from_page_domain = get_domain(from_page)
    to_page_domain = get_domain(to_page)
    page = SiteVisits.query.filter_by(page_name=page_name).first()
    page.overall_frequency += 1

    # time of day frequency 
    if timestamp.hour >= 0 or timestamp.hour <= 5 or timestamp.hour >= 21:
        page.latenight_frequency += 1
    elif timestamp.hour >= 6 or timestamp.hour <= 11:
        page.morning_frequency += 1
    elif timestamp.hour >= 12 or timestamp.hour <= 17:
        page.midday_frequency += 1
    elif timestamp.hour >= 18 or timestamp.hour <= 20:
        page.afterwork_frequency += 1
    
    # day of week frequency
    if timestamp.weekday() == 0:
        page.monday_frequency += 1
    elif timestamp.weekday() == 1:
        page.tuesday_frequency += 1
    elif timestamp.weekday() == 2:
        page.wednesday_frequency += 1
    elif timestamp.weekday() == 3:
        page.thursday_frequency += 1
    elif timestmap.weekday() == 4:
        page.friday_frequency += 1
    elif timestamp.weekday() == 5:
        page.saturday_frequency += 1
    elif timestamp.weekday() == 6:
        page.sunday_frequency += 1

    # page visit during the week
    if timestamp.weekday() < 5:
        page.weekday_frequency += 1
    else:
        page.weekend_frequency += 1

    SiteVisits.query.filter_by(page_name=page_name).delete()
    db.session.add(page)
    db.session.commit()
    return page
