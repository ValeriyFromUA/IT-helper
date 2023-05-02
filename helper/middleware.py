from django.shortcuts import redirect

ALLOWED_URLS = ["/confirm/", "/login/", "/logout/", "/home/", "", "/staff/registration/", "/staff/login/",
                "/registration/", "/confirm_staff/", "/admin/", "/fast_task/"]
ONLY_STAFF_URLS = ["/staff/task/", "/staff/main/"]


class ConfirmUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if not request.user.is_confirmed:
                if request.path not in ALLOWED_URLS:
                    return redirect("/confirm/")
            elif not request.user.is_staff:
                if request.path in ONLY_STAFF_URLS:
                    return redirect("/home/")
        else:
            if request.path not in ALLOWED_URLS:
                return redirect("/home/")
        response = self.get_response(request)
        return response
