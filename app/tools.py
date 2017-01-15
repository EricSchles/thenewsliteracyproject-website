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


def increment_page(page_name,from_page,to_page,timestamp):
    page = SiteVisits.query.filter_by(page_name=page_name).first()
    page.overall_frequency += 1

    if timestamp.hour >=  
