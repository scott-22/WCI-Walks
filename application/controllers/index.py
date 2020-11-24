import datetime

from flask import Blueprint, url_for, redirect, render_template, request, session
from application.templates.utils import get_all_time_leaderboard, get_day_leaderboard

from application.models import database

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=('GET',))
def home():
    db = database.get_db()
    with db.cursor() as cur:
        total = database.get_total(cur)
    
    return render_template(
        'index.html',
        alltimeleaderboard=get_all_time_leaderboard(),
        yesterdayleaderboard=get_day_leaderboard(datetime.date.today()-datetime.timedelta(days=1)),
        total=total
    )