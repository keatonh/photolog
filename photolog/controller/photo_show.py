# -*- coding: utf-8 -*-
"""
    photolog.controller.photo_show
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    업로드된 사진을 보여준다.
    
    :copyright: (c) 2013 by 4mba.
    :license: MIT LICENSE 2.0, see license for more details.
"""


import os
from flask import request, redirect, url_for, current_app, send_from_directory \
				, render_template, session
from werkzeug.utils import secure_filename

from photolog.database import DBManager
from photolog.model.photo import Photo
from photolog.controller.login import login_required
from photolog.exif_reader import EXIFReader

from photolog.photolog_blueprint import photolog
from datetime import datetime
import uuid



@photolog.route('/photo/show/all')
@login_required
def show_all():
    dao = DBManager.db_session
    
    return render_template('entry_all.html', photos=dao.query(Photo).order_by(Photo.upload_date.desc()).all())