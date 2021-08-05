from .serializers import FieldsMappingSerializer
import requests, traceback


def get_model_for_meta(model):
    """функция передают в Мета данные класс параметр модел"""
    serializer = FieldsMappingSerializer
    serializer.Meta.model = model
    return serializer


class GetApiData:
    urls = {
        'budget' : 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETS/data?pageSize=1000&filterstatus=ACTIVE&pageNum=',
        'glav_budget': 'http://budget.gov.ru/epbs/registry/7710568760-BUDGETCLASGRBSFB/data?pageSize=1000&pageNum=',
    }

    def get_data(self, url_param, num_page):
        url = ''
        if url_param == 'budget':
            url = self.urls['budget']
        if url_param == 'glav_budget':
            url = self.urls['glav_budget']

        try:
            response = requests.get(url=url+str(num_page))
            if response.status_code != 200:
                err_msg = 'Request to {} responded with status {}'.format(url, response.status_code)
                raise ValueError(err_msg)
            else:
                return response.json()
        except Exception:
            err_msg = 'Error in getting data\n' + str(traceback.format_exc())
            raise Exception(err_msg)

