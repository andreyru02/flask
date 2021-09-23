from flask import request, jsonify
from flask.views import MethodView

from app import app
from models import Advertisement
from schema import USER_CREATE
from validator import validate


class AdvertisementView(MethodView):

    def get(self, ad_id):
        ad = Advertisement.by_id(ad_id)
        return jsonify(ad.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        ad = Advertisement(**request.json)
        ad.add()
        return jsonify(ad.to_dict())

    def delete(self, ad_id):
        ad = Advertisement.by_id(ad_id)
        ad.delete()
        return jsonify({'status': 200})


app.add_url_rule('/advertisements/<int:ad_id>', view_func=AdvertisementView.as_view('advertisements_get'),methods=['GET', ])
app.add_url_rule('/advertisements/', view_func=AdvertisementView.as_view('advertisements_create'), methods=['POST', ])
app.add_url_rule('/advertisements/<int:ad_id>', view_func=AdvertisementView.as_view('advertisements_delete'), methods=['DELETE', ])
