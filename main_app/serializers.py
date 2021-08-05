from rest_framework import serializers


class FieldsMappingSerializer(serializers.ModelSerializer):

    parentcode = serializers.SerializerMethodField(source='parentcode_id')
    budget = serializers.SerializerMethodField(source='budget_id')

    class Meta:
        model = ''
        fields = '__all__'

    def create(self, validated_data):
        updt_data, _ = self.Meta.model.objects.update_or_create(code=validated_data.get('code'),
                                                                defaults=validated_data)
        return updt_data

