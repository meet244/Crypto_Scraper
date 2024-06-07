from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer
from .tasks import scrape_coin_data

class TaskManagerViewSet(viewsets.ViewSet):
    """
    A viewset for managing tasks.
    """

    @action(detail=False, methods=['post'])
    def start_scraping(self, request):
        """
        Start scraping task.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: The HTTP response object.
        """
        coins = request.data
        print(coins)
        print(type(coins))
        task = Task.objects.create()
        scrape_coin_data.delay(task.id, coins)
        return Response({"job_id": task.id}, status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=['get'])
    def scraping_status(self, request, pk=None):
        """
        Get the status of a scraping task.

        Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the task.

        Returns:
        - Response: The HTTP response object.
        """
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
