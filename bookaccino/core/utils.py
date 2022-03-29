def logged_in_switch_view(logged_in_view, logged_out_view):
    def inner_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return logged_in_view(request, *args, **kwargs)
        return logged_out_view(request, *args, **kwargs)

    return inner_view
