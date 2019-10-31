class SetRemoteAddrFromForwardedFor(object):

    def process_request(self, request):
        try:
            real_ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
        except KeyError:
            pass
        else:
            if real_ip:
                real_ip = real_ip.split(',')[0]
                request.META['REMOTE_ADDR'] = real_ip
