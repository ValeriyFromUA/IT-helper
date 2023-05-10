from django.views.generic import ListView
from ..models import Feedback


class CommentsView(ListView):
    template_name = "comments.html"
    model = Feedback
    context_object_name = "comments"
    ordering = ["-id"]
    paginate_by = 10
