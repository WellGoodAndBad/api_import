from .models import GlavBudgetClass, Budget


class ImportDataMixin:
    def import_data_page(self, import_data_, model_import_data):
        data_list = []
        for i in import_data_.get('data', []):
            if i.get('enddate') == '':
                i['enddate'] = None

            if model_import_data == 'budget':
                if i.get('status').lower() == 'active':
                    obj = Budget.objects.filter(code=i.get('code')).first()
                    i['parentcode_id'] = obj.id if obj is not None else None

            data_list.append(i)

        serializer = self.get_serializer(data=data_list, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)