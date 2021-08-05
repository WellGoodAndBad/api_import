from rest_framework.response import Response
from rest_framework import viewsets, status
from .mixins import ImportDataMixin
from .models import GlavBudgetClass, Budget
from .service import get_model_for_meta, GetApiData


class ApiImportSet(viewsets.ModelViewSet, ImportDataMixin):

    def get_serializer_class(self):
        """выбирает модель для сериализатора, в зависимости от параметров url.Например ?model=budget.
        То есть поля сериалитора будут меняться в записимости от указанной модели."""
        req_model = self.request.query_params.get('model')
        if req_model == 'glav_budget':
            return get_model_for_meta(GlavBudgetClass)
        if req_model == 'budget':
            return get_model_for_meta(Budget)

    def create(self, request, *args, **kwargs):
        req_param_model = self.request.query_params.get('model')
        if req_param_model:
            getApiData = GetApiData()
            datas = getApiData.get_data(url_param=req_param_model, num_page='1')  # получение данных
            page_count = datas.get('pageCount', '1')  # количество страниц с данными
            self.import_data_page(datas, req_param_model)  # импорт данных с 1й страницы

            for num_page in range(2, int(page_count)+1):  # импорт данных с остальных страниц
                datas = getApiData.get_data(url_param=req_param_model, num_page=str(num_page))
                self.import_data_page(datas, req_param_model)

            headers = self.get_success_headers('data imported')
            return Response(status=status.HTTP_201_CREATED, headers=headers)
        return Response(status=status.HTTP_200_OK)
