from django.shortcuts import redirect

NOT_ALLOWED_URLS = ["/edit_profile/", "/new_task/", "/staff/task/", "/staff/main/", "/new_price/"]
ONLY_STAFF_URLS = ["/staff/task/", "/staff/main/", "/new_price/"]


class ConfirmUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(request.path)
        if request.user.is_authenticated:
            if not request.user.is_confirmed:
                if request.path in NOT_ALLOWED_URLS:
                    return redirect("/confirm/")
                elif request.path in ONLY_STAFF_URLS:
                    return redirect("/home/")
        if not request.user.is_staff:
            if request.path in ONLY_STAFF_URLS:
                return redirect("/home/")
        response = self.get_response(request)
        return response
