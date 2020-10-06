from Accounts.models import Examinee, Examiner


def check(request):
    if request.user.is_authenticated:
        examinee = Examinee.objects.filter(user=request.user)
        examiner = Examiner.objects.filter(user=request.user)
        if examinee:
            return {'examinee': True}
        elif examiner:
            return {'examiner': True}
    return {}
