from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from jobsite.models import Company,Job
from jobsite.serializer import CompanySerializer
from jobsite.serializer import JobSerializer ,UserSerializer
from django.contrib.auth.models import User
from jobsite.models import CustomUser
from django.db.models import Q

# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Company.objects.all()
    serializer_class =CompanySerializer

class JobView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=Job.objects.all()
    serializer_class = JobSerializer

class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class SearchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=self.request.query_params.get('search')
        if query:
            c=Company.objects.filter(Q(company_name__icontains=query)|Q(description__icontains=query))
            j=Job.objects.filter(Q(job_title__icontains=query)|Q(location=query)|Q(description__icontains=query)|Q(skills__icontains=query)|Q(experience__icontains=query))
            if not (c.exists or j.exists):
                return Response({'msg':'No Search Results'},status=status.HTTP_200_OK)
            cs = CompanySerializer(c, many=True)
            js= JobSerializer(j,many=True)
            return Response(cs.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No Results'}, status=status.HTTP_200_OK)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':"Logout Successfully"},status=status.HTTP_200_OK)
