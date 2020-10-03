from Accounts.models import Examinee, Examiner


def check(request):
    examinee = Examinee.objects.filter(user=request.user)
    examiner = Examiner.objects.filter(user=request.user)
    if examinee:
        return {'examinee': True}
    if examiner:
        return {'examiner': True}
    return None