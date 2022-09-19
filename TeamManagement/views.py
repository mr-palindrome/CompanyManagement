from django.shortcuts import render
from rest_framework import views, generics, viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import Q
from django.core.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .queries import *
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

# Create your views here.


class CompanyViewNoPK(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    model = Company
    queryset = company_query()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, *args, ** kwargs):
        return self.list(request, *args, ** kwargs)
    def post(self, request, *args, ** kwargs):
        return self.create(request, *args, ** kwargs)



class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = company_query()
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GetCompanyById(generics.RetrieveAPIView):
    model = Company
    serializer_class = CompanySerializer
    queryset = company_query()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class GetCompanyByName(generics.ListAPIView):
    model = Company
    serializer_class = CompanySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = company_query()
    lookup_url_kwarg = "name"

    def get_queryset(self, *args, **kwargs):
        name = self.kwargs.get(self.lookup_url_kwarg)
        if name is not None:
            company = company_name_filter_query(name)
            return company

        else:
            company = company_query()
            return company




class TeamViewNoPK(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    model = Team
    queryset = team_query()
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    def get(self, request, *args, ** kwargs):
        return self.list(request, *args, ** kwargs)
    def post(self, request, *args, ** kwargs):
        return self.create(request, *args, ** kwargs)



class TeamView(generics.RetrieveUpdateDestroyAPIView):
    model = Team
    queryset = team_query()
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class CreateTeamByCompanyID(generics.CreateAPIView):
    model = Team
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    def post(self, *args, **kwargs):
        company_id = self.kwargs.get(self.lookup_url_kwarg)
        team_lead_name = self.request.data.get("team_lead_name")
        company = company_id_filter_query(company_id)
        team = Team.objects.create(team_lead_name=team_lead_name, company=company)
        return Response(status= HTTP_200_OK, data={"id": team.id})


class GetTeamByCompanyID(generics.ListAPIView):
    model = Team
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = team_query()

    def list(self, *args, **kwargs):
        queryset = company_query()
        serializer = CompanySerializer(queryset, many=True)
        company_data = serializer.data
        for query in queryset:
            team = self.queryset.filter(company=query)
            team_serializer = TeamByCompanyIDSerializer(team, many=True)
            team_data = team_serializer.data
            for data in company_data:
                if data["id"] == str(query.id):
                    data["teams"] = team_data
        return Response(status= HTTP_200_OK, data={"data": company_data})
