import random
import string

from flask import redirect, render_template

from . import app, db
from .forms import URL_Form
from .models import URL_map


def get_unique_short_id():
    letters_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_digits, 6))
    if URL_map.query.filter_by(short=rand_string).first():
        return get_unique_short_id()
    return rand_string


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_Form()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = get_unique_short_id()
        url = URL_map(
            original=form.original_link.data,
            short=short_url,
        )
        db.session.add(url)
        db.session.commit()
        context = {'form': form, 'short_url': short_url}
        return render_template('main.html', **context)
    return render_template('main.html', form=form)


@app.route('/<string:short_url>')
def redirect_view(short_url):
    url = URL_map.query.filter_by(short=short_url).first_or_404()
    return redirect(url.original)
