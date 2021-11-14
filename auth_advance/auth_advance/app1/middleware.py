from django.shortcuts import redirect

def articleMiddleware(get_response):
    def middleware(request):
        if not request.session.get('username'):
            print('middleware')
            return redirect('cLogin')
        response = get_response(request)
        return response
    return middleware
