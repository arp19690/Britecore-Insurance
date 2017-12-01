from .models import RiskTypes
from .models import RiskTypeFields
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render_to_response
from django.views import View

# Create your views here.
class RiskView(APIView):
    def get(self, request):
        query_id = request.GET.get('id', None)

        try:
            if query_id is None:
                risk_types = RiskTypes.objects.order_by('name')
            else:
                if query_id.isdigit():
                    risk_types = RiskTypes.objects.filter(id=query_id)
                else:
                    raise ValueError('Invalid input. Only integers allowed.')

            output = self.fetch_children(risk_types)
            return Response(output)
        except ValueError as e:
            return Response({'Error': str(e)})

    def fetch_children(self, risk_type_obj):
        result_list = list()
        try:
            for rt in risk_type_obj:
                risk_type_fields = RiskTypeFields.objects.filter(risk_type=rt).order_by(
                    'field_name')
                result_list.append({'id': rt.id,
                                    'risk_type': rt.name,
                                    'fields': risk_type_fields.values('display_name',
                                                                      'field_name',
                                                                      'field_type')})
            return result_list
        except Exception as e:
            return Response({'Error': str(e)})


class RiskHTML(View):
    def get(self, request):
        return render_to_response('risks/index.html')
